import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)

my_pwm = GPIO.PWM(16,300)
my_pwm.start(100)

stopit = False

while(stopit != True):
        dutycycle = input("Enter ( 0 to QUIT) ")
        if dutycycle ==0:
                stopit = True
        my_pwm.ChangeDutyCycle(int(dutycycle))

GPIO.cleanup()
