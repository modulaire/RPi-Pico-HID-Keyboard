## RPi-Pico-HID-Keyboard
Much like the input of a MakeyMakey, or an Arduino Leonardo, using a Raspberry Pico with CircuitPython we can prepare a device to behave like a keyboard when connected to a computer.<br/>
<br/>
__You must use CircuitPython 7.0.0 or higher__ in order for the included codes to work. After installing CircuitPython on the Pico, simply copy the codes _boot.py_ and _code.py_ to the device. Also copy the entire folder titled *adafruit_hid*. With several buttons wired up to designated pins you should immediately see results after unplugging, re-plugging the Pico and opening a basic text editor on your computer. <br/>
<br/>
All pins and keyboard character mapping are found in the file _code.py_ <br/>
All buttons/switches added to the device are to be connected to ground. Internal Pull-Up resistors are activated in the code, so no need to add them in your circuit <br/>
##### You will need to add a button to GPIO pin 0. To edit your code on the Pico, this pin must be pulled LOW when connecting the device to your computer. Otherwise you will be locked out and the device will behave only as a keyboard.

#### references:

[adafruit_hid module for CircuitPython (github page)](https://github.com/adafruit/Adafruit_CircuitPython_HID/tree/main/adafruit_hid)

[adafruit: customizing usb devices in circuit python](https://learn.adafruit.com/customizing-usb-devices-in-circuitpython)

[CircuitPython download for Raspberry Pico](https://circuitpython.org/board/raspberry_pi_pico/) 

[DIY pico mechanical keyboard (code was taken from here)](https://learn.adafruit.com/diy-pico-mechanical-keyboard-with-fritzing-circuitpython/code-the-pico-keyboard)
