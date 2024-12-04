''' 
Description: ROS 2 PUBLISHER node for object detection using YOLOv5 and publishing detections to the RSLA system
 


 Notes Log:
 2024-11-10: Comments added by Will M.
'''


import cv2
from ultralytics import YOLO
import os, sys

#Imported ROS 2 libraries
import rclpy                                                   
import rclpy.logging                                                        
from rclpy.node import Node
import rclpy.subscription
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

from rsla_interfaces.msg import Detection
from rsla_interfaces.msg import DetectionArray

from math import tan, radians

import time

frame_rate = 10
prev_time = 0

bridge = CvBridge()

dir_path = os.path.dirname(os.path.realpath(__file__))

node = None
model = None
model_classes = []

class_widths = [22.86, 304.8, 30.48, 7.62, 7.62, 30.48, 335.28, 60.96]

detections = []

image_resolution = (640, 640)
image_fov = (80, 64)

start_time = 0

detections_msg = DetectionArray()

det_pub = None

def time_millis():
    return round(time.time() * 1000) - start_time

def set_start_time():
    start_time = time_millis()

def image_callback(img_msg):
    global node
    global model
    global detections

    current_time = time_millis()

    try:
        orig_image = bridge.imgmsg_to_cv2(img_msg, "bgr8")
        cv_image = cv2.resize(orig_image, (640, 640))

        results = model.predict(cv_image)

        boxes = results[0].boxes.xyxy.cpu().tolist()
        classes = results[0].boxes.cls.cpu().tolist()
        confidences = results[0].boxes.conf.cpu().tolist()

        raw_detections = list(zip(boxes, classes, confidences))

        # Reset all current detections
        for det in detections:
            det["detected"] = False

        # Process new detections
        for det in raw_detections:
            # Disregard low confidence predictions & gate legs (for now, because there's two of them in every frame)
            det_class = int(det[1])

            if det[2] < 0.7 or model_classes[det_class] == "gate_leg":
                continue

            # Only consider confident predictions
            det_center_x = (det[0][0] + det[0][2]) / 2
            det_center_y = (det[0][1] + det[0][3]) / 2
            det_width = (det[0][2] - det[0][0])
            det_height = (det[0][3] - det[0][1])

            # Get angles
            det_yaw_rel_angle = (image_fov[0] * (det_center_x - (image_resolution[0] / 2))) / image_resolution[0]
            det_pitch_rel_angle = (image_fov[1] * (det_center_y - (image_resolution[1] / 2))) / image_resolution[1]

            # Approximate distance (will be shit but alas)
            rel_angular_size = (det_width / image_resolution[0]) * image_fov[0]
            approx_distance = class_widths[det_class] / tan(radians(rel_angular_size))

            detections[det_class] = { "timestamp" : current_time, "class": det_class, "detected": True, "confidence": det[2], "angle": (det_yaw_rel_angle, det_pitch_rel_angle), "distance": approx_distance, "center": (det_center_x, det_center_y), "size": (det_width, det_height) }
    except CvBridgeError as e:
        print(f"CvBridgeError: {e}")

def publish_detection_array():
    global detections
    global detections_msg
    global det_pub

    current_time = time_millis()

    for index, detection in enumerate(detections):
        if detection:
            new_detection = Detection()
            
            new_detection.id = int(detection["class"])
            new_detection.detected = detection["detected"]
            new_detection.confidence = float(detection["confidence"])
            new_detection.millis_since_last_detected = current_time - detection["timestamp"]
            new_detection.ang_x = float(detection["angle"][0])
            new_detection.ang_y = float(detection["angle"][1])
            new_detection.distance = float(detection["distance"])

            detections_msg.detections[index] = new_detection

    det_pub.publish(detections_msg)

def main(args = None):
    global node
    global model
    global model_classes
    global detections
    global det_pub

    set_start_time()

    # Create the YOLO network
    model = YOLO(os.path.expanduser("~/cv_model/best.pt"))
    model_classes = model.names

    print(model_classes)

    for index in model_classes:
        detections.append({ "timestamp" : 0, "class": index, "detected": False, "confidence": 0, "angle": (0, 0), "distance": 0.0, "center": (0, 0), "size": (0, 0) })

        default_detection = Detection(detected=False)
        detections_msg.detections.append(default_detection)

    # Init the ROS node
    rclpy.init(args = args)

    # Create the node
    node = rclpy.create_node('rsla_vision')

    # Initialize the image subscriber
    img_sub = node.create_subscription(Image, '/front_camera/image_raw', image_callback, 1)
    img_sub

    # Initialize the detection subscriber
    det_pub = node.create_publisher(DetectionArray, "rsla/vision/detections", 1)

    det_pub_timer = node.create_timer(0.5, publish_detection_array)
    det_pub_timer

    while rclpy.ok():
        rclpy.spin_once(node)

    # Explicitly destroy node
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
