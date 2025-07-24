import requests
import json

# my base home path, pls don't heck me

# imma import usrname, pwd and url all from a json file ig. I'll just put the json in home directory.

def login():
    session = requests.Session()
    
    credentials = read_creds()
    username = credentials['username']
    password = credentials['password']
    url = credentials['url']

    payload = {
        "mode": "191",  # Login mode
        "username": username,
        "password": password,
        "producttype": 0
    }

    response = session.post(url, data=payload, verify=False)
    print("Login Status Code:", response.status_code)
    print("Login Response:\n", response.text)

def logout():
    session = requests.Session()

    credentials = read_creds()
    username = credentials['username']
    url = credentials['url']

    payload = {
        "mode": "193",  # Logout mode
        "username": username,
        "producttype": 0
    }

    response = session.post(url, data=payload, verify=False)
    print("Logout Status Code:", response.status_code)
    print("Logout Response:\n", response.text)


def read_creds():
    path = "/home/kushal/hostel_wifi.json"
    with open(path, 'r') as json_file:
        credentials = json.load(json_file)
    return credentials
