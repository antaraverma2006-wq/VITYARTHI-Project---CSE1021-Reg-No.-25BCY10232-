# Railway Reservation System

trains = [
    {"number": 101, "name": "Express A", "seats": 5},
    {"number": 202, "name": "Express B", "seats": 3},
    {"number": 303, "name": "Superfast C", "seats": 2}
]

bookings = []

def show_trains():
    print("\nAvailable Trains:")
    for t in trains:
        print("Train No:", t["number"], "| Name:", t["name"], "| Seats Left:", t["seats"])

def book_ticket():
    show_trains()
    try:
        tno = int(input("\nEnter Train Number to Book: "))
        name = input("Enter Passenger Name: ")
    except:
        print("Invalid input!")
        return

    found = False
    for t in trains:
        if t["number"] == tno:
            found = True
            if t["seats"] > 0:
                t["seats"] -= 1
                bookings.append({"train": t["name"], "name": name})
                print("\nTicket Booked Successfully!")
                print("Passenger:", name)
                print("Train:", t["name"])
            else:
                print("\nSorry, No seats available!")
            break

    if not found:
        print("Train not found!")

def view_bookings():
    print("\nAll Bookings:")
    if len(bookings) == 0:
        print("No bookings yet!")
    else:
        for b in bookings:
            print("Passenger:", b["name"], "| Train:", b["train"])

def main_menu():
    while True:
        print("\n===== TRAIN RESERVATION SYSTEM =====")
        print("1. Show Trains")
        print("2. Book Ticket")
        print("3. View Bookings")
        print("4. Exit")

        try:
            ch = int(input("Enter your choice: "))
        except:
            print("Please enter a valid number!")
            continue
if ch == 1:
            show_trains()
        elif ch == 2:
            book_ticket()
        elif ch == 3:
            view_bookings()
        elif ch == 4:
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice!")

main_menu()
