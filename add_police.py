import sqlite3

def add_new_station(station_name, station_latitude, station_longitude, station_contact_number):
    conn = sqlite3.connect('police_station_details.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO police_stations 
                          (station_name, station_latitude, station_longitude, station_contact_number) 
                          VALUES (?, ?, ?, ?)''',
                          (station_name, station_latitude, station_longitude, station_contact_number))
        
        conn.commit()
        print("New police station detail added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Police Station already exists.")

    conn.close()

new_station_name = "Shantinagar Police"
new_station_latitude = 29.38493  # Example latitude
new_station_longitude = 34.84983 # Example longitude
new_station_contact_number = "4874552470"

add_new_station(new_station_name, new_station_latitude, new_station_longitude, new_station_contact_number)