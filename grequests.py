import subprocess
import os

def download(directory, filename):
    # The base URL of the image files in the GitHub repository
    # Example: base_url = 'https://raw.githubusercontent.com/Denis2054/RAG-Driven-Generative-AI/main/'
    # Actual: https://github.com/GammelNuuk/publiccommons/blob/main/grequests.py
    base_url = 'https://github.com/GammelNuuk/publiccommons/blob/main/'
    
    # Complete URL for the file
    file_url = f"{base_url}{directory}/{filename}"

    # Use curl to download the file, including an Authorization header for the private token
    try:
        # Prepare the curl command with the Authorization header
        curl_command = f'curl -o {filename} {file_url}'

        # Execute the curl command
        subprocess.run(curl_command, check=True, shell=True)
        print(f"Downloaded '{filename}' successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to download '{filename}'. Check the URL, your internet connection, and if the token is correct and has appropriate permissions.")
