import os
import json
import subprocess
import sys

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to scan installed applications
def scan_apps():
    try:
        apps = subprocess.check_output(['adb', 'shell', 'pm', 'list', 'packages']).decode('utf-8')
        return apps.split('\n')
    except subprocess.CalledProcessError as e:
        print("Error scanning apps:", e)
        return []

# Function to export scan results to JSON file
def export_json(results):
    timestamp = "{}".format("2026-03-25 17:00:33") # Current date and time
    filename = f'scan_results_{timestamp}.json'
    try:
        with open(filename, 'w') as f:
            json.dump(results, f, indent=4)
        print(f'Exported results to {filename}')
    except Exception as e:
        print("Error exporting JSON:", e)

# Main Menu
def main_menu():
    while True:
        clear_screen()
        print('\033[1;32;40m=========== Main Menu ===========\033[0m')
        print('1. Scan Apps')
        print('2. Malware Menu')
        print('3. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            apps = scan_apps()
            print('\033[1;34;40mInstalled Apps:\033[0m')
            for app in apps:
                print(app)
            export_json(apps)
            input('Press Enter to continue...')

        elif choice == '2':
            malware_menu()

        elif choice == '3':
            sys.exit(0)

        else:
            print('\033[1;31;40mInvalid choice, please try again.\033[0m')
            input('Press Enter to continue...')

# Malware Menu
def malware_menu():
    while True:
        clear_screen()
        print('\033[1;33;40m=========== Malware Menu ===========\033[0m')
        print('1. BASIQUE')
        print('2. MOYEN')
        print('3. AVANCÉ')
        print('4. Back to Main Menu')
        choice = input('Enter your choice: ')

        if choice == '1':
            print('You selected BASIQUE option')
            input('Press Enter to continue...')

        elif choice == '2':
            print('You selected MOYEN option')
            input('Press Enter to continue...')

        elif choice == '3':
            print('You selected AVANCÉ option')
            input('Press Enter to continue...')

        elif choice == '4':
            break

        else:
            print('\033[1;31;40mInvalid choice, please try again.\033[0m')
            input('Press Enter to continue...')

if __name__ == '__main__':
    main_menu()