# Blackout-proof Xmas Tree
A pattern for a 3D RGB Xmas Tree and RPi.

![photo](docs/photo.jpeg)
## Hardware
* Raspberry Pi
* 3D RGB Xmas Tree for Raspberry Pi
* Waveshare UPS HAT

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
    /usr/bin/python3 /home/pi/xmas-tree/main.py &
    ```
    conversely, you can run in `screen`
    ```
    su - pi -c "/usr/bin/screen -dm sh -c '/usr/bin/python3 /home/pi/xmas-tree/main.py'"
    ```

### Support the project
If you would like to support this project and and keep me caffeinated, you can do it here:

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/drmod)
