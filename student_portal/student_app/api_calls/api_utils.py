from .api_handler import APIHandler

def run_api_calls(roll_number=None):
    """Consolidated function to run all API calls"""
    api_handler = APIHandler()
    
    outputs = {
        "graduation_check": api_handler.call_graduation_check_api(),
        "bucket": api_handler.call_bucket_api(),
        "mandatory": api_handler.call_mandatory_api(),
        "ssh_major": api_handler.call_ssh_major_api(),
        "cw": api_handler.call_cw_api(),
        "sg": api_handler.call_sg_api(),
        "thirty_two_credits": api_handler.call_thirty_two_credits_api(),
        "ip": api_handler.call_ip_api(),
        "online_courses": api_handler.call_online_courses_api(),
        "two_x_courses": api_handler.call_two_x_courses_api(),
        "btp": api_handler.call_btp_api(),
        "honors": api_handler.call_honors_api(),
        "minors": api_handler.call_minors_api(),
        "eco_major_core": api_handler.call_eco_major_core_api(),
        "incomplete_grade": api_handler.call_incomplete_grade_api(),
        "required_credits": api_handler.call_required_credits_api(),
        "eco_major_elective": api_handler.call_eco_major_elective_api(),
    }
    return outputs

def get_course_info():
    """Get course information"""
    api_handler = APIHandler()
    return api_handler.call_course_info_api()

def get_specific_info():
    """Get specific student information"""
    api_handler = APIHandler()
    return api_handler.call_specific_api()
