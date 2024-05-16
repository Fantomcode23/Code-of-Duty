import sqlite3

def create_vehicle_database():
    conn = sqlite3.connect('vehicle_details.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS vehicles (
                        owner_name TEXT,
                        vehicle_number TEXT PRIMARY KEY,
                        model TEXT,
                        color TEXT,
                        latitude REAL,
                        longitude REAL,
                        emergency_contact_1 TEXT,
                        emergency_contact_2 TEXT
                    )''')
    conn.commit()
    conn.close()
    print("Vehicle database created successfully.")

def create_hospital_database():
    conn = sqlite3.connect('hospital_details.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS hospitals (
                        hospital_name TEXT,
                        hospital_latitude REAL,
                        hospital_longitude REAL,
                        hospital_contact_number TEXT
                    )''')
    conn.commit()
    conn.close()
    print("Hospital database created successfully.")

def create_police_station_database():
    conn = sqlite3.connect('police_station_details.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS police_stations (
                        station_name TEXT,
                        station_latitude REAL,
                        station_longitude REAL,
                        station_contact_number TEXT
                    )''')
    conn.commit()
    conn.close()
    print("Police station database created successfully.")

def create_tow_truck_database():
    conn = sqlite3.connect('tow_truck_details.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tow_trucks (
                        company_name TEXT,
                        company_latitude REAL,
                        company_longitude REAL,
                        company_contact_number TEXT
                    )''')
    conn.commit()
    conn.close()
    print("Tow truck database created successfully.")

create_vehicle_database()
create_hospital_database()
create_police_station_database()
create_tow_truck_database()
