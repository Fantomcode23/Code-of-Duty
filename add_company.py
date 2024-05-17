import sqlite3

def add_new_company(company_name, company_latitude, company_longitude, company_contact_number):
    conn = sqlite3.connect('tow_truck_details.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO tow_trucks 
                          (company_name, company_latitude, company_longitude, company_contact_number) 
                          VALUES (?, ?, ?, ?)''',
                          (company_name, company_latitude, company_longitude, company_contact_number))
        
        conn.commit()
        print("New tow company detail added successfully.")
    except sqlite3.IntegrityError:
        print("Error: Tow Company already exists.")

    conn.close()

new_company_name = "Powai Tow"
new_company_latitude = 85.3983  # Example latitude
new_company_longitude = 38.5883 # Example longitude
new_company_contact_number = "9483794498"

add_new_company(new_company_name, new_company_latitude, new_company_longitude, new_company_contact_number)
