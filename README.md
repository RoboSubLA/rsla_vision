# RoboSubLA Computer Vision 


# ROS 2 Iron Installation Guide for Ubuntu 22.04

This guide provides steps to install ROS 2 Iron on Ubuntu 22.04. Follow these instructions carefully to set up your environment.

## 1. System Setup

### Set Locale
Ensure that your locale supports UTF-8. If in a minimal environment (e.g., a docker container), your locale may be minimal like POSIX. We recommend using the following settings:

```bash
# Check for UTF-8 locale
locale  

# Install locales if necessary
sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

# Verify settings
locale  
```

## 2. Enable Required Repositories

### Add the ROS 2 Apt Repository
First, make sure the Ubuntu Universe repository is enabled:

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

Next, add the ROS 2 GPG key:

```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

Add the repository to your sources list:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

## 3. Install Development Tools (Optional)

If you plan to build ROS 2 packages or do development, install the development tools:

```bash
sudo apt update && sudo apt install ros-dev-tools
```

## 4. Install ROS 2

First, update your apt repository caches:

```bash
sudo apt update
```

### Important Note
Before installing ROS 2, ensure that your system is fully updated:

```bash
sudo apt upgrade
```

### Desktop Install (Recommended)
This includes ROS, RViz, demos, and tutorials:

```bash
sudo apt install ros-iron-desktop
```

### ROS-Base Install (Bare Bones)
For a minimal installation with only communication libraries, message packages, and command-line tools (no GUI tools):

```bash
sudo apt install ros-iron-ros-base
```

## 5. Install Additional RMW Implementations (Optional)
By default, ROS 2 uses Fast DDS. You can install and switch to different middleware implementations if needed. For more information, refer to the ROS 2 documentation.

## 6. Setup Environment

After installation, set up your environment by sourcing the following file:

```bash
# Replace '.bash' with your shell if you're not using bash
source /opt/ros/iron/setup.bash
```

## 7. Try Some Examples

### C++ Talker
In one terminal, source the setup file and run the C++ talker:

```bash
source /opt/ros/iron/setup.bash
ros2 run demo_nodes_cpp talker
```

### Python Listener
In another terminal, source the setup file and run the Python listener:

```bash
source /opt/ros/iron/setup.bash
ros2 run demo_nodes_py listener
```

You should see the talker publishing messages and the listener receiving them, confirming that both the C++ and Python APIs are working properly.

## 8. Next Steps

You can continue with the [tutorials and demos](https://docs.ros.org/en/iron/Tutorials.html) to configure your environment, create your own workspace, and learn core ROS 2 concepts.

## 9. Optional: Use the ROS 1 Bridge
To connect topics between ROS 1 and ROS 2, refer to the [ROS 1 bridge documentation](https://docs.ros.org/en/iron/Tutorials/ROS1-Bridge.html).

## 10. Troubleshooting
If you encounter any issues, refer to the [ROS 2 troubleshooting guide](https://docs.ros.org/en/iron/Tutorials/Troubleshooting.html).

## 11. Uninstall ROS 2

To uninstall ROS 2:

```bash
sudo apt remove ~nros-iron-* && sudo apt autoremove
```

You may also want to remove the repository:

```bash
sudo rm /etc/apt/sources.list.d/ros2.list
sudo apt update
sudo apt autoremove
sudo apt upgrade
```

---