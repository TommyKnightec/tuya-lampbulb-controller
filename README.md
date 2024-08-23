# Tuya lamp controller

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Setup

This project relies on [TinyTuya](https://github.com/jasonacox/tinytuya), a Python module to interface with Tuya-compatible smart devices. Before you can use this project, please follow the instructions on the TinyTuya repository.

Make sure your devices are correctly set up and connected to the cloud as described in the TinyTuya documentation.

Once everything is set up, you're ready to use this project.

## Key Map

The project uses keyboard input to control the smart bulb. Below is a description of what each key does:

- **Up Arrow (`↑`)**: Increases the brightness by 10%, up to a maximum of 100%.
- **Down Arrow (`↓`)**: Decreases the brightness by 10%, down to a minimum of 0%.
- **Right Arrow (`→`)**: Cycles forward through the available colors.
- **Left Arrow (`←`)**: Cycles backward through the available colors.
- **Lowercase `o` or `1`**: Turns the smart bulb on.
- **Lowercase `f` or `0`**: Turns the smart bulb off.
- **`ESC`, lowercase `e`, or lowercase `q`**: Exits the program.

The program includes a debounce delay of 0.2 seconds to prevent accidental multiple inputs.
