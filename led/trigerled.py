import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 12)  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(25, GPIO.IN)    # set GPIO 25 as input  
GPIO.setup(18, GPIO.OUT)

GPIO.output(18,GPIO.HIGH)

try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(25): # if port 25 == 1  
            print "Port 25 is 1/GPIO.HIGH/True - button pressed"  
            GPIO.output(18,GPIO.HIGH)
        else:  
            print "Port 25 is 0/GPIO.LOW/False - button not pressed"  
            GPIO.output(18,GPIO.LOW)
        sleep(1)
  
except KeyboardInterrupt:  
    GPIO.cleanup()         # clean up after yourself 
