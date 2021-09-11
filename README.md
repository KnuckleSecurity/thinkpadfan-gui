# Thinkpad Fan Tweaker GUI

<p align="left">
  <a href="https://github.com/krygeNNN/thinkpadfan-gui">
    <img src="Images/fan-icon-vector-15.png" alt="Logo" width="80" height="80">
  </a>
<p align="center">
  <a href="https://github.com/krygeNNN/thinkpadfan-gui">
    <img src="Images/thinkpadgui.png" alt="Logo" >
  </a>

## Description

Spesifically designed for ThinkPad/IBM laptops to twek fan speed with an graphical user interface.
You can also monitor CPU, GPU temperatures.

## Getting Started

### Dependencies

* Python3 libraries --> python3 python3-tk, subprocess, shlex
* Unix binaries --> lm-sensors
* OS --> Any Linux kernel with `thinkpad-acpi` patch. 

### Installing
 ```
  git clone https://github.com/krygeNNN/thinkpadfan-gui.git
  pip3 install -r requirements.txt
  ```
Arch Based
  ```
  sudo pacman -S lm-sensors
  ```
Debian Based
  ```
  sudo apt-get install lm-sensors
  ```

### Setup

* `echo options thinkpad_acpi fan_control=1 | sudo tee /etc/modprobe.d/thinkpad_acpi.conf`
* Reboot your computer.
* Run script with `sudo`
```
sudo python3 thinkpad_fan_gui.py
```
