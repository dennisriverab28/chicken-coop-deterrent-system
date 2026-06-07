import os
import random
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# List of sound files (update paths if needed)
sound_files = [
    "sounds/dog_barking.mp3",
    "sounds/geese.mp3"
]

# Keep track of the previous sound
previous_sound = None

def play_random_sound():
    global previous_sound

    print("[DEBUG] Available sounds:", sound_files)

    # Avoid repeating the same sound
    options = [s for s in sound_files if s != previous_sound]
    sound = random.choice(options)
    previous_sound = sound

    print(f"[SOUND] Playing: {sound}")
    try:
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"[ERROR] Could not play sound: {e}")
