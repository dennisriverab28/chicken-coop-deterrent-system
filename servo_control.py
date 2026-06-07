import pigpio
import time
import math

SERVO_PIN1 = 25  # GPIO25
SERVO_PIN2 = 24  # GPIO24

# Initialize pigpio and set mode
pi = pigpio.pi()
pi.set_mode(SERVO_PIN1, pigpio.OUTPUT)
pi.set_mode(SERVO_PIN2, pigpio.OUTPUT)

# Function to set servo angle
def set_angle(angle):
    pulse_width = 500 + int((angle / 180.0) * 2000)
    pi.set_servo_pulsewidth(SERVO_PIN1, pulse_width)
    pi.set_servo_pulsewidth(SERVO_PIN2, pulse_width)


try:
    while True:
        for t in range(0, 360, 3):
            angle = 90 + 90 * math.sin(math.radians(t))
            set_angle(angle)
            time.sleep(0.01)
        # set_angle(0)
        # time.sleep(0.6)

        # set_angle(120)
        # time.sleep(0.6)

    
finally:
    print("Releasing servos")
    pi.set_servo_pulsewidth(SERVO_PIN1, 0)
    pi.set_servo_pulsewidth(SERVO_PIN2, 0)
    pi.stop()



