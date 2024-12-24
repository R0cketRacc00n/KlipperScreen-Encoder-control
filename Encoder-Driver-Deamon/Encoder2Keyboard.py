from gpiozero import RotaryEncoder, Button
from evdev import UInput, ecodes as e
import time
import signal

# Configurable Variables
pin_a = 27 # Encoder A Pin
pin_b = 17 # Encoder B Pin
pin_button = 22 # Encoder Switch (SW) Pin
hold_time = 10 # Time that holding the button
ui = UInput()

def button_hold():
    ui.write(e.EV_KEY, e.KEY_ENTER, 1)  # KEY_A down
    ui.write(e.EV_KEY, e.KEY_ENTER, 0)  # KEY_A up
    ui.syn()

def button_pressed():
    ui.write(e.EV_KEY, e.KEY_ENTER, 1)  # KEY_A down
    ui.write(e.EV_KEY, e.KEY_ENTER, 0)  # KEY_A up
    ui.syn()


def ChangeFocus():
    global encoder
    steps = encoder.steps
    if steps > 0:
        ui.write(e.EV_KEY, e.KEY_TAB, 1)  # KEY_A down
        ui.write(e.EV_KEY, e.KEY_TAB, 0)  # KEY_A up
        ui.syn()
    elif steps < 0:
        ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)  # KEY_A down
        ui.write(e.EV_KEY, e.KEY_TAB, 1)  # KEY_A down
        ui.write(e.EV_KEY, e.KEY_TAB, 0)  # KEY_A up
        ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 0)  # KEY_A down
        ui.syn()
    encoder.steps = 0  # Reset encoder steps after each move

# Set up GPIO devices
encoder = RotaryEncoder(pin_a, pin_b)
encoder.when_rotated = ChangeFocus

button = Button(pin_button)
button.hold_time = hold_time
button.when_held = button_hold
button.when_pressed = button_pressed

# Keep the script running
signal.pause()

