import requests
import time

# Create a persistent session, cause the site also does that thing.
session = requests.Session()

# URL GOES HERE!
BASE_URL = "https://hfw.vitap.ac.in:8090/login.xml"
# USERNAME GOES HERE!
USERNAME = "" 
# PASSWORD GOES HERE!
PASSWORD = ""

def login():
    payload = {
        "mode": "191",  # Login mode
        "username": USERNAME,
        "password": PASSWORD,
        "producttype": 0
    }

    response = session.post(BASE_URL, data=payload, verify=False)
    print("Login Status Code:", response.status_code)
    print("Login Response:\n", response.text)

def logout():
    payload = {
        "mode": "193",  # Logout mode
        "username": USERNAME,
        "producttype": 0
    }

    response = session.post(BASE_URL, data=payload, verify=False)
    print("Logout Status Code:", response.status_code)
    print("Logout Response:\n", response.text)


# Simple demo, will work on terminal thing later on
task = input("Enter 1 to login, 0 to logout: ").strip()
if task == "1":
    login()
elif task == "0":
    logout()
else:
    print("Invalid input. Enter 1 for login or 0 for logout.")