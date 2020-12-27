import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(21,GPIO.IN)

def switchPressed(channel):
  print("Someone is Detected")
  GPIO.output(16,1)
  time.sleep(5)
  GPIO.output(16,0)


GPIO.add_event_detect(21, GPIO.RISING, callback=switchPressed)

try:
  while 1:
    print(".")
    time.sleep(5)
finally:
  GPIO.cleanup()