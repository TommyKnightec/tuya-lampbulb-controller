
import tinytuya
import time
import keyboard
from lightbulb_methods import *

DEVICEID = "" # Replace this with your device id
DEVICEIP = "" # Replace this with your device IP
DEVICEKEY = "" # Replace this with the key found by tiny tuya scanner
DEVICEVERS = "3.3" # Replace this with your device version. At the time of writing most bulbs seem to be version 3.3.

# Validate that all required strings are filled out
if not all([DEVICEID, DEVICEIP, DEVICEKEY, DEVICEVERS]):
    print("Error: One or more required fields are missing!")
    if not DEVICEID:
        print("DEVICEID is missing.")
    if not DEVICEIP:
        print("DEVICEIP is missing.")
    if not DEVICEKEY:
        print("DEVICEKEY is missing.")
    if not DEVICEVERS:
        print("DEVICEVERS is missing.")
    exit()

# Initialize the bulb device
print('Looking for device...')
d = tinytuya.BulbDevice(DEVICEID, DEVICEIP, DEVICEKEY)
d.set_version(float(DEVICEVERS))  # Always set version
d.set_socketPersistent(True)  # Keep socket connection open

# Set initial brightness and color
set_brightness(d, 50)
set_color(d, 0)

print("Use arrow keys to control the bulb. Up/Down to adjust brightness. Left/Right to change color.")
print("Press ESC, 'E', or 'Q' to exit the program.")

try:
    turn_on(d)
    while True:
        if keyboard.is_pressed('up'):
            increase_brightness(d, 10)
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('down'):
            decrease_brightness(d, 10)
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('right'):
            next_color(d)
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('left'):
            prev_color(d)
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('o') or keyboard.is_pressed('1') :
            turn_on(d)
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('f') or keyboard.is_pressed('0') :
            turn_off(d)
            time.sleep(0.2)  # Debounce delay

        # Check for ESC, E, or Q key to exit
        if keyboard.is_pressed('esc') or keyboard.is_pressed('e') or keyboard.is_pressed('q'):
            print("Exit key pressed. Exiting program...")
            break

except KeyboardInterrupt:
    print("Program exited by user.")

finally:
    turn_off(d)
    print("Bulb turned off.")
