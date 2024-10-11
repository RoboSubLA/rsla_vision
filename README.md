# RoboSubLA Computer Vision 

## ROS2 Installation 
`locale  # check for UTF-8` \
`sudo apt update && sudo apt install locales`\
`sudo locale-gen en_US en_US.UTF-8` \
`sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8` \
`export LANG=en_US.UTF-8`\
`Locale  # verify settings`

```sudo apt install software-properties-common``` \
```sudo add-apt-repository universe``` \
```sudo apt update && sudo apt install curl -y ``` \
```sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg``` 

```echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null```

```sudo apt update``` \
```sudo apt upgrade``` \
Desktop Install for ROS, RViz, demos, tutorials \
```sudo apt install ros-iron-desktop```

### Environment setup
Replace ".bash" with your shell if you're not using bash\
Possible values are: setup.bash, setup.sh, setup.zsh\
```source /opt/ros/iron/setup.bash ```

### Watch ROS2 tutorial videos for futher help
[YOUTUBE](https://www.youtube.com/@RoboticsBackEnd)

