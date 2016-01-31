import RPi.GPIO as GPIO
import time

PIN_NO = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NO, GPIO.OUT)

try:
	for i in range(5):
		print 'times %s' % (i + 1)
		GPIO.output(PIN_NO,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PIN_NO,GPIO.LOW)
		time.sleep(2)
		GPIO.cleanup()
except KeyboardInterrupt:
	GPIO.cleanup()
