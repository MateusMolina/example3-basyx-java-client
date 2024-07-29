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

def main():
    url = "http://localhost:8081/submodels/aHR0cHM6Ly9odHctYmVybGluLmRlL2lkcy9zbS9kZW1vc3VibW9kZWx2Mw/submodel-elements/IntProp/$value"
    while True:
        new_value = generate_random_int()
        update_property_value(url, new_value)
        time.sleep(5)

if __name__ == "__main__":
    main()
