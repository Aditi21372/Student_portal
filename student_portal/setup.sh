#!/bin/bash

echo "Setting up Student Portal..."

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please update the .env file with your settings"
fi

# Run migrations
echo "Running database migrations..."
python manage.py migrate

echo "Setup complete!"
echo "To start the server, run: python manage.py runserver"
echo "The application will be available at http://127.0.0.1:8000/student_api/api/"
