import sqlite3

def print_datasets(database_file):
    try:
        # Connect to the database
        connection = sqlite3.connect(database_file)
        cursor = connection.cursor()

        # Execute a query to select all datasets
        cursor.execute("SELECT * FROM vehicles")

        # Fetch all rows
        vehicles = cursor.fetchall()

        # Print the datasets
        for vehicle in vehicles:
            print(vehicle)

        # Close the connection
        connection.close()
    except sqlite3.Error as error:
        print("Error reading datasets:", error)

# Example usage
if __name__ == "__main__":
    database_file = "vehicle_details.db"
    print_datasets(database_file)

