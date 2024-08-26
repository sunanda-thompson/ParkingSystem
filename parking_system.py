import time

class Parker:
    def __init__(self, status, fname, lname, park_time, parker_id, lot_number):
        self.status = status  # Status (1 for Teacher, 2 for School Staff, 3 for Visitor)
        self.fname = fname    # First Name
        self.lname = lname    # Last Name
        self.park_time = park_time  # Parking time (Date and Time)
        self.parker_id = parker_id  # Unique ID for each parker
        self.lot_number = lot_number  # Assigned parking lot number
        self.next = None  # Pointer to the next parker (for linked list, if needed)

class ParkingSystem:
    def __init__(self):
        self.head = None  # Global linked list to store parkers
        self.parker_count = 0  # Counter for the number of parkers

    def menu(self):
        print("****************************************************************")
        print("************************ WELCOME *******************************")
        print("************************    TO   *******************************")
        print("************************ DENBIGH *******************************")
        print("************************   HIGH  *******************************")
        print("************************ PARKING *******************************")
        print("************************  SYSTEM *******************************")
        print("****************************************************************")
        print("\n")
        print("Please select an option from the list below:")
        print("PRESS 1 to add a parker's information")
        print("PRESS 2 to update a parker's file")
        print("PRESS 3 to output a ticket with ID and parking lot number")
        print("PRESS 4 to delete a parker's file")
        print("PRESS 5 to view all parker's information")
        print("PRESS 6 to EXIT the menu")

    def add_parker(self):
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        status = int(input("Please select status (1 for Teacher, 2 for School staff, 3 for Visitor): "))

        self.parker_count += 1
        parker_id = self.parker_count
        lot_number = self.parker_count % 100  # Simple logic for lot number assignment
        park_time = time.time()

        new_parker = Parker(status, fname, lname, park_time, parker_id, lot_number)
        new_parker.next = self.head
        self.head = new_parker

        print(f"Parker added successfully with ID: {parker_id} and Lot Number: {lot_number}")

    def update_parker(self):
        parker_id = int(input("Enter the parker's ID to update: "))
        current = self.head

        while current:
            if current.parker_id == parker_id:
                current.fname = input("Enter new first name: ")
                current.lname = input("Enter new last name: ")
                current.status = int(input("Select new status (1 for Teacher, 2 for School staff, 3 for Visitor): "))

                print("Parker information updated successfully.")
                return
            current = current.next

        print(f"Parker with ID {parker_id} not found.")

    def parking_ticket(self):
        parker_id = int(input("Enter the parker's ID to print the ticket: "))
        current = self.head

        while current:
            if current.parker_id == parker_id:
                print("****************** PARKING TICKET ******************")
                print(f"ID: {current.parker_id}")
                print(f"Name: {current.fname} {current.lname}")
                print(f"Status: {current.status}")
                print(f"Lot Number: {current.lot_number}")
                print(f"Parking Time: {time.ctime(current.park_time)}")
                print("****************************************************")
                return
            current = current.next

        print(f"Parker with ID {parker_id} not found.")

    def delete_parker(self):
        parker_id = int(input("Enter the parker's ID to delete: "))
        current = self.head
        previous = None

        while current:
            if current.parker_id == parker_id:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                print(f"Parker with ID {parker_id} deleted successfully.")
                return
            previous = current
            current = current.next

        print(f"Parker with ID {parker_id} not found.")

    def view_parkers(self):
        if not self.head:
            print("No parkers in the system.")
            return

        current = self.head
        print("****************** PARKER'S INFO ******************")
        while current:
            print(f"ID: {current.parker_id}")
            print(f"Name: {current.fname} {current.lname}")
            print(f"Status: {current.status}")
            print(f"Lot Number: {current.lot_number}")
            print(f"Parking Time: {time.ctime(current.park_time)}")
            print("----------------------------------------------------")
            current = current.next
        print("****************************************************")

    def run(self):
        while True:
            self.menu()
            choice = int(input())

            if choice == 1:
                self.add_parker()
            elif choice == 2:
                self.update_parker()
            elif choice == 3:
                self.parking_ticket()
            elif choice == 4:
                self.delete_parker()
            elif choice == 5:
                self.view_parkers()
            elif choice == 6:
                print("Exiting the program.")
                break
            else:
                print("WRONG CHOICE. Please select a valid option.")

if __name__ == "__main__":
    parking_system = ParkingSystem()
    parking_system.run()
