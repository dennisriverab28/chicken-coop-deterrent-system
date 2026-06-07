import RPi.GPIO as GPIO
import time

DIR_PIN=5
STEP_PIN= 6
STEP_DELAY =0.0008

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)

try:
	while True:	
		#open (Clockwise)
		GPIO.output(DIR_PIN,GPIO.HIGH)
		start_time=time.time()
		while (time.time() - start_time)<7:
			GPIO.output(STEP_PIN,GPIO.HIGH)
			time.sleep(STEP_DELAY)
			GPIO.output(STEP_PIN,GPIO.LOW)
			time.sleep(STEP_DELAY)
			
		time.sleep(1)#pause
		
		
		#close (counter-clockwise)
		GPIO.output(DIR_PIN,GPIO.LOW)
		start_time=time.time()
		while (time.time() - start_time)<7:
			GPIO.output(STEP_PIN,GPIO.HIGH)
			time.sleep(STEP_DELAY)
			GPIO.output(STEP_PIN,GPIO.LOW)
			time.sleep(STEP_DELAY)
			
		time.sleep(1)#pause
	

except KeyboardInterrupt:
	print("Program Interrupted")
finally:
	GPIO.cleanup()
	
