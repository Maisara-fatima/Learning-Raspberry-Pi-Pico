import machine 
import utime

led_external = machine.Pin(15, machine.Pin.OUT)

#The LED is connected to GPIO pin 15 and is set as an output pin

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

#The button is connected to GPIO pin 14 and is set as an input pin with a pull-down resistor.

while True:
    
    if button.value() == 1:

# This checks if the button is pressed.
        
        led_external.value(1)

#If the button is pressed, this turns on the external LED

        utime.sleep(1)

#This means the LED will stay on for 1 second after the button is pressed.

    led_external.value(0)  

#This turns off the external LED by setting its value to 0.
