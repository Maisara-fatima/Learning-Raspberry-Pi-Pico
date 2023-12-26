import machine
import utime
import urandom


pressed = False

led = machine.Pin(15,machine.Pin.OUT)
top_button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
bottom_button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
fastest_button = None


def button_handler(pin):
    global pressed
    if not pressed:
        pressed = True
        global fastest_button
        fastest_button = pin 
        
        
led.value(1)
utime.sleep(urandom.uniform(5,10))
led.value(0)
timer_start = utime.ticks_ms()
top_button.irq(trigger=machine.Pin.IRQ_RISING, handler = button_handler)
bottom_button.irq(trigger=machine.Pin.IRQ_RISING, handler = button_handler)

while fastest_button is None:
    utime.sleep(1)
if fastest_button is top_button:
    print(" The Top player wins! ")
    
elif fastest_button is bottom_button:
    print(" The Bottom player wins! " )
