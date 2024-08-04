To get started on your "MINI WEATHER STATION" project, let's break down the requirements and steps needed:

*Hardware Setup*

1. Raspberry Pi 4B:
   - Install Raspbian OS.
   - Ensure you have internet connectivity (either Wi-Fi or Ethernet).
2. DHT 11 Sensor:
   - Connect the DHT 11 sensor to the GPIO pins of the Raspberry Pi.
   - You may need a pull-up resistor (4.7k or 10k ohm) for stable readings.
3. Camera Module:
   - Attach the camera module to the CSI port on the Raspberry Pi.
   - Enable the camera interface in raspi-config.
4. 7-inch Screen:
   - Connect the Screen to the HDMI port of the Raspberry Pi.
   - Adjust the display settings in the Raspberry Pi configuration if necessary.

*Software Setup*
1. Install Required Libraries:
   ```
   sudo apt-get update
   sudo apt-get install python3-pip
   sudo pip3 install Adafruit_DHT
   ```
2. For the camera module:
   ```
   sudo apt-get install python3-picamera
   ```
3. For displaying graphics:
   ```
   sudo apt-get install python3-matplotlib
   ```
4. For the database (SQLite):
   ```
   sudo apt-get install sqlite3
   sudo pip3 install sqlite3
   ```
5. Install Tkinter (if not already installed):
   ```
   sudo apt-get install python3-tk
   ```
