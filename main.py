from machine import Pin
import time

led = Pin("LED", Pin.OUT)

def blink(times, duration):
    for _ in range(times):
        led.value(1)
        time.sleep(duration)
        led.value(0)
        time.sleep(duration)
while True:
    blink(3, 0.25)
    blink(3, 0.5)
    blink(3, 0.25)
    time.sleep(3)
    
