# Student Portal

A Django-based student portal for accessing various student-related APIs.

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd student_portal
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file with your settings
# Make sure to update:
# - API_BASE_URL (default: http://localhost:3002/api)
# - DEBUG (set to True for development)
# - ALLOWED_HOSTS (add localhost and 127.0.0.1 for development)
```

5. Run database migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

The application will be available at http://127.0.0.1:8000/student_api/api/

## API Endpoints

The portal provides access to the following student information APIs:
- Graduation Check
- Bucket Information
- Mandatory Requirements
- SSH Major
- Course Work
- Student Grades
- 32 Credits Check
- IP Information
- Online Courses
- Two XX Courses
- BTP Information
- Honors
- Minors
- Economics Major Core
- Incomplete Grades
- Required Credits
- Economics Major Electives

## Development Notes

- Make sure the API server is running at the configured API_BASE_URL
- For development, set DEBUG=True in .env
- Add any new dependencies to requirements.txt
