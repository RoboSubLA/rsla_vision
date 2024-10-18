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

---

# Installing Anaconda and OpenCV on Ubuntu/Linux

## Prerequisites

Anaconda comes with the `anaconda-navigator` package, which includes the dependency package `qt`. Some GUI applications might require additional dependencies to function properly on Linux systems. To ensure compatibility, install the following extended dependencies:

### Debian-based systems (including Ubuntu)

```bash
sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
```

## Installation

### Step 1: Download Anaconda Installer

Visit [Anaconda's official download page](https://repo.anaconda.com/archive/) to download the latest installer. Alternatively, you can download it via the terminal using the following command (replace `<INSTALLER_VERSION>` with the desired version):

```bash
# Example for Linux x86_64
curl -O https://repo.anaconda.com/archive/Anaconda3-<INSTALLER_VERSION>-Linux-x86_64.sh
```

### Step 2: Verify Installer Integrity (Optional)

To verify the integrity of the installer, you can use the following command (replace `<INSTALLER_VERSION>` with the correct version):

```bash
sha256sum Anaconda3-<INSTALLER_VERSION>-Linux-x86_64.sh
```

Compare the output with the checksum provided on Anaconda's website.

### Step 3: Install Anaconda

Run the installer using the following command (replace `<INSTALLER_VERSION>` with the correct version):

```bash
bash ~/Downloads/Anaconda3-<INSTALLER_VERSION>-Linux-x86_64.sh
```

Follow the on-screen prompts:
1. Press `Enter` to review the license.
2. Type `yes` to accept the license agreement.
3. Press `Enter` to accept the default install location or specify a different directory.

### Step 4: Initialize Conda

After installation, Anaconda recommends initializing `conda`. You can either accept the prompt to run `conda init` or do it manually:

```bash
source ~/anaconda3/bin/activate
conda init
```

Close and reopen the terminal for changes to take effect or run:

```bash
source ~/.bashrc
```

### Step 5: Verify Installation

Once Anaconda is installed, you can verify the installation by launching Anaconda Navigator:

```bash
anaconda-navigator
```

Alternatively, verify with `conda`:

```bash
conda list
```

You should see a list of installed packages in your base environment.

## Installing OpenCV with Conda

To install OpenCV using `conda`, you can use one of the following commands:

### Method 1: Install from `conda-forge` Channel

```bash
conda install conda-forge::opencv
```

### Method 2: Install from other labels (if needed)

```bash
conda install conda-forge/label/broken::opencv
conda install conda-forge/label/cf201901::opencv
conda install conda-forge/label/cf202003::opencv
conda install conda-forge/label/gcc7::opencv
```

## Additional Resources

- [Anaconda Documentation](https://docs.anaconda.com/)
- [OpenCV Documentation](https://docs.opencv.org/4.x/)

