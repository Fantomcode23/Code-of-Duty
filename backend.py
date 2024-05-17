from flask import Flask, request, jsonify
import random
import math 
import webbrowser

def open_html_file(file_path):
    webbrowser.open("file://" + file_path, new=2)

app = Flask(__name__)

# Database connections
hospital_details_db = {}  # hospital database
police_station_details_db = {}  # police station database
vehicle_details_db = {}  # vehicle database

# Function to generate random GPS coordinates
def generate_gps_coordinates():
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)
    return lat, lon

# Function to calculate distance between two GPS coordinates
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # radius of the earth in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

# Function to send notification to nearest hospitals
def send_notification_to_hospitals(lat, lon, vehicle_data):
    nearest_hospitals = []
    for hospital_id, hospital_data in hospital_db.items():
        hospital_latitude, hospital_longitude = hospital_data['latitude'], hospital_data['longitude']
        distance = calculate_distance(lat, lon, hospital_latitude, hospital_longitude)
        if distance < 50:  # 5 km radius
            nearest_hospitals.append(hospital_name)
    if nearest_hospitals:
        notification_data = {'vehicle_data': vehicle_data, 'hospital_ids': nearest_hospitals}
        html_file_path = "file:///C:/Users/shrey/OneDrive/Desktop/index.html"
        open_html_file(html_file_path)
        print("Notification sent to hospitals:", notification_data)

# Function to send notification to nearest police stations
def send_notification_to_police_stations(lat, lon, vehicle_data):
    nearest_police_stations = []
    for police_id, police_data in police_db.items():
        police_lat, police_lon = police_data['latitude'], police_data['longitude']
        distance = calculate_distance(lat, lon, police_lat, police_lon)
        if distance < 5:  # 5 km radius
            nearest_police_stations.append(police_id)
    if nearest_police_stations:
        notification_data = {'vehicle_data': vehicle_data, 'police_ids': nearest_police_stations}
        # Send notification to police stations using a notification service (e.g. Twilio, Nexmo)
        print("Notification sent to police stations:", notification_data)

# API endpoint to simulate sensor signal and generate GPS coordinates
@app.route('/simulate_sensor_signal', methods=['POST'])
def simulate_sensor_signal():
    vehicle_data = request.get_json()
    lat, lon = generate_gps_coordinates()
    vehicle_db[vehicle_data['vehicle_number']] = {'owner_name': vehicle_data['owner_name'], 'model': vehicle_data['model'], 'color': vehicle_data['color'], 'latitude': lat, 'longitude': lon, 'emergency_contact_1': vehicle_data['emergency_contact_1'], 'emergency_contact_2': vehicle_data['emergency_contact_2']}
    send_notification_to_hospitals(lat, lon, vehicle_data)
    send_notification_to_police_stations(lat, lon, vehicle_data)
    return jsonify({'message': 'Sensor signal simulated successfully'})

if __name__ == '_main_':
    app.run(debug=True)