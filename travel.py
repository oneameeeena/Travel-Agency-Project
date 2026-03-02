from datetime import datetime

# -------------------------
# 1. Trip Categories
# -------------------------
trip_categories = ["hotel", "transport", "accommodation", "visit"]

# -------------------------
# 2. Trips
# -------------------------
trips = []

# Function to add a trip
def add_trip(trip_id, city, departure_date_str, price):
    departure_date = datetime.strptime(departure_date_str, "%Y-%m-%d")
    trip = {
        "id": trip_id,
        "city": city,
        "departure_date": departure_date,
        "price": price
    }
    trips.append(trip)
    print(f"Trip to {city} added successfully!")

# Function to remove a trip
def remove_trip(trip_id):
    global trips
    trips = [t for t in trips if t["id"] != trip_id]
    print(f"Trip ID {trip_id} removed successfully!")

# Function to display a trip
def show_trip(trip_id):
    for t in trips:
        if t["id"] == trip_id:
            print({
                "id": t["id"],
                "city": t["city"],
                "departure_date": t["departure_date"].strftime("%Y-%m-%d"),
                "price": t["price"]
            })
            return
    print("Trip not found!")

# Function to show all trips
def display_trips():
    if not trips:
        print("No trips available.")
    for t in trips:
        show_trip(t["id"])

# Function to search trips by price
def search_trip_by_price(price):
    results = [t for t in trips if t["price"] == price]
    if not results:
        print("No trips found with that price.")
    return results

# Function to search trips by city
def search_trip_by_city(city):
    results = [t for t in trips if t["city"].lower() == city.lower()]
    if not results:
        print("No trips found for that city.")
    return results

# Function to search trips by date
def search_trip_by_date(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    results = [t for t in trips if t["departure_date"] == date_obj]
    if not results:
        print("No trips found for that date.")
    return results

# Helper to find a trip by ID
def search_trip_by_id(trip_id):
    for t in trips:
        if t["id"] == trip_id:
            return t
    return None

# -------------------------
# 3. Bookings
# -------------------------
bookings = []

# Function to book a trip for a client
def book_trip(booking_id, trip_id, client_name):
    trip = search_trip_by_id(trip_id)
    if not trip:
        print("Cannot book: Trip does not exist.")
        return
    booking = {
        "id": booking_id,
        "trip": trip,
        "client_name": client_name
    }
    bookings.append(booking)
    print(f"Trip booked for {client_name} successfully!")

# Function to cancel a booking
def cancel_booking(booking_id):
    global bookings
    bookings = [b for b in bookings if b["id"] != booking_id]
    print(f"Booking ID {booking_id} canceled.")

# Function to display a booking's information
def show_booking(booking_id):
    for b in bookings:
        if b["id"] == booking_id:
            print({
                "id": b["id"],
                "client_name": b["client_name"],
                "trip_city": b["trip"]["city"],
                "departure_date": b["trip"]["departure_date"].strftime("%Y-%m-%d"),
                "price": b["trip"]["price"]
            })
            return
    print("Booking not found!")

# Function to calculate the total amount for a booking
def total_amount_booking(booking_id):
    for b in bookings:
        if b["id"] == booking_id:
            total = b["trip"]["price"]
            print(f"Total amount for booking ID {booking_id}: {total}")
            return total
    print("Booking not found!")
    return 0

# Function to display all trips in progress
def display_trips_in_progress():
    today = datetime.today()
    for b in bookings:
        if b["trip"]["departure_date"] >= today:
            show_booking(b["id"])

# Function to calculate total amount of all trips in a given month/year
def total_amount_month(month, year):
    total = 0
    for b in bookings:
        trip_date = b["trip"]["departure_date"]
        if trip_date.month == month and trip_date.year == year:
            total += b["trip"]["price"]
    print(f"Total amount of all trips in {month}/{year}: {total}")
    return total

# -------------------------
# 4. Menu
# -------------------------
def menu():
    while True:
        print("\n--- Travel Agency Trip Management ---")
        print("1. Add Trip")
        print("2. Remove Trip")
        print("3. Show Trip")
        print("4. Display All Trips")
        print("5. Search Trip by Price")
        print("6. Search Trip by City")
        print("7. Search Trip by Date")
        print("8. Book a Trip")
        print("9. Cancel Booking")
        print("10. Show Booking")
        print("11. Total Amount for Booking")
        print("12. Display Trips in Progress")
        print("13. Total Amount of Trips in Month")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tid = input("Trip ID: ")
            city = input("City: ")
            date = input("Departure Date (YYYY-MM-DD): ")
            price = float(input("Price: "))
            add_trip(tid, city, date, price)
        elif choice == "2":
            tid = input("Trip ID to remove: ")
            remove_trip(tid)
        elif choice == "3":
            tid = input("Trip ID to show: ")
            show_trip(tid)
        elif choice == "4":
            display_trips()
        elif choice == "5":
            price = float(input("Price to search: "))
            results = search_trip_by_price(price)
            for t in results:
                show_trip(t["id"])
        elif choice == "6":
            city = input("City to search: ")
            results = search_trip_by_city(city)
            for t in results:
                show_trip(t["id"])
        elif choice == "7":
            date = input("Date to search (YYYY-MM-DD): ")
            results = search_trip_by_date(date)
            for t in results:
                show_trip(t["id"])
        elif choice == "8":
            bid = input("Booking ID: ")
            tid = input("Trip ID: ")
            client = input("Client Name: ")
            book_trip(bid, tid, client)
        elif choice == "9":
            bid = input("Booking ID to cancel: ")
            cancel_booking(bid)
        elif choice == "10":
            bid = input("Booking ID to show: ")
            show_booking(bid)
        elif choice == "11":
            bid = input("Booking ID to calculate total: ")
            total_amount_booking(bid)
        elif choice == "12":
            display_trips_in_progress()
        elif choice == "13":
            month = int(input("Month (1-12): "))
            year = int(input("Year: "))
            total_amount_month(month, year)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
