from lightbulb import LightBulb
import time
import keyboard

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

lightbulb = LightBulb(device_id=DEVICEID, device_ip=DEVICEIP, device_key=DEVICEKEY, device_version=DEVICEVERS)


print("Use arrow keys to control the bulb. Up/Down to adjust brightness. Left/Right to change color.")
print("Press ESC, 'E', or 'Q' to exit the program.")

try:
    lightbulb.turn_on()
    while True:
        if keyboard.is_pressed('up'):
            lightbulb.increase_brightness(10)
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('down'):
            lightbulb.decrease_brightness(10)
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('right'):
            lightbulb.next_color()
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('left'):
            lightbulb.prev_color()
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('o') or keyboard.is_pressed('1') :
            lightbulb.turn_on()
            time.sleep(0.2)  # Debounce delay

        if keyboard.is_pressed('f') or keyboard.is_pressed('0') :
            lightbulb.turn_off()
            time.sleep(0.2)  # Debounce delay

        # Check for ESC, E, or Q key to exit
        if keyboard.is_pressed('esc') or keyboard.is_pressed('e') or keyboard.is_pressed('q'):
            print("Exit key pressed. Exiting program...")
            break

except KeyboardInterrupt:
    print("Program exited by user.")

finally:
    lightbulb.turn_off()
    print("Bulb turned off.")
