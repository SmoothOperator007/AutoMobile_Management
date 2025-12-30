import mysql.connector

# Database connection function
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="pythonuser",
        password="python123",
        database="automobile_management"
    )

# Vehicle Management Functions
def add_vehicle():
    make = input("Enter vehicle make: ")
    model = input("Enter vehicle model: ")
    price = float(input("Enter vehicle price: "))
    availability = int(input("Enter vehicle availability: "))

    conn = connect_to_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO vehicles (make, model, price, availability)
    VALUES (%s, %s, %s, %s)
    """
    values = (make, model, price, availability)
    cursor.execute(query, values)

    conn.commit()
    conn.close()
    print("Vehicle added successfully!")

def view_vehicles():
    conn = connect_to_db()
    cursor = conn.cursor()

    query = "SELECT * FROM vehicles"
    cursor.execute(query)
    vehicles = cursor.fetchall()

    print("\nVehicle List:")
    for vehicle in vehicles:
        print(vehicle)

    conn.close()

# Customer Management Functions
def add_customer():
    name = input("Enter customer name: ")
    contact = input("Enter customer contact: ")
    email = input("Enter customer email: ")

    conn = connect_to_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO customers (name, contact, email)
    VALUES (%s, %s, %s)
    """
    values = (name, contact, email)
    cursor.execute(query, values)

    conn.commit()
    conn.close()
    print("Customer added successfully!")

def view_customers():
    conn = connect_to_db()
    cursor = conn.cursor()

    query = "SELECT * FROM customers"
    cursor.execute(query)
    customers = cursor.fetchall()

    print("\nCustomer List:")
    for customer in customers:
        print(customer)

    conn.close()

# Sales Management Functions
def record_sale():
    customer_id = int(input("Enter customer ID: "))
    vehicle_id = int(input("Enter vehicle ID: "))
    amount = float(input("Enter sale amount: "))

    conn = connect_to_db()
    cursor = conn.cursor()

    # Check availability
    query = "SELECT availability FROM vehicles WHERE vehicle_id = %s"
    cursor.execute(query, (vehicle_id,))
    result = cursor.fetchone()

    if result:
        availability = result[0]

        if availability > 0:
            sale_query = """
            INSERT INTO sales (customer_id, vehicle_id, sale_date, amount)
            VALUES (%s, %s, CURDATE(), %s)
            """
            cursor.execute(sale_query, (customer_id, vehicle_id, amount))

            update_query = """
            UPDATE vehicles
            SET availability = availability - 1
            WHERE vehicle_id = %s
            """
            cursor.execute(update_query, (vehicle_id,))

            conn.commit()
            print("Sale recorded successfully!")
        else:
            print("Sorry, the vehicle is not available for sale.")
    else:
        print("Vehicle ID not found.")

    conn.close()

def view_sales():
    conn = connect_to_db()
    cursor = conn.cursor()

    query = "SELECT * FROM sales"
    cursor.execute(query)
    sales = cursor.fetchall()

    print("\nSales Records:")
    for sale in sales:
        print(sale)

    conn.close()

# Service Management Functions
def record_service():
    vehicle_id = int(input("Enter vehicle ID: "))
    service_date = input("Enter service date (YYYY-MM-DD): ")
    details = input("Enter service details: ")

    conn = connect_to_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO services (vehicle_id, service_date, details)
    VALUES (%s, %s, %s)
    """
    values = (vehicle_id, service_date, details)
    cursor.execute(query, values)

    conn.commit()
    conn.close()
    print("Service recorded successfully!")

def view_services():
    conn = connect_to_db()
    cursor = conn.cursor()

    query = "SELECT * FROM services"
    cursor.execute(query)
    services = cursor.fetchall()

    print("\nService Records:")
    for service in services:
        print(service)

    conn.close()

# Main Function
def main():
    while True:
        print("\n--- Automobile Management System ---")
        print("1. Add Vehicle")
        print("2. View Vehicles")
        print("3. Add Customer")
        print("4. View Customers")
        print("5. Record Sale")
        print("6. View Sales")
        print("7. Record Service")
        print("8. View Services")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_vehicle()
        elif choice == 2:
            view_vehicles()
        elif choice == 3:
            add_customer()
        elif choice == 4:
            view_customers()
        elif choice == 5:
            record_sale()
        elif choice == 6:
            view_sales()
        elif choice == 7:
            record_service()
        elif choice == 8:
            view_services()
        elif choice == 9:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
