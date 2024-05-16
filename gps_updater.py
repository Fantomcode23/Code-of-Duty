import sqlite3
import random

def generate_random_coordinates():
    latitude = round(random.uniform(-90, 90), 6)
    longitude = round(random.uniform(-180, 180), 6)
    return latitude, longitude

def update_vehicle_coordinates(vehicle_number, latitude, longitude):
    conn = sqlite3.connect('vehicle_details.db')
    cursor = conn.cursor()

    cursor.execute('''UPDATE vehicles 
                      SET latitude = ?, longitude = ?
                      WHERE vehicle_number = ?''', (latitude, longitude, vehicle_number))

    conn.commit()
    conn.close()

def get_vehicle_coordinates(vehicle_number):
    conn = sqlite3.connect('vehicle_details.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT latitude, longitude 
                      FROM vehicles 
                      WHERE vehicle_number = ?''', (vehicle_number,))
    coordinates = cursor.fetchone()

    conn.close()

    return coordinates

new_latitude, new_longitude = generate_random_coordinates()

vehicle_number = "XYZ456"  
update_vehicle_coordinates(vehicle_number, new_latitude, new_longitude)

updated_coordinates = get_vehicle_coordinates(vehicle_number)
if updated_coordinates:
    print("Updated Vehicle Coordinates:", updated_coordinates)
else:
    print("Failed to retrieve updated coordinates.")
