import machine
import time
import neopixel
import ujson

with open("config.json") as f:
    config = ujson.load(f)

PWM_PIN = config["pwm_pin"]
NEOPIXEL_PIN = config["neopixel_pin"]
NUM_PIXELS = config["num_pixels"]

np = neopixel.NeoPixel(machine.Pin(NEOPIXEL_PIN), NUM_PIXELS)
pwm_pin = machine.Pin(PWM_PIN, machine.Pin.IN)

pulse_start = 0
pulse_width = 0

def pwm_callback(pin):
    global pulse_start, pulse_width
    if pin.value():
        pulse_start = time.ticks_us()
    else:
        pulse_width = time.ticks_diff(time.ticks_us(), pulse_start)

pwm_pin.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=pwm_callback)

def pulse_to_color(pulse_us):
    pulse_clamped = max(1000, min(2000, pulse_us))
    r = int(255 * (2000 - pulse_clamped) / 1000) if pulse_clamped < 1500 else 0
    g = int(255 * (1 - abs(pulse_clamped - 1500) / 500))
    b = int(255 * (pulse_clamped - 1000) / 1000) if pulse_clamped > 1500 else 0
    return (r, g, b)

while True:
    print("PWM ", pulse_width)
    color = pulse_to_color(pulse_width)
    for i in range(NUM_PIXELS):
        np[i] = color
    np.write()
    time.sleep_ms(100)
