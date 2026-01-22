tickets = []

def book_ticket():
    passenger = input("Enter passenger name: ")
    route = input("Enter travel route: ")
    tickets.append({
        "passenger": passenger,
        "route": route
    })
    print("Ticket booked successfully")

def view_tickets():
    if not tickets:
        print("No tickets booked")
    else:
        for t in tickets:
            print("Passenger:", t["passenger"], "| Route:", t["route"])

def main():
    while True:
        print("1. Book Ticket")
        print("2. View Tickets")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            book_ticket()
        elif choice == "2":
            view_tickets()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
