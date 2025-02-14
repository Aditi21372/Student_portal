API_CONFIG = {
    'base_url': 'http://192.168.3.164:3002/api',  # Updated to match the actual API server
    'timeout': 10,
    'verify_ssl': False,
    'fallback_data': {
        'student_data': {
            'Name': 'Unknown',
            'branch': 'Unknown'
        },
        'course_data': [],
        'ssh_courses': [],
        'discipline_courses': []
    }
}
