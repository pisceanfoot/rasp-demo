import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 12)  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  

READ_PORT = 24
LED_OUT_PORT = 18

GPIO.setup(READ_PORT, GPIO.IN)    # set GPIO as input  
GPIO.setup(LED_OUT_PORT, GPIO.OUT)

GPIO.output(LED_OUT_PORT,GPIO.HIGH)

try:  
    while True:            # this will carry on until you hit CTRL+C  
    	VALUE = GPIO.input(READ_PORT)
    	print VALUE
        if VALUE: # if port == 1  
            print "Port is 1/GPIO.HIGH/True - button pressed"  
            GPIO.output(LED_OUT_PORT,GPIO.HIGH)
        else:  
            print "Port is 0/GPIO.LOW/False - button not pressed"  
            GPIO.output(LED_OUT_PORT,GPIO.LOW)
        sleep(0.2)
  
except KeyboardInterrupt:  
    GPIO.cleanup()         # clean up after yourself 

# sleep(5)
# GPIO.cleanup()