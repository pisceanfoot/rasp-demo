import RPi.GPIO as GPIO
import time

PIN_NO = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_NO, GPIO.OUT)

for i in range(20):
	GPIO.output(PIN_NO,GPIO.HIGH)
	time.sleep(2)
	GPIO.output(PIN_NO,GPIO.LOW)
	time.sleep(2)

GPIO.cleanup()