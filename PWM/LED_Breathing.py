import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(16, GPIO.OUT)

p = GPIO.PWM(16, 300)  # channel=16 frequency=300Hz
p.start(0)

try:
    while 1:
        for dc in range(0, 101, 2):
            p.ChangeDutyCycle(dc)
            time.sleep(0.03)
        for dc in range(100, -1, -2):
            p.ChangeDutyCycle(dc)
            time.sleep(0.03)

except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()
