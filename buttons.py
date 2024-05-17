import webbrowser

def open_html_file(file_path):
    webbrowser.open("file://" + file_path, new=2)

def contact_help():
    print("Which help service do you want to contact?")
    print("1. Police")
    print("2. Tow Truck")
    print("3. Hospital")
    print("4. Emergency Contact")
    print("5. False Alarm")

    choice = input("Enter the number corresponding to the service: ")

    if choice == '1':
        html_file_path = "C:/Users/Thrisha%20Kiran/Desktop/police/index.html"
        open_html_file(html_file_path)
    elif choice == '2':
        html_file_path = "C:/Users/Thrisha%20Kiran/Desktop/tow/index.html"
        open_html_file(html_file_path)
    elif choice == '3':
        html_file_path = "C:/Users/Thrisha%20Kiran/Desktop/hospital/index.html"
        open_html_file(html_file_path)
    elif choice == '4':
        html_file_path = "C:/Users/Thrisha%20Kiran/Desktop/emergency/index.html"
        open_html_file(html_file_path)
    elif choice == '5':
        print("Thank you for informing us that it was a false alarm.")
        html_file_path = "C:/Users/Thrisha%20Kiran/Desktop/retrieve/index.html"
        open_html_file(html_file_path)
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

# Example usage:
contact_help()