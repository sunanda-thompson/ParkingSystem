# Parking System Management

## Purpose

The Parking System Management program is designed to manage parking information for a school environment. The system allows users to add, update, view, and delete parker information, as well as generate parking tickets. This command-line tool is suitable for managing parking records of teachers, school staff, and visitors.

## Features

- **Add Parker:** Register new parkers with their first name, last name, status (Teacher, School Staff, Visitor), and automatically assign a unique ID and parking lot number.
- **Update Parker:** Modify existing parker information.
- **View Parker Info:** Retrieve and display detailed parker information using their unique ID.
- **Delete Parker:** Remove a parker's record from the system.
- **Parking Ticket:** Generate a parking ticket that includes parker's ID, name, status, lot number, and parking time.

## Technologies Utilized

- **Python:** The program is written entirely in Python, using its core libraries.
- **Linked List:** The program uses a linked list data structure to manage parker records.
- **Time Module:** The `time` module is used to record and display parking time.


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sunanda-thompson/ParkingSystem.git
   ```
2. **Navigate into the directory:**
   ```bash
   cd ParkingSystem
   ```
3. **Run the main script:**
   ```bash
   python parking_system.py
   ```

## Usage
- Follow the on-screen menu to add, update, view, or delete parkers.

## License
This project is licensed under the MIT License.
