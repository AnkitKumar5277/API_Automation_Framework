# Payloads-This file contains the diffrent payloads taht w euse for various requests type like the below
# Create Booking
# Update Booking
# Auth
from dotenv import load_dotenv
import os


# Create booking payload
def payload_create_booking():
    payload = {
        "firstname": "Pony",
        "lastname": "Brownie",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


# Update booking payload.Data can be changed during runtime if required

def payload_update_booking():
    payload = {
        "firstname": "Joy",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload


# Update booking -patch request payload
def payload_update_booking_patch():
    payload = {
        "firstname": "James",
        "lastname": "Brown"
    }
    return payload

# Create token payload.username amd password can be repalced  by env variable file(will rewrite later)
def payload_create_token():
    load_dotenv()
    payload = {
        "username": os.getenv("USER_NAME"),
        "password": os.getenv("PASSWORD")
    }
    return payload
