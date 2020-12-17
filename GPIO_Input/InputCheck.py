import RPi.GPIO as GPIO

import time



GPIO.setmode(GPIO.BCM)

GPIO.setup(16,GPIO.OUT)

GPIO.setup(20,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#GPIO.setup(20,GPIO.IN)

try:
  while 1:
    if GPIO.input(20)==0:
      GPIO.output(16,0)
    else:
      GPIO.output(16,1)
 
finally:
  GPIO.cleanup()
