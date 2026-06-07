from relay_stepper_control import RelayStepperController
import time

def main():
    stepper = RelayStepperController()

    try:
        while True:
            print("\n=== TEST MENU ===")
            print("1) Rotate Clockwise")
            print("2) Rotate Counterclockwise")
            print("3) Exit")
            choice = input("Select an option: ").strip()

            if choice == "1":
                stepper.power_on()
                time.sleep(0.5)
                stepper.rotate("cw", 5)
                stepper.power_off()

            elif choice == "2":
                stepper.power_on()
                time.sleep(0.5)
                stepper.rotate("ccw", 5)
                stepper.power_off()

            elif choice == "3":
                break
            else:
                print("Invalid option.")

    except KeyboardInterrupt:
        print("\n[EXIT] Interrupted by user.")
    finally:
        stepper.cleanup()

if __name__ == "__main__":
    main()
