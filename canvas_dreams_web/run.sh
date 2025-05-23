#!/bin/bash

# Activate virtual environment if it exists
if [ -d "../venv" ]; then
    source ../venv/bin/activate
fi

# Install requirements
pip install -r requirements.txt

# Run the Flask server
python server.py
