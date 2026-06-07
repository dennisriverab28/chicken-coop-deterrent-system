import RPi.GPIO as GPIO
import time

# Relay control pins
RELAY_1_PIN = 17  # Controls polarity to COM of actuator
RELAY_2_PIN = 27  # Controls opposite polarity

class PolarityRelayController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RELAY_1_PIN, GPIO.OUT)
        GPIO.setup(RELAY_2_PIN, GPIO.OUT)
        self.stop()
        print("[RELAY] System initialized. Relays OFF.")

    def extend(self):
        # Relay 1 LOW, Relay 2 HIGH
        GPIO.output(RELAY_1_PIN, GPIO.HIGH)
        GPIO.output(RELAY_2_PIN, GPIO.HIGH)
        print("[RELAY] EXTEND: Relay 1 = LOW, Relay 2 = HIGH.")

    def retract(self):
        # Relay 1 HIGH, Relay 2 LOW
        GPIO.output(RELAY_1_PIN, GPIO.LOW)
        GPIO.output(RELAY_2_PIN, GPIO.LOW)
        print("[RELAY] RETRACT: Relay 1 = HIGH, Relay 2 = LOW.")

    def stop(self):
        # Both LOW (default/failsafe)
        GPIO.output(RELAY_1_PIN, GPIO.HIGH)
        GPIO.output(RELAY_2_PIN, GPIO.LOW)
        print("[RELAY] STOPPED: Both relays LOW (no power).")

    def cleanup(self):
        self.stop()
        GPIO.cleanup()
        print("[CLEANUP] GPIO cleanup complete.")
