import time
from datetime import datetime

def display_banner():
    print("WELCOME TO PARKING MANAGEMENT")
    time.sleep(1)

# Initialize global variables
vehicle_data = {
    "number": [],
    "type": [],
    "name": [],
    "owner": [],
    "date": [],
    "time": []
}
parking_space = {"bikes": 100, "cars": 250, "bicycles": 78}

# Functions for operations
def vehicle_entry():
    print("\n--- Add Vehicle Entry ---")
    while True:
        v_no = input("Enter vehicle number (XXXX-XX-XXXX): ").upper()
        if not v_no or len(v_no) != 12:
            print("Invalid vehicle number. Please try again.")
            continue
        if v_no in vehicle_data["number"]:
            print("Vehicle number already exists. Try again.")
            continue
        vehicle_data["number"].append(v_no)
        break

    while True:
        v_type = input("Enter vehicle type (Bicycle=A, Bike=B, Car=C): ").lower()
        if v_type == "a":
            vehicle_data["type"].append("Bicycle")
            parking_space["bicycles"] -= 1
            break
        elif v_type == "b":
            vehicle_data["type"].append("Bike")
            parking_space["bikes"] -= 1
            break
        elif v_type == "c":
            vehicle_data["type"].append("Car")
            parking_space["cars"] -= 1
            break
        else:
            print("Invalid type. Try again.")

    v_name = input("Enter vehicle name: ") or "Unknown"
    vehicle_data["name"].append(v_name)

    o_name = input("Enter owner name: ") or "Unknown"
    vehicle_data["owner"].append(o_name)

    current_date = datetime.now().strftime("%d-%m-%Y")
    current_time = datetime.now().strftime("%H:%M:%S")
    vehicle_data["date"].append(current_date)
    vehicle_data["time"].append(current_time)

    print("Vehicle entry added successfully!")

def remove_entry():
    print("\n--- Remove Vehicle Entry ---")
    v_no = input("Enter vehicle number to remove (XXXX-XX-XXXX): ").upper()
    if v_no in vehicle_data["number"]:
        i = vehicle_data["number"].index(v_no)
        for key in vehicle_data.keys():
            vehicle_data[key].pop(i)
        print("Vehicle entry removed successfully!")
    else:
        print("Vehicle not found.")

def view_parked_vehicles():
    print("S.No\tNumber\tType\tName\tOwner\tDate\tTime")
    for i in range(len(vehicle_data['number'])):
        print(f"{i+1}\t{vehicle_data['number'][i]}\t{vehicle_data['type'][i]}\t{vehicle_data['name'][i]}\t{vehicle_data['owner'][i]}\t{vehicle_data['date'][i]}\t{vehicle_data['time'][i]}")

def view_parking_space():
    print("\n--- Parking Space Availability ---")
    for k, v in parking_space.items():
        print(f"{k.capitalize()} spaces left: {v}")
     
def display_menu():
    print("\n--- Main Menu ---")
    print("1. Vehicle Entry")
    print("2. Remove Entry")
    print("3. View Parked Vehicles")
    print("4. View Parking Space")
    print("5. Exit")

def main():
    display_banner()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            vehicle_entry()
        elif choice == "2":
            remove_entry()
        elif choice == "3":
            view_parked_vehicles()
        elif choice == "4":
            view_parking_space()
        elif choice == "5":
            print("Thank you for using the Parking Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()