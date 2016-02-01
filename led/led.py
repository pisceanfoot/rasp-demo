import RPi.GPIO as GPIO
import time

PIN_NO = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NO, GPIO.OUT)

try:
	for i in range(5):

		print 'times %s' % (i + 1)
		GPIO.output(PIN_NO,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(PIN_NO,GPIO.LOW)
		time.sleep(1)
except KeyboardInterrupt:
	pass
finally:
	GPIO.cleanup()