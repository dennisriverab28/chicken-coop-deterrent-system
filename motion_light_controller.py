import RPi.GPIO as GPIO
import time

# GPIO Pins
PIR_PIN = 21       # PIR motion sensor
LIGHT_PIN = 16     # Relay IN pin for light (active LOW)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LIGHT_PIN, GPIO.OUT, initial=GPIO.HIGH)  # Start with light OFF

def monitor_motion():
    print("[SYSTEM] Motion detection system initialized.")
    print("[SYSTEM] Waiting for motion...")

    try:
        while True:
            if GPIO.input(PIR_PIN):  # Motion detected
                print("[MOTION] Detected! Flashing light...")

                for i in range(5):
                    GPIO.output(LIGHT_PIN, GPIO.LOW)   # Turn ON relay (active LOW)
                    print(f"[FLASH] Light ON ({i+1})")
                    time.sleep(0.3)

                    GPIO.output(LIGHT_PIN, GPIO.HIGH)  # Turn OFF relay
                    print(f"[FLASH] Light OFF ({i+1})")
                    time.sleep(0.3)

                GPIO.output(LIGHT_PIN, GPIO.HIGH)  # Ensure light is OFF
                print("[SYSTEM] Flashing complete. Light OFF. Waiting for PIR to reset...")
                time.sleep(3)  # Optional delay to prevent re-triggering too fast

            time.sleep(0.1)

    except KeyboardInterrupt:
        print("[EXIT] Motion monitoring stopped by user.")
        GPIO.cleanup()
