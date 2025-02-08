from api_handler import APIHandler

def main():
    api_handler = APIHandler("http://localhost:3002/api")
    
    # List of API calls to make
    api_calls = {
        "Graduation Check": api_handler.call_graduation_check_api,
        "Bucket": api_handler.call_bucket_api,
        "Mandatory": api_handler.call_mandatory_api,
        "SSH Major": api_handler.call_ssh_major_api,
        "CW": api_handler.call_cw_api,
        "SG": api_handler.call_sg_api,
        "Thirty Two Credits": api_handler.call_thirty_two_credits_api,
        "IP": api_handler.call_ip_api,
        "Online Courses": api_handler.call_online_courses_api,
        "Two XX Courses": api_handler.call_two_x_courses_api,
        "BTP": api_handler.call_btp_api,
        "Honors": api_handler.call_honors_api,
        "Minors": api_handler.call_minors_api,
        "Eco Major Core": api_handler.call_eco_major_core_api,
        "Incomplete Grade": api_handler.call_incomplete_grade_api,
        "Required Credits": api_handler.call_required_credits_api,
        "Eco Major Elective": api_handler.call_eco_major_elective_api,
    }
    
    # Execute each API call and print the output
    for name, call in api_calls.items():
        print(f"{name} API Output: {call()}")

if __name__ == "__main__":
    main()
