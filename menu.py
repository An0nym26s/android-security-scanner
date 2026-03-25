import json
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def export_to_json(data, filename='scan_results.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def main_menu():
    results = {"scan_apps": [], "scan_malware": []}
    while True:
        clear_screen()
        print("Main Menu:")
        print("1. Scan Apps")
        print("2. Scan Malware")
        print("3. Export JSON")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Placeholder for scan apps functionality
            print("Scanning apps...")
            results["scan_apps"].append("Example app scan result.")
        
        elif choice == '2':
            results["scan_malware"] += malware_menu()
        
        elif choice == '3':
            export_to_json(results)
            print("Results exported to scan_results.json.")
            input("Press Enter to continue...")
        
        elif choice == '4':
            print("Quitting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

def malware_menu():
    malware_results = []
    while True:
        clear_screen()
        print("Malware Scanning Menu:")
        print("1. BASIQUE")
        print("2. MOYEN")
        print("3. AVANCÉ")
        print("4. Return")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            malware_results.append("BASIQUE scan result.")
        
        elif choice == '2':
            malware_results.append("MOYEN scan result.")
        
        elif choice == '3':
            malware_results.append("AVANCÉ scan result.")
        
        elif choice == '4':
            return malware_results
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()