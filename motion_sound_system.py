import RPi.GPIO as GPIO
import time
import pygame
import random

# GPIO Pins
PIR_PIN = 21
LIGHT_PIN = 16

# Sound file paths
sound_files = [
    "sounds/dog_barking.mp3",
    "sounds/alarm-301729.mp3",
    "sounds/an-eagle-squawking-overhead-226774.mp3",
    "sounds/duck-quacking-37392.mp3",
    "sounds/hawk-78766.mp3",
    "sounds/howling-wolves-6965.mp3",
    "sounds/hawk-78766.mp3",
    "sounds/lion-roaring-sfx-293295.mp3",
    "sounds/rooster-cry-chicken-rooster-305576.mp3",
    "sounds/tiger-attack-195840.mp3",
    "sounds/wolf-howl-6310.mp3",
    "sounds/geese.mp3"
]

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LIGHT_PIN, GPIO.OUT, initial=GPIO.HIGH)

# Setup Pygame Mixer
pygame.mixer.init()
previous_sound = None

def play_random_sound():
    global previous_sound
    available = [s for s in sound_files if s != previous_sound]
    sound = random.choice(available)
    previous_sound = sound

    print(f"[SOUND] Playing: {sound}")
    try:
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
    except Exception as e:
        print(f"[ERROR] Sound failed: {e}")

def flash_light(times=5, delay=0.3):
    for i in range(times):
        GPIO.output(LIGHT_PIN, GPIO.LOW)
        print(f"[FLASH] ON ({i+1})")
        time.sleep(delay)
        GPIO.output(LIGHT_PIN, GPIO.HIGH)
        print(f"[FLASH] OFF ({i+1})")
        time.sleep(delay)
    GPIO.output(LIGHT_PIN, GPIO.HIGH)
    print("[FLASH] Done. Light OFF.")

def motion_handler():
    print("[SYSTEM] Monitoring for motion...")
    try:
        while True:
            if GPIO.input(PIR_PIN):
                print("[MOTION] Motion detected!")
                flash_light()
                play_random_sound()
                print("[SYSTEM] Cooldown...")
                time.sleep(3)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("[EXIT] Program interrupted.")
        GPIO.cleanup()
