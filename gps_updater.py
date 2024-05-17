import sqlite3
import random
import webbrowser
import re

def open_html_file(file_path):
    webbrowser.open("file://" + file_path, new=2)

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

# Generate random coordinates
new_latitude, new_longitude = generate_random_coordinates()

# Update coordinates in the database
vehicle_number = "XYZ456"  
update_vehicle_coordinates(vehicle_number, new_latitude, new_longitude)

# Get updated coordinates
updated_coordinates = get_vehicle_coordinates(vehicle_number)

if updated_coordinates:
    # Read the HTML file
    html_file_path = "C:/Users/shrey/OneDrive/Desktop/index.html"
    with open(html_file_path, 'r') as file:
        html_content = file.read()

    # Replace placeholders in HTML with actual coordinates
    updated_html_content = re.sub(r'{{latitude}}', str(updated_coordinates[0]), html_content)
    updated_html_content = re.sub(r'{{longitude}}', str(updated_coordinates[1]), updated_html_content)

    # Write the modified HTML content to a new file
    modified_html_file_path = "C:/Users/shrey/OneDrive/Desktop/modified_index.html"
    with open(modified_html_file_path, 'w') as file:
        file.write(updated_html_content)

    # Open the modified HTML file
    open_html_file(modified_html_file_path)
else:
    print("Failed to retrieve updated coordinates.")
