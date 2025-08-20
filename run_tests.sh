#!/bin/bash

# Exit immediately if a command fails
set -e

# Activate virtual environment
source venv/Scripts/activate  # For Windows Git Bash
# OR use: source venv/bin/activate  # For Linux/Mac

# Run tests
pytest -q

# Capture exit code
if [ $? -eq 0 ]; then
  echo "All tests passed!"
  exit 0
else
  echo "Some tests failed!"
  exit 1
fi
