import sqlite3

def add_new_hospital(hospital_name, hospital_latitude, hospital_longitude, hospital_contact_number):
    conn = sqlite3.connect('hospital_details.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO hospitals 
                          (hospital_name, hospital_latitude, hospital_longitude, hospital_contact_number) 
                          VALUES (?, ?, ?, ?)''',
                          (hospital_name, hospital_latitude, hospital_longitude, hospital_contact_number))
        
        conn.commit()
        print("New hospital detail added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Hospital already exists.")

    conn.close()

new_hospital_name = "Apollo Hospitals"
new_hospital_latitude = 76.7868  # Example latitude
new_hospital_longitude = 78.5768  # Example longitude
new_hospital_contact_number = "9746787867"

add_new_hospital(new_hospital_name, new_hospital_latitude, new_hospital_longitude, new_hospital_contact_number)
