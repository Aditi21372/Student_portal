import requests
import logging
from typing import Dict, Any
from .config import API_CONFIG
from .rules import RuleManager

logger = logging.getLogger(__name__)
rule_manager = RuleManager()

class APIHandler:
    def __init__(self):
        self.base_url = API_CONFIG['base_url']
        self.timeout = API_CONFIG['timeout']
        self.verify_ssl = API_CONFIG['verify_ssl']
        
    def get_student_data(self, roll_number: str) -> Dict[str, Any]:
        """Get basic student data including branch"""
        url = f"{self.base_url}/{roll_number}/info"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching student data: {str(e)}")
            # Return fallback data when API is unavailable
            fallback = API_CONFIG['fallback_data']['student_data']
            fallback['error'] = 'Failed to fetch student data'
            fallback['details'] = str(e)
            return fallback
        
    def get_course_data(self, roll_number: str, branch: str) -> Dict[str, Any]:
        """Get course data with branch-specific logic"""
        url = f"{self.base_url}/{roll_number}/courseinfo"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching course data: {str(e)}")
            return {
                'error': 'Failed to fetch course data',
                'details': str(e)
            }

    def get_ssh_courses(self, roll_number: str, branch: str) -> Dict[str, Any]:
        """Get SSH courses data with branch-specific logic"""
        if branch == 'CSSS':
            url = f"{self.base_url}/ssh-major"
        else:
            url = f"{self.base_url}/{branch}/ssh"
        
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Adjust response for CSSS branch
            if branch == 'CSSS':
                data['rule'] = '28 credits of SSH courses'
            elif branch == 'CSD':
                data['rule'] = '16 credits of SSH courses'
            else:
                data['rule'] = '12 credits of SSH courses'
                
            return data
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching SSH courses: {str(e)}")
            return {
                'error': 'Failed to fetch SSH courses',
                'details': str(e)
            }

    def get_32_credits(self, roll_number: str, branch: str) -> Dict[str, Any]:
        """Get 32 credits data with branch-specific logic"""
        if branch == 'CSSS':
            url = f"{self.base_url}/{branch}/sixteen-cse-credits"
            rule = '16 Credits of CSE Courses'
        else:
            url = f"{self.base_url}/{branch}/thirtytwo-credits"
            rule = '32 Credits of Discipline Courses'
            
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            data['rule'] = rule
            return data
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching 32 credits: {str(e)}")
            return {
                'error': 'Failed to fetch 32 credits',
                'details': str(e)
            }

    def get_csai_core_courses(self, roll_number: str) -> Dict[str, Any]:
        """Get CSAI core courses data"""
        url = f"{self.base_url}/csai-core"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(12).check_rule(student_data, None)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching CSAI core courses: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_csai_application_courses(self, roll_number: str) -> Dict[str, Any]:
        """Get CSAI application courses data"""
        url = f"{self.base_url}/csai-application"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(14).check_rule(student_data, None)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching CSAI application courses: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_csai_math_courses(self, roll_number: str) -> Dict[str, Any]:
        """Get CSAI math courses data"""
        url = f"{self.base_url}/csai-math"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(15).check_rule(student_data, None)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching CSAI math courses: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_eco_major_core(self, roll_number: str) -> Dict[str, Any]:
        """Get ECO Major core courses"""
        url = f"{self.base_url}/eco-major-core"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(16).check_rule(student_data, None)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching ECO Major core courses: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_eco_major_elective(self, roll_number: str) -> Dict[str, Any]:
        """Get ECO Major elective courses"""
        url = f"{self.base_url}/eco-major-elective"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(17).check_rule(student_data, None)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching ECO Major elective courses: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_btp_credits(self, roll_number: str) -> Dict[str, Any]:
        """Get BTP credits data"""
        url = f"{self.base_url}/btp"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Transform the response to match Angular's expected format
            return {
                'isCompleteBool': data.get('isCompleteBool', False),
                'isCompleteText': data.get('isCompleteText', 'Incomplete'),
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching BTP credits: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_ip_credits(self, roll_number: str) -> Dict[str, Any]:
        """Get IP credits data"""
        url = f"{self.base_url}/ip"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Transform the response to match Angular's expected format
            return {
                'isCompleteBool': data.get('isCompleteBool', False),
                'isCompleteText': data.get('isCompleteText', 'Incomplete'),
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching IP credits: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_online_course_credits(self, roll_number: str) -> Dict[str, Any]:
        """Get online course credits data"""
        url = f"{self.base_url}/onlinecourses"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Transform the response to match Angular's expected format
            return {
                'isCompleteBool': data.get('isCompleteBool', False),
                'isCompleteText': data.get('isCompleteText', 'Incomplete'),
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching online course credits: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_two_xx_courses(self, roll_number: str, branch: str) -> Dict[str, Any]:
        """Get 2XX level courses data"""
        url = f"{self.base_url}/{branch}/twoxxcourses"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Transform the response to match Angular's expected format
            return {
                'isCompleteBool': data.get('isCompleteBool', False),
                'isCompleteText': data.get('isCompleteText', 'Incomplete'),
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching 2XX level courses: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_discipline_courses(self, roll_number: str, branch: str) -> Dict[str, Any]:
        """Get discipline courses data"""
        url = f"{self.base_url}/{branch}/thirtytwocredits"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching discipline courses: {str(e)}")
            return {
                'error': 'Failed to fetch discipline courses',
                'details': str(e)
            }

    def get_mandatory_courses(self, roll_number: str, branch: str) -> Dict[str, Any]:
        """Get mandatory core courses data"""
        url = f"{self.base_url}/{branch}/core"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(0).check_rule(student_data, branch)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'coreCourses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching mandatory courses: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'coreCourses': []
                }
            }

    def get_bucket_courses(self, roll_number: str, branch: str) -> Dict[str, Any]:
        """Get bucket courses data"""
        url = f"{self.base_url}/{branch}/buckets"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(1).check_rule(student_data, branch)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'studentBucketCourses': data.get('data', {}).get('courses', []),
                    'completedBuckets': data.get('data', {}).get('completedBuckets', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching bucket courses: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'studentBucketCourses': [],
                    'completedBuckets': []
                }
            }

    def get_ssh_courses(self, roll_number: str, branch: str) -> Dict[str, Any]:
        """Get SSH courses data"""
        url = f"{self.base_url}/{branch}/ssh"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(2).check_rule(student_data, branch)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching SSH courses: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_cw_courses(self, roll_number: str) -> Dict[str, Any]:
        """Get Community Work courses data"""
        url = f"{self.base_url}/cw"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(3).check_rule(student_data, None)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', []),
                    'button_text': 'View Details'
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching CW courses: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_sg_courses(self, roll_number: str) -> Dict[str, Any]:
        """Get Self Growth courses data"""
        url = f"{self.base_url}/sg"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(4).check_rule(student_data, None)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', []),
                    'button_text': 'View Details'
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching SG courses: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_ip_credits(self, roll_number: str) -> Dict[str, Any]:
        """Get IP credits data"""
        url = f"{self.base_url}/ip"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(6).check_rule(student_data, None)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching IP credits: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_online_course_credits(self, roll_number: str) -> Dict[str, Any]:
        """Get online course credits data"""
        url = f"{self.base_url}/onlinecourses"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(7).check_rule(student_data, None)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching online course credits: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_two_xx_courses(self, roll_number: str, branch: str) -> Dict[str, Any]:
        """Get 2XX level courses data"""
        url = f"{self.base_url}/{branch}/twoxxcourses"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(8).check_rule(student_data, branch)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching 2XX level courses: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_btp_credits(self, roll_number: str) -> Dict[str, Any]:
        """Get BTP credits data"""
        url = f"{self.base_url}/btp"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(9).check_rule(student_data, None)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', [])
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching BTP credits: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_honors(self, roll_number: str, branch: str) -> Dict[str, Any]:
        """Get honors data"""
        url = f"{self.base_url}/{branch}/honors"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            return {
                'isCompleteBool': data.get('isCompleteBool', False),
                'isCompleteText': data.get('isCompleteText', 'Incomplete'),
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', []),
                    'button_text': 'View Details'
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching honors: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': []
            }

    def get_minors(self, roll_number: str) -> Dict[str, Any]:
        """Get minors data"""
        url = f"{self.base_url}/minors"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            minors_data = []
            for minor in data.get('data', []):
                minors_data.append({
                    'stream': minor.get('stream', ''),
                    'totalCredits': minor.get('totalCredits', 0),
                    'isCompleteText': minor.get('isCompleteText', 'Incomplete'),
                    'courses': minor.get('courses', [])
                })
            
            return {
                'isCompleteBool': data.get('isCompleteBool', False),
                'isCompleteText': data.get('isCompleteText', 'Incomplete'),
                'data': {
                    'minors': minors_data,
                    'button_text': 'View Details'
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching minors: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': []
            }

    def get_eco_major_core(self, roll_number: str) -> Dict[str, Any]:
        """Get ECO Major core courses"""
        url = f"{self.base_url}/eco-major-core"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching ECO Major core courses: {str(e)}")
            return {
                'error': 'Failed to fetch ECO Major core courses',
                'details': str(e)
            }

    def get_eco_major_elective(self, roll_number: str) -> Dict[str, Any]:
        """Get ECO Major elective courses"""
        url = f"{self.base_url}/eco-major-elective"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching ECO Major elective courses: {str(e)}")
            return {
                'error': 'Failed to fetch ECO Major elective courses',
                'details': str(e)
            }

    def get_incomplete_grades(self, roll_number: str) -> Dict[str, Any]:
        """Get incomplete grades data"""
        url = f"{self.base_url}/incomplete-grades"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(10).check_rule(student_data, None)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'courses': data.get('data', {}).get('courses', []),
                    'button_text': 'View Details'
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching incomplete grades: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': {
                    'totalCredits': 0,
                    'courses': []
                }
            }

    def get_total_credits(self, roll_number: str) -> Dict[str, Any]:
        """Get total credits data"""
        url = f"{self.base_url}/total-credits"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()
            
            # Get student data and process with rule system
            student_data = self.get_student_data(roll_number)
            rule_result = rule_manager.get_rule(11).check_rule(student_data, None)
            
            # Merge API data with rule processing
            return {
                'isCompleteBool': rule_result['isCompleteBool'],
                'isCompleteText': rule_result['isCompleteText'],
                'data': {
                    'totalCredits': data.get('data', {}).get('totalCredits', 0),
                    'button_text': 'No Action'
                }
            }
        except (requests.exceptions.RequestException, ValueError) as e:
            logger.error(f"Error fetching total credits: {str(e)}")
            return {
                'isCompleteBool': False,
                'isCompleteText': 'Error',
                'data': 0
            }
