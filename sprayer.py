# sprayer.py
import pigpio
import time

SERVO_PIN = 17  # BCM pin
pi = pigpio.pi()

if not pi.connected:
    raise Exception("Could not connect to pigpio daemon")

def spray_water(times=5):
    for _ in range(times):
        pi.set_servo_pulsewidth(SERVO_PIN, 2000)  # Spray
        time.sleep(0.5)
        pi.set_servo_pulsewidth(SERVO_PIN, 1000)  # Reset
        time.sleep(0.5)

    pi.set_servo_pulsewidth(SERVO_PIN, 0)  # Stop signal

def cleanup():
    pi.stop()
