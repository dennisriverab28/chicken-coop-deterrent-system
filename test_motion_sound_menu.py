from motion_sound_system import flash_light, play_random_sound, motion_handler

def main_menu():
    while True:
        print("\n======= MOTION DETERRENT TEST MENU =======")
        print("1. Test Flashing Light")
        print("2. Test Random Sound")
        print("3. Run Full System (Motion + Flash + Sound)")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == '1':
            print("[TEST] Flashing light test starting...")
            flash_light()
        elif choice == '2':
            print("[TEST] Playing random sound...")
            play_random_sound()
        elif choice == '3':
            print("[SYSTEM] Running full system. Ctrl+C to stop.")
            motion_handler()
        elif choice == '4':
            print("[EXIT] Test menu closed.")
            break
        else:
            print("[ERROR] Invalid selection. Try again.")

if __name__ == "__main__":
    main_menu()
