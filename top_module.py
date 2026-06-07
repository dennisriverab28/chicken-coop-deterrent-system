import time
from relay_polarity_control import PolarityRelayController
from relay_stepper_control import RelayStepperController
from motion_light_controller import monitor_motion
from motion_sound_system import flash_light, play_random_sound
from motion_sound_system import motion_handler
from sunset_sunrise_control import SunriseSunsetController

# Init components
actuator = PolarityRelayController()
stepper = RelayStepperController()
sun = SunriseSunsetController()

# Track status
actuator_extended = True
last_action = None

def open_coop():
    global actuator_extended, last_action
    if not actuator_extended:
        print("[COOP] Already OPEN.")
        return
    actuator.retract()
    time.sleep(20)
    actuator.stop()
    actuator_extended = False
    last_action = f"Opened at {time.strftime('%I:%M:%S %p')}"

def close_coop():
    global actuator_extended, last_action
    if actuator_extended:
        print("[COOP] Already CLOSED.")
        return
    actuator.extend()
    time.sleep(20)
    actuator.stop()
    actuator_extended = True
    last_action = f"Closed at {time.strftime('%I:%M:%S %p')}"

def auto_mode():
    global actuator_extended
    print("[AUTO MODE] Started. Ctrl+C to exit.")
    try:
        while True:
            if sun.needs_update():
                sun.fetch_sun_times()

            action = sun.check_sun_times()
            print(f"[AUTO CHECK] Status: {action.upper()}")

            if action == "open":
                open_coop()
            elif action == "close":
                close_coop()
            else:
                print("[AUTO] No action needed now.")

            time.sleep(600)
    except KeyboardInterrupt:
        print("\n[AUTO MODE] Stopped.")

def sim_mode():
    global actuator_extended
    while True:
        print("\n=== SIMULATION MODE ===")
        print("1) Simulate DAY (Open Coop)")
        print("2) Simulate NIGHT (Close Coop)")
        print("3) Exit Sim")
        sim = input("Choose: ").strip()

        if sim == "1":
            open_coop()
        elif sim == "2":
            close_coop()
        elif sim == "3":
            break
        else:
            print("Invalid choice.")

def main_menu():
    while True:
        print("\n========== CHICKEN COOP MAIN MENU ==========")
        print("1) Run Auto Mode (Sunrise/Sunset)")
        print("2) Simulate Day/Night")
        print("3) Test Actuator via Relay")
        print("4) Test Stepper Motor")
        print("5) Flashing Light Only")
        print("6) Random Sound Only")
        print("7) Full Motion Deterrent Test")
        print("8) Exit")

        choice = input("Select option: ").strip()

        if choice == '1':
            auto_mode()
        elif choice == '2':
            sim_mode()
        elif choice == '3':
            print("\n[TEST] Retract (OPEN)...")
            actuator.retract()
            time.sleep(15)
            actuator.stop()
            time.sleep(2)

            print("\n[TEST] Extend (CLOSE)...")
            actuator.extend()
            time.sleep(15)
            actuator.stop()
        elif choice == '4':
            dir_choice = input("CW or CCW? (cw/ccw): ").strip().lower()
            if dir_choice in ['cw', 'ccw']:
                stepper.power_on()
                time.sleep(0.5)
                stepper.rotate(dir_choice, 5)
                stepper.power_off()
            else:
                print("Invalid direction.")
        elif choice == '5':
            flash_light()
        elif choice == '6':
            play_random_sound()
        elif choice == '7':
            motion_handler()
        elif choice == '8':
            print("[EXIT] Program ended.")
            actuator.cleanup()
            stepper.cleanup()
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
