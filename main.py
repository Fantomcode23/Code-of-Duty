import random
import webbrowser
import pygame
import time

class Car:
    def _init_(self, model, color, name, latitude, longitude):
        self.model = model
        self.color = color
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

class Hospital:
    def _init_(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

class PoliceStation:
    def _init_(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

# Randomly generate car details and coordinates
def generate_car():
    models = ["Toyota", "Honda", "Ford", "Chevrolet", "BMW"]
    colors = ["Red", "Blue", "Green", "Black", "White"]
    names = ["Car A", "Car B", "Car C", "Car D", "Car E"]

    model = random.choice(models)
    color = random.choice(colors)
    name = random.choice(names)
    latitude = random.uniform(12.8, 12.9)  # Latitude range for Bangalore to Mysore highway
    longitude = random.uniform(77.3, 77.5)  # Longitude range for Bangalore to Mysore highway

    return Car(model, color, name, latitude, longitude)

# Randomly generate hospital and police station locations
def generate_locations():
    hospitals = []
    police_stations = []

    for _ in range(5):
        hospital = Hospital("Hospital", random.uniform(12.85, 12.95), random.uniform(77.35, 77.45))
        hospitals.append(hospital)

    for _ in range(2):
        police_station = PoliceStation("Police Station", random.uniform(12.85, 12.95), random.uniform(77.35, 77.45))
        police_stations.append(police_station)

    return hospitals, police_stations

# Send signal to hospitals and police stations
def send_signal(car, hospitals, police_stations):
    print("Sending signal to hospitals and police stations...")
    
    # Play the audio file
    pygame.mixer.init()
    pygame.mixer.music.load("C:\Users\shrey\OneDrive\Desktop\censor-beep-9.mp3")
    pygame.mixer.music.play()
    
    # Wait for at least 5 seconds to ensure the sound plays fully
    time.sleep(5)
    
    for hospital in hospitals:
        print(f"Signal sent to {hospital.name} at coordinates ({hospital.latitude}, {hospital.longitude})")
    for police_station in police_stations:
        print(f"Signal sent to {police_station.name} at coordinates ({police_station.latitude}, {police_station.longitude})")

    # Assume one hospital and one police station respond
    chosen_hospital = random.choice(hospitals)
    chosen_police_station = random.choice(police_stations)

    print(f"\n{chosen_hospital.name} at coordinates ({chosen_hospital.latitude}, {chosen_hospital.longitude}) accepted the signal.")
    print(f"{chosen_police_station.name} at coordinates ({chosen_police_station.latitude}, {chosen_police_station.longitude}) accepted the signal.")

    return chosen_hospital, chosen_police_station

# Open HTML files for hospital, police station, emergency contact, and tow truck service
def open_html_files(file_paths):
    for file_path in file_paths:
        webbrowser.open("file://" + file_path, new=2)

# Main program
def main():
    car = generate_car()
    print(f"Car Details: Model - {car.model}, Color - {car.color}, Name - {car.name}")
    print(f"Car Coordinates: Latitude - {car.latitude}, Longitude - {car.longitude}\n")

    hospitals, police_stations = generate_locations()
    print("Coordinates of Assumed Hospitals:")
    for hospital in hospitals:
        print(f"{hospital.name}: Latitude - {hospital.latitude}, Longitude - {hospital.longitude}")
    print("\nCoordinates of Assumed Police Stations:")
    for police_station in police_stations:
        print(f"{police_station.name}: Latitude - {police_station.latitude}, Longitude - {police_station.longitude}\n")

    chosen_hospital, chosen_police_station = send_signal(car, hospitals, police_stations)

    # Open HTML files for hospital, police station, emergency contact, and tow truck service
    html_files = [
        "C:\Users\shrey\OneDrive\Desktop\police_station_server.html",
        "C:\Users\shrey\OneDrive\Desktop\tow_company_server.html",
        "C:\Users\shrey\OneDrive\Desktop\hospital_server.html",
        "C:\Users\shrey\OneDrive\Desktop\emergency_server.html"
    ]
    open_html_files(html_files)

if _name_ == "_main_":
    main()