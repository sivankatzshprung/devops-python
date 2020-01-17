# Requests: HTTP for Humans
# http://docs.python-requests.org/en/master/
####
# HTTP in nutshell:
# Two commonly used methods for a request-response between a client and server are: GET and POST.
# GET - Requests data from a specified resource
# POST - Submits data to be processed to a specified resource
# https://www.w3schools.com/tags/ref_httpmethods.asp
# List of HTTP status codes : https://www.w3schools.com/tags/ref_httpmessages.asp
# Let's example with some NASA open API and requests python module
# http://api.open-notify.org example for API , we will see only GET request examples. For POST continue explore by yourself.
import sys
import requests
import json
from datetime import datetime

try:
    # Make a get request to get the latest position of the international space station from the opennotify api.
    response_now = requests.get("http://api.open-notify.org/iss-now.json")
    response_astros = requests.get("http://api.open-notify.org/astros.json")

    print(response_now.status_code)
    print(response_now.text)
    print(response_astros.status_code)
    print(response_astros.text)
    data = response_now.json()
    time_s = datetime.fromtimestamp(int(data['timestamp']))
    location = data['iss_position']
    print(f"Timestamp:\t\t{time_s}")
    print(f"Position:")
    print(f"\tlatitude:\t {location['latitude']}")
    print(f"\tlongitude:\t {location['longitude']}")
    print(50*"=")
    data = response_astros.json()
    print("People in Space Right Now:")
    for name in data['people']:
        print(f"\t{name['name']}")

except Exception as e:
    print(e)