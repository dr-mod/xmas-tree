# Xmas Tree
A simple pattern for a 3D RGB Xmas Tree and RPi.

## Hardware
* Raspberry Pi
* 3D RGB Xmas Tree for Raspberry Pi

## Installation
1. Install dependencies
    ```
    sudo apt install python3-gpiozero
    ```
2. Download the script
    ```
    git clone https://github.com/dr-mod/xmas-tree.git ~/xmas-tree
    ```
3. Run it 
    ```
    python3 ~/xmas-tree/main.py
    ```
4. To make it run on startup
    1. `nano /etc/rc.local` 
    2. Add one the following before `exit 0`
    ```
    /usr/bin/python3 /home/pi/xmas-tree/main.py&
    ```
    conversely, you can run in `screen`
    ```
    su - pi -c "/usr/bin/screen -dm sh -c '/usr/bin/python3 /home/pi/xmas-tree/main.py'"
    ```
