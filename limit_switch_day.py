import RPi.GPIO as GPIO
import time
from event_logger import log_event
from sunrise_sunset_control import SunriseSunsetController

LIMIT_SWITCH_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LIMIT_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

sun = SunriseSunsetController()
limit_switch_count = 0

def monitor_limit_switch_day():
    global limit_switch_count
    print("[LIMIT] Monitoring limit switch during the day...")
    while True:
        if sun.check_sun_times() == "open":
            if GPIO.input(LIMIT_SWITCH_PIN) == GPIO.LOW:
                limit_switch_count += 1
                print(f"[LIMIT] Chicken Stepped! Total: {limit_switch_count}")
                log_event("Limit Switch Chicken Detected", f"Count: {limit_switch_count}")
                time.sleep(5)
        else:
            time.sleep(5)
