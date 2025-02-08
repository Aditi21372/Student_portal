import requests

class APIHandler:
    def __init__(self, base_url):
        self.base_url = base_url

    def call_graduation_check_api(self):
        """Call the graduation check API and return its output."""
        return self.get("CSSS/graduation-check")

    def call_bucket_api(self):
        """Call the bucket API and return its output."""
        return self.get("CSSS/bucket")

    def call_mandatory_api(self):
        """Call the mandatory API and return its output."""
        return self.get("CSSS/mandatory")

    def call_ssh_major_api(self):
        """Call the SSH major API and return its output."""
        return self.get("ssh-major")

    def call_cw_api(self):
        """Call the CW API and return its output."""
        return self.get("cw")

    def call_sg_api(self):
        """Call the SG API and return its output."""
        return self.get("sg")

    def call_thirty_two_credits_api(self):
        """Call the thirty-two credits API and return its output."""
        return self.get("CSSS/thirtytwocredits")

    def call_ip_api(self):
        """Call the IP API and return its output."""
        return self.get("ip")

    def call_online_courses_api(self):
        """Call the online courses API and return its output."""
        return self.get("onlinecourses")

    def call_two_x_courses_api(self):
        """Call the two XX courses API and return its output."""
        return self.get("CSSS/twoxxcourses")

    def call_btp_api(self):
        """Call the BTP API and return its output."""
        return self.get("btp")

    def call_honors_api(self):
        """Call the honors API and return its output."""
        return self.get("CSSS/honors")

    def call_minors_api(self):
        """Call the minors API and return its output."""
        return self.get("minors")

    def call_eco_major_core_api(self):
        """Call the eco major core API and return its output."""
        return self.get("eco-major-core")

    def call_incomplete_grade_api(self):
        """Call the incomplete grade API and return its output."""
        return self.get("incompletegrade")

    def call_required_credits_api(self):
        """Call the required credits API and return its output."""
        return self.get("required-credits")

    def call_eco_major_elective_api(self):
        """Call the eco major elective API and return its output."""
        return self.get("eco-major-elective")

    def call_course_info_api(self):
        """Call the course info API and return its output."""
        return self.get("2021393/courseinfo")

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
