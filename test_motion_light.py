from motion_light_controller import monitor_motion

if __name__ == "__main__":
    print("\n========== Motion + Light Test ==========")
    print("System will now detect motion and flash the light 5 times.\n")

    try:
        monitor_motion()
    except KeyboardInterrupt:
        print("\n[EXIT] Program terminated by user.")
