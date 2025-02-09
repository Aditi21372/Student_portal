import os
from dotenv import load_dotenv

load_dotenv()

API_CONFIG = {
    'base_url': os.getenv('API_BASE_URL', 'http://localhost:3002/api'),
    'timeout': 30,
    'verify_ssl': True
}
