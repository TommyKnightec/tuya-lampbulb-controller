import tinytuya
class LightBulb:
    def __init__(self, device_id="", device_ip="", device_key="", device_version="3.3"):
        # Validate that all required strings are filled out
        if not all([device_id, device_ip, device_key, device_version]):
            raise ValueError("Error: One or more required fields are missing!")

        self.device_id = device_id
        self.device_ip = device_ip
        self.device_key = device_key
        self.device_version = device_version

        self.device = tinytuya.BulbDevice(device_id, device_ip, device_key)
        self.device.set_version(float(device_version))
        self.device.set_socketPersistent(True)

        self.brightness_level = 50  # Initial brightness level in percentage
        self.color_index = 0  # Start with the first color in the rainbow

        # Rainbow color dictionary
        self.rainbow = {
            "red": [255, 0, 0],
            "orange": [255, 127, 0],
            "yellow": [255, 200, 0],
            "green": [0, 255, 0],
            "blue": [0, 0, 255],
            "indigo": [46, 43, 95],
            "violet": [139, 0, 255]
        }

        # Get a list of the colors in the rainbow
        self.colors = list(self.rainbow.keys())

    def status(self):
        data = self.device.status()
        print('Device status: %r' % data)

    def clamp(self, value, min_value=0, max_value=100):
        return max(min_value, min(value, max_value))

    def set_brightness(self, level):
        clamped_level = self.clamp(level, 0, 100)
        self.brightness_level = clamped_level
        print(f'Setting brightness to {self.brightness_level}%')
        self.device.set_brightness_percentage(self.brightness_level)

    def increase_brightness(self, amount):
        new_brightness = self.brightness_level + amount
        self.set_brightness(new_brightness)

    def decrease_brightness(self, amount):
        new_brightness = self.brightness_level - amount
        self.set_brightness(new_brightness)

    def set_color(self, index):
        self.color_index = index % len(self.colors)
        color_name = self.colors[self.color_index]
        r, g, b = self.rainbow[color_name]

        # Adjust the RGB values based on the current brightness level
        brightness_factor = self.brightness_level / 100
        r = int(r * brightness_factor)
        g = int(g * brightness_factor)
        b = int(b * brightness_factor)

        print(f'Setting color to {color_name} ({r}, {g}, {b})')
        self.device.set_colour(r, g, b)

    def next_color(self):
        index = self.color_index + 1
        self.set_color(index)

    def prev_color(self):
        index = self.color_index - 1
        self.set_color(index)

    def turn_on(self):
        print('Turning on')
        self.device.turn_on()

    def turn_off(self):
        print('Turning off')
        self.device.turn_off()