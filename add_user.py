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

new_owner_name = "Code of Duty"
new_vehicle_number = "XYZ456"
new_model = "Toyota Corolla"
new_color = "Blue"
new_latitude = 40.7128  # Example latitude
new_longitude = -74.0060  # Example longitude
new_emergency_contact_1 = "1234567890"
new_emergency_contact_2 = "0987654321"

add_new_vehicle(new_owner_name, new_vehicle_number, new_model, new_color, new_latitude, new_longitude, new_emergency_contact_1, new_emergency_contact_2)
