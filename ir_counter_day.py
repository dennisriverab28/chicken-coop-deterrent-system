import RPi.GPIO as GPIO
import time
from event_logger import log_event
from sunrise_sunset_control import SunriseSunsetController

IR_SENSOR_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

sun = SunriseSunsetController()
chicken_count = 0

def monitor_ir_sensor_day():
    global chicken_count
    print("[IR] Monitoring IR sensor during the day...")
    while True:
        if sun.check_sun_times() == "open":
            if GPIO.input(IR_SENSOR_PIN) == GPIO.LOW:
                chicken_count += 1
                print(f"[IR] Chicken Entered! Total: {chicken_count}")
                log_event("IR Chicken Detected", f"Count: {chicken_count}")
                time.sleep(5)
        else:
            time.sleep(5)
