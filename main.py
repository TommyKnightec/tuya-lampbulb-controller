
import tinytuya
import time
import keyboard

DEVICEID = "bf29c3ffa8ddbd78892mit"
DEVICEIP = "192.168.0.110"
DEVICEKEY = "dad8e175b0be17cf"
DEVICEVERS = "3.3"

# Initialize the bulb device
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

def set_brightness(level):
    print(f'Setting brightness to {level}%')
    d.set_brightness_percentage(level)

def set_color(index):
    color_name = colors[index]
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
    while True:
        if keyboard.is_pressed('up'):
            if brightness_level < 100:
                brightness_level += 10
                set_brightness(brightness_level)
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('down'):
            if brightness_level > 0:
                brightness_level -= 10
                set_brightness(brightness_level)
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('right'):
            color_index = (color_index + 1) % len(colors)
            set_color(color_index)
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('left'):
            color_index = (color_index - 1) % len(colors)
            set_color(color_index)
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