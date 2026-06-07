from sound_deterrent import play_random_sound

def main():
    print("\n=== SOUND DETERRENT TEST MENU ===")
    print("1. Play Random Sound")
    print("2. Exit")

    while True:
        choice = input("Select an option: ").strip()

        if choice == '1':
            play_random_sound()
        elif choice == '2':
            print("[EXIT] Exiting test.")
            break
        else:
            print("[ERROR] Invalid choice.")

if __name__ == "__main__":
    main()
