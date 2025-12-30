🚗 Automobile Management System (Python + MySQL)

📌 Project Description
The Automobile Management System is a console-based Python application that manages vehicles, customers, sales, and service records using a MySQL database.
It demonstrates how Python can interact with a relational database to perform real-world CRUD operations.

🛠️ Technologies Used

Python 3.12
MySQL Server 8.0
MySQL Connector for Python
VS Code / Python IDLE
MySQL Command Line or MySQL Workbench

📁 Project Structure

AutoMobile_Management/
│

├── AutoMobile_Management.py   # Main Python application

├── database.sql               # SQL script for database setup

├── README.md                  # Project documentation

⚙️ Database Setup

Step 1: Open MySQL
Use MySQL Command Line Client or MySQL Workbench.

Step 2: Run the SQL file
Navigate to the folder containing database.sql and run:

SOURCE database.sql;

This will:
Create the database automobile_management
Create all required tables
Insert sample data

👤 Database User
This project uses a dedicated MySQL user instead of the root user.
Example:
Username: pythonuser
Password: python123

(You may update these credentials in the Python file according to your local MySQL setup.)

🐍 Python Setup
This project requires the MySQL Connector package to allow Python to communicate with the MySQL database.
Run the following command:
pip install mysql-connector-python

▶️ How to Run the Project
python AutoMobile_Management.py


You will see a menu-driven interface to manage vehicles, customers, sales, and services.

✨ Features
Add and view vehicles
Add and view customers
Record vehicle sales
Record service records
Persistent database storage
Menu-driven console application


📚 Learning Outcomes
Python–MySQL integration
Database schema design
SQL scripting using .sql files
Debugging environment and dependency issues
Professional project structuring

🧑‍🎓 Author

Arnab Banerjee
