import requests
import random
import time

""" Requires running aas-environment @ localhost:8081 """

def generate_random_int(min_value=0, max_value=100):
    """Generate a random integer between min_value and max_value."""
    return random.randint(min_value, max_value)

def escape_number(number):
    return "\""+str(number)+"\""

def update_property_value(url, value):
    """Send a PUT request to update the property value at the given URL."""
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(url, data=escape_number(value), headers=headers)
        response.raise_for_status()
        print(f"Updated value to {value}. Server response: {response.status_code}")
    except requests.RequestException as e:
        print(f"Failed to update value: {e}")

def read_value(url):
    """Send a GET request to read the property value at the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Got the value {response.text}. Server response: {response.status_code}")
        return float(response.text.strip('"'))
    except requests.RequestException as e:
        print(f"Failed to get value: {e}")

def compute_bpm(biegung, dauer):
    return biegung / dauer

def main():
    url_bpm = "http://localhost:8081/submodels/aHR0cHM6Ly9leGFtcGxlLmNvbS9pZHMvc20vNjA1Ml85MDAzXzcwNDJfMzY4Mw/submodel-elements/BPM/$value"
    url_biegung = "http://localhost:8081/submodels/aHR0cHM6Ly9leGFtcGxlLmNvbS9pZHMvc20vMTQ4MV85MDAzXzcwNDJfNzUxMA/submodel-elements/B/$value"
    url_dauer = "http://localhost:8081/submodels/aHR0cHM6Ly9leGFtcGxlLmNvbS9pZHMvc20vMTQ4MV85MDAzXzcwNDJfNzUxMA/submodel-elements/D/$value"

    while True:
        biegung = read_value(url_biegung)
        dauer = read_value(url_dauer)
        bpm = compute_bpm(biegung, dauer)
        update_property_value(url_bpm, bpm)
        time.sleep(5)

if __name__ == "__main__":
    main()
