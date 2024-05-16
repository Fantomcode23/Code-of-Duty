import sqlite3

def add_new_vehicle(owner_name, vehicle_number, model, color, latitude, longitude, emergency_contact_1, emergency_contact_2):
    conn = sqlite3.connect('vehicle_details.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO vehicles 
                          (owner_name, vehicle_number, model, color, latitude, longitude, emergency_contact_1, emergency_contact_2) 
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                          (owner_name, vehicle_number, model, color, latitude, longitude, emergency_contact_1, emergency_contact_2))
        
        conn.commit()
        print("New vehicle detail added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Vehicle number already exists.")

    conn.close()

new_owner_name = "Gojo"
new_vehicle_number = "XYZ456"
new_model = "Renault Kwid"
new_color = "Yellow"
new_latitude = 00.00000  # Example latitude
new_longitude = 00.0000  # Example longitude
new_emergency_contact_1 = "99999944444"
new_emergency_contact_2 = "2002002002"

add_new_vehicle(new_owner_name, new_vehicle_number, new_model, new_color, new_latitude, new_longitude, new_emergency_contact_1, new_emergency_contact_2)
