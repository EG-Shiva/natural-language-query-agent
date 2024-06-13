import os
import requests
from PyPDF2 import PdfReader
import pandas as pd

# Function to download lecture notes
def download_lecture_notes(lecture_urls, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
        for i, url in enumerate(lecture_urls):
            filename = f"lecture_note_{i}.txt"
            file_path = os.path.join(output_dir, filename)
            try:
                # Example code to download files (replace with your download logic)
                response = requests.get(url)
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f"Lecture note downloaded: {file_path}")
            except Exception as e:
                print(f"Failed to download lecture note from {url}: {e}")
    except Exception as e:
        print(f"Failed to create directory {output_dir}: {e}")

# Function to preprocess lecture notes
def preprocess_lecture_notes(input_dir, output_dir):
    try:
        os.makedirs(output_dir, exist_ok=True)
        for i in range(len(os.listdir(input_dir))):
            input_file = os.path.join(input_dir, f"lecture_note_{i}.txt")
            output_file = os.path.join(output_dir, f"preprocessed_note_{i}.txt")
            with open(input_file, 'r') as f:
                lecture_text = f.read()
                # Example preprocessing logic (replace with your actual preprocessing steps)
                preprocessed_text = lecture_text.upper()  # Example: Convert text to uppercase
            with open(output_file, 'w') as f:
                f.write(preprocessed_text)
            print(f"Lecture note preprocessed: {output_file}")
    except Exception as e:
        print(f"Failed to preprocess lecture notes in {input_dir}: {e}")

# Function to download LLM architectures table
def download_llm_architectures_table(url, output_file):
    try:
        response = requests.get(url)
        with open(output_file, 'w') as f:
            f.write(response.text)
        print(f"LLM architectures table downloaded and saved: {output_file}")
    except Exception as e:
        print(f"Failed to download LLM architectures table from {url}: {e}")
