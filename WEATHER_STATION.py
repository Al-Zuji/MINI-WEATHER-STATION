import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
import Adafruit_DHT
import sqlite3
import threading
import time
from picamera import PiCamera

# Sensor setup
sensor = Adafruit_DHT.DHT11
pin = 4  # GPIO pin where the sensor is connected

# Database setup
conn = sqlite3.connect('weather_station.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS weather (timestamp DATETIME, temperature REAL, humidity REAL)''')

# Camera setup
camera = PiCamera()

# Tkinter setup
root = tk.Tk()
root.title("Mini Weather Station")

# Labels for temperature and humidity
temp_label = tk.Label(root, text="Temperature: --.- C", font=("Helvetica", 16))
temp_label.pack(pady=10)

humidity_label = tk.Label(root, text="Humidity: --.- %", font=("Helvetica", 16))
humidity_label.pack(pady=10)

# Canvas for live camera feed
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Function to update sensor data
def update_sensor_data():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            temp_label.config(text=f"Temperature: {temperature:.1f} C")
            humidity_label.config(text=f"Humidity: {humidity:.1f} %")
            # Save to database
            c.execute("INSERT INTO weather (timestamp, temperature, humidity) VALUES (datetime('now'), ?, ?)", (temperature, humidity))
            conn.commit()
        else:
            temp_label.config(text="Failed to get reading. Try again!")
            humidity_label.config(text="")
        time.sleep(60)  # Read every minute

# Function to update live camera feed
def update_camera_feed():
    while True:
        camera.capture('/home/pi/weather_image.jpg')
        img = Image.open('/home/pi/weather_image.jpg')
        img = img.resize((640, 480), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
        canvas.image = img
        time.sleep(1)

# Function to capture and save image
def snap_and_save():
    camera.capture('/home/pi/snap_image.jpg')
    messagebox.showinfo("Image Captured", "Image saved as snap_image.jpg")

# Button to snap and save image
snap_button = tk.Button(root, text="Snap & Save Picture", command=snap_and_save)
snap_button.pack(pady=20)

# Start sensor and camera feed threads
sensor_thread = threading.Thread(target=update_sensor_data)
sensor_thread.daemon = True
sensor_thread.start()

camera_thread = threading.Thread(target=update_camera_feed)
camera_thread.daemon = True
camera_thread.start()

root.mainloop()
