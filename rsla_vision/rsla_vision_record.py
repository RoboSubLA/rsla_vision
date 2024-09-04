import cv2
from ultralytics import YOLO
import os, sys

frame_rate = 10
prev_time = 0

rec_path = os.path.expanduser("~/rsla-rec/")

def main(args = None):
    cap = cv2.VideoCapture(0)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Get frame info

    size = (frame_width, frame_height)

    print("Frame dimensions: ", size)
    
    # Find next filename
    output_filename_prefix = "rsla_vid_output_"
    output_type = "mp4"
    output_filename_iterator = 0
    output_filename = ""
    output_fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    output_file_created = False

    while output_filename_iterator < 100:
        output_filename = os.path.join(rec_path, f'{output_filename_prefix}{output_filename_iterator:>02}.{output_type}')

        if not os.path.isfile(output_filename):
            output_file_created = True
            break

        output_filename_iterator += 1

    if not output_file_created:
        print("No output filenames available")
        sys.exit(-2)

    # Create output object
    out = cv2.VideoWriter(output_filename, output_fourcc, 30, size)

    if not out.isOpened():
        print(f"Error creating video output {output_filename}")
        sys.exit(-3)

    print(f"Created video output at {output_filename}")

    # Loop until stopped
    running = True

    while(running):
        try:
            # Get new webcam frame
            ret, frame = cap.read()

            # Write the image
            out.write(frame)
        except KeyboardInterrupt:
            running = False

    print("\nDestroying objects")
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
