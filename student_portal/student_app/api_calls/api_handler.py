import requests

class APIHandler:
    def __init__(self, base_url):
        self.base_url = base_url

    def call_specific_api(self):
        """Call the specific API and return its output."""
        return self.get("2021372/info")

    def get(self, endpoint, params=None):
        """Make a GET request to the specified endpoint."""
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during GET request: {e}")
            return None

    def post(self, endpoint, data=None):
        """Make a POST request to the specified endpoint."""
        try:
            response = requests.post(f"{self.base_url}/{endpoint}", json=data)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error during POST request: {e}")
            return None
