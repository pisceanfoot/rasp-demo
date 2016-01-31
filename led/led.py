import RPI.GPIO as GPIO
import time

PIN_OUT = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_NO, GPIO.OUT)
GPIO.output(PIN_NO,GPIO.HIGH)

time.sleep(20)

GPIO.cleanup()