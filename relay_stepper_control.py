import RPi.GPIO as GPIO
import time

# GPIO pin setup (BCM mode)
DIR_PIN = 5
STEP_PIN = 6
RELAY_PIN = 18  # Controls power to stepper driver

STEP_DELAY = 0.001  # 1ms per pulse

class RelayStepperController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DIR_PIN, GPIO.OUT)
        GPIO.setup(STEP_PIN, GPIO.OUT)
        GPIO.setup(RELAY_PIN, GPIO.OUT)
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn OFF relay initially

    def power_on(self):
        GPIO.output(RELAY_PIN, GPIO.LOW)  # Active LOW relay
        print("[RELAY] Power ON to stepper driver.")

    def power_off(self):
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Deactivate
        print("[RELAY] Power OFF to stepper driver.")

    def rotate(self, direction="cw", duration=5):
        if direction == "cw":
            GPIO.output(DIR_PIN, GPIO.HIGH)
            print("[STEPPER] Rotating CLOCKWISE.")
        else:
            GPIO.output(DIR_PIN, GPIO.LOW)
            print("[STEPPER] Rotating COUNTERCLOCKWISE.")

        start_time = time.time()
        while time.time() - start_time < duration:
            GPIO.output(STEP_PIN, GPIO.HIGH)
            time.sleep(STEP_DELAY)
            GPIO.output(STEP_PIN, GPIO.LOW)
            time.sleep(STEP_DELAY)

    def cleanup(self):
        self.power_off()
        GPIO.cleanup()
        print("[CLEANUP] GPIO cleaned up.")
