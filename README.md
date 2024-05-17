Vehicle Details Management System
This repository contains Python scripts and HTML files for managing vehicle details, including registration, updating coordinates, and more.

Features:
Add New Vehicle: Add details of a new vehicle to the database.
Update Vehicle Coordinates: Update the coordinates (latitude and longitude) of a vehicle.
Add new Hospital : Adds a new Hospital along with its details to the database.
Add new Police Station : Adds a new Police Station along with its details to the database.
Add new Tow Company: Adds a new Tow Company along with its details to the database.
Generate Random Coordinates: Generate random coordinates for a vehicle for current simulation and sends it to the hospital, police station and the emergency contact receivers.
As the Hospital, Police Station and Emergency Contact endpoint APIs need Proxy servers to be connected, we have created sample pages of how the notification on the Hospital device is going to be.
SQLite Database Integration: Utilizes SQLite database for storing vehicle details.
Files:
create_db.py : Creates the various databases required
add_hospital : Adds the new Hospital details
add_police_station : Adds a new police station details
add_tow_truck: Adds the new tow truck details
add_user: adds the new user details
backend.py: A temporary backend framework created to display the modus operandi. It cannot be implemented as we require a proper Proxy Messaging Service
gps_updater.py : Generates a randomg gps coordinate and simulates sample web pages which are created to represent the format of notification the emergency services are goig to receive.
Usage:
Ensure you have Python installed.
Install the required dependencies using pip install sqlite3.
Run the Python scripts to interact with the vehicle database.
Contributors:
Thrisha kiran (@thrishaaa)
Shreya hegde (@hshreya1310)
vamshika c(@vamshika-0210)
Kalyan k(@kkn2004)
S.H.I.E.L.D Website
This repository contains HTML and CSS files for the S.H.I.E.L.D website, a fictional organization for managing emergency services.

Features:
User Interface: Provides a user-friendly interface for accessing S.H.I.E.L.D services.
Responsive Design: Designed to be responsive and accessible across various devices.
Files:
index.html: HTML file for the main page of the S.H.I.E.L.D website.
styles.css: CSS file for styling the S.H.I.E.L.D website.
Usage:
Open index.html in a web browser to view the S.H.I.E.L.D website.
Contributors:
Thrisha kiran (@thrishaaa)
Shreya hegde (@hshreya1310)
vamshika c(@vamshika-0210)
Kalyan k(@kkn2004)
User Registration System
This repository contains HTML files and JavaScript code for user registration on the S.H.I.E.L.D website.

Features:
New User Registration: Allows new users to register on the S.H.I.E.L.D website.
Password Matching: Ensures that the entered password matches the re-entered password.
Files:
register.html: HTML file for the user registration page.
script.js: JavaScript file containing functions for user registration.
Usage:
Open register.html in a web browser to access the user registration page.
Fill in the required details and submit the form to register as a new user.
Contributors:
Thrisha kiran (@thrishaaa)
Shreya hegde (@hshreya1310)
vamshika c(@vamshika-0210)
Kalyan k(@kkn2004)
