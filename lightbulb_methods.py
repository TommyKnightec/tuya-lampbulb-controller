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

# Get a list of the colors in the rainbow
colors = list(rainbow.keys())

def status(device):
    data = device.status()
    print('Device status: %r' % data)

def clamp(value, min_value=0, max_value=100):
    return max(min_value, min(value, max_value))

def set_brightness(device, level):
    global brightness_level

    clamped_level = clamp(level, 0, 100) # Clamp the value before sending it to bulb
    brightness_level = clamped_level # Set global variable to new level
    print(f'Setting brightness to {brightness_level}%')
    device.set_brightness_percentage(brightness_level)

def increase_brightness(device, amount):
    global brightness_level

    new_brightness = brightness_level + amount
    set_brightness(device, new_brightness)

def decrease_brightness(device, amount):
    global brightness_level

    new_brightness = brightness_level - amount
    set_brightness(device, new_brightness)

def set_color(device, new_index):
    global color_index
    global brightness_level

    color_index = new_index % len(colors) # Force the index to be in bounds
    color_name = colors[color_index]
    r, g, b = rainbow[color_name]

    # Adjust the RGB values based on the current brightness level
    brightness_factor = brightness_level / 100
    r = int(r * brightness_factor)
    g = int(g * brightness_factor)
    b = int(b * brightness_factor)

    print(f'Setting color to {color_name} ({r}, {g}, {b})')
    device.set_colour(r, g, b)

def next_color(device):
    global color_index

    index = color_index + 1
    set_color(device, index)

def prev_color(device):
    global color_index

    index = (color_index - 1)
    set_color(device, index)

def turn_on(device):
    print('Turning on')
    device.turn_on()

def turn_off(device):
    print('Turning off')
    device.turn_off()
