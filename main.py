
import tinytuya
import time
import keyboard

DEVICEID = "" # Replace this with your device id
DEVICEIP = "" # Replace this with your device IP
DEVICEKEY = "" # Replace this with the key found by tiny tuya scanner
DEVICEVERS = "3.3" # Replace this with your device version. At the time of writing most bulbs seem to be version 3.3.

# Initialize the bulb device
print('Looking for device...')
d = tinytuya.BulbDevice(DEVICEID, DEVICEIP, DEVICEKEY)
d.set_version(float(DEVICEVERS))  # Always set version
d.set_socketPersistent(True)  # Keep socket connection open

# Initial brightness and color index
brightness_level = 50  # Initial brightness level in percentage
color_index = 0  # Start with the first color in the rainbow

# Initial brightness and color index
brightness_level = 50  # Initial brightness level in percentage
color_index = 0  # Start with the first color in the rainbow

# Rainbow color dictionary
rainbow = {
    "red": [255, 0, 0],
    "orange": [255, 127, 0],
    "yellow": [255, 200, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
    "indigo": [46, 43, 95],
    "violet": [139, 0, 255]
}


def status():
    d = tinytuya.Device(DEVICEID, DEVICEIP, DEVICEKEY, version=DEVICEVERS)
    data = d.status()
    print('Device status: %r' % data)
# Get a list of the colors in the rainbow
colors = list(rainbow.keys())

def clamp(value, min_value=0, max_value=100):
    return max(min_value, min(value, max_value))
def set_brightness(level):
    global brightness_level

    clamped_level = clamp(level, 0, 100) # Clamp the value before sending it to bulb
    brightness_level = clamped_level # Set global variable to new level
    print(f'Setting brightness to {brightness_level}%')
    d.set_brightness_percentage(brightness_level)

def increase_brightness(amount):
    global brightness_level

    new_brightness = brightness_level + amount
    set_brightness(new_brightness)

def decrease_brightness(amount):
    global brightness_level

    new_brightness = brightness_level - amount
    set_brightness(new_brightness)

def next_color():
    global color_index

    index = color_index + 1
    set_color(index)

def prev_color():
    global color_index
    
    index = (color_index - 1)
    set_color(index)
def set_color(index):
    global color_index

    color_index = index % len(colors) # Force the index to be in bounds
    color_name = colors[color_index]
    r, g, b = rainbow[color_name]
    print(f'Setting color to {color_name} ({r}, {g}, {b})')
    d.set_colour(r, g, b)
def turn_on():
    print('Turning on')
    d.turn_on()
def turn_off():
    print('Turning off')
    d.turn_off()

# Set initial brightness and color
set_brightness(brightness_level)
set_color(color_index)

print("Use arrow keys to control the bulb. Up/Down to adjust brightness. Left/Right to change color.")
print("Press ESC, 'E', or 'Q' to exit the program.")

try:
    turn_on()
    while True:
        if keyboard.is_pressed('up'):
            increase_brightness(10)
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('down'):
            decrease_brightness(10)
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('right'):
            next_color()
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('left'):
            prev_color()
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('o') or keyboard.is_pressed('1') :
            turn_on()
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('f') or keyboard.is_pressed('0') :
            turn_off()
            time.sleep(0.2)  # Debounce delay

        # Check for ESC, E, or Q key to exit
        if keyboard.is_pressed('esc') or keyboard.is_pressed('e') or keyboard.is_pressed('q'):
            print("Exit key pressed. Exiting program...")
            break

except KeyboardInterrupt:
    print("Program exited by user.")

finally:
    d.turn_off()
    print("Bulb turned off.")
