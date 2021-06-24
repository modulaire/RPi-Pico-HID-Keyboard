import board
from digitalio import DigitalInOut, Direction, Pull
import storage

switch = digitalio.DigitalInOut(board.GP0)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

if not switch.value:
    storage.disable_usb_drive()    # Turn off CIRCUITPY