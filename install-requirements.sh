#!/usr/bin/env bash

# Read the version number from the .python-version file
PYTHON_VERSION=$(cat .python-version)

# Check if PYTHON_VERSION is not empty
if [ -z "$PYTHON_VERSION" ]; then
    echo "Error: .python-version is empty. Please specify a Python version."
    exit 1
fi

# Remove the existing Python version directory in pyenv, if it exists
# -r: recursive, -f: force (no error if it doesn't exist)
rm -rf ~/.pyenv/versions/$PYTHON_VERSION*

# Check for the removal's success
if [ $? -ne 0 ]; then
    echo "Error removing existing Python version from pyenv."
    exit 1
fi

# Install the Python version specified in .python-version using pyenv
# This command assumes that .python-version contains the version to install
pyenv install

# Check for pyenv install's success
if [ $? -ne 0 ]; then
    echo "Pyenv failed to install Python."
    exit 1
fi

# Upgrade pip to the latest version
pip install --upgrade pip

# Check for pip upgrade's success
if [ $? -ne 0 ]; then
    echo "Failed to upgrade pip."
    exit 1
fi

# Install the required packages from requirements.txt
pip install -r requirements.txt

# Check for requirements installation's success
if [ $? -ne 0 ]; then
    echo "Failed to install requirements."
    exit 1
fi

# Indicate successful completion
echo "Setup completed successfully."
