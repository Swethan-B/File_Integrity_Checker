# File-Integrity-Checker
A Python-based tool to monitor file integrity by calculating and comparing hash values (e.g., SHA-256). This tool helps detect unauthorized changes, modifications, or deletions of files, ensuring the integrity of critical system or application files.

## Introduction
The File Integrity Checker is a simple but effective Python script that monitors files by calculating their hash values (using SHA-256) and comparing these hashes over time. If any file is modified, added, or deleted, the tool alerts the user about the change. This tool can be used for detecting unauthorized file modifications, ensuring data integrity, and complying with security standards in various environments.

## Installation

Install Python dependencies: Ensure you have Python 3 installed. If not, download and install Python 3.
Then, install any necessary libraries:

    pip install hashlib
    
## Usage
Edit the file_path : Open Checker.py and specify the file you wish to check. Example:

    file_path = '/path/to/file1.txt'

Edit the stored_hash :  Open Checker.py and specify the sha-256 hash value of the original file. Example:

    stored_hash = 'steftwjg324fHSGUAYVHAGDVAHFY'
Run the script: Execute the Python script to start checking the file:

    python3 Checker.py
    
The script will calculate the hash of the specified files and compare them to stored hash values. If any changes are detected, it will display a message.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Preview Image

Here’s a screenshot of the project:

![Screenshot](Screenshot.png.png)
