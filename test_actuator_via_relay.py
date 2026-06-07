import time
from relay_polarity_control import PolarityRelayController

if __name__ == "__main__":
    relay_control = PolarityRelayController()

    try:
        print("\n[TEST] RETRACTING (Coop OPENING)...")
        relay_control.retract()
        time.sleep(15)  # Adjust to actual actuator timing
        relay_control.stop()
        time.sleep(2)

        print("\n[TEST] EXTENDING (Coop CLOSING)...")
        relay_control.extend()
        time.sleep(15)  # Adjust as needed
        relay_control.stop()
        time.sleep(2)
        print("\n[TEST] Test sequence complete.")

    except KeyboardInterrupt:
        print("\n[TEST] Interrupted by user.")
    finally:
        relay_control.cleanup()
