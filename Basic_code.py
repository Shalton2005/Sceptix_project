import datetime
import time
medicine_tracker = {}
water_tracker = {}
sleep_tracker = {}

def display_menu():
    print("\nMulti-purpose Tracking System Menu:")
    print("1. Medicine Tracker")
    print("2. Drinking Water Tracker")
    print("3. Sleep Tracker")
    print("4. View Previous Data")
    print("5. Exit")

def medicine_tracking():
    medicine_name = input("Enter the name of the medicine: ")
    medicine_dosage = input("Enter the dosage: ")
    medicine_tracker[medicine_name] = medicine_dosage
    print("Medicine tracked successfully!")

def water_tracking():
    water_amount = input("Enter the amount of water consumed (in ml): ")
    water_tracker.setdefault("Total Water Consumed", 0)
    water_tracker["Total Water Consumed"] += int(water_amount)
    print("Water intake tracked successfully!")

def sleep_tracking():
    sleep_duration = input("Enter the duration of sleep (in hours): ")
    sleep_date = input("Enter the date of sleep (MM/DD/YYYY): ")
    sleep_tracker[sleep_date] = sleep_duration
    print("Sleep tracked successfully!")

def view_previous_data():
    print("\nPrevious Data:")
    print("Medicine Tracker:", medicine_tracker)
    print("Water Tracker:", water_tracker)
    print("Sleep Tracker:", sleep_tracker)

def set_reminder(task_time):
    current_time = datetime.datetime.now().time()
    task_datetime = datetime.datetime.strptime(task_time, '%H:%M').time()

    thirty_minutes = datetime.timedelta(minutes=30)
    reminder_time = (datetime.datetime.combine(datetime.date.today(), task_datetime) - thirty_minutes).time()

    while current_time < reminder_time:
        time.sleep(60)  # Check every minute
        current_time = datetime.datetime.now().time()

    print("\nReminder: Time to perform the task!")

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        medicine_tracking()
    elif choice == '2':
        water_tracking()
    elif choice == '3':
        sleep_tracking()
    elif choice == '4':
        view_previous_data()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

    # Ask for reminder if applicable
    if choice in ['1', '2', '3']:
        task_time = input("Enter the time to perform the task (HH:MM): ")
        set_reminder(task_time)
