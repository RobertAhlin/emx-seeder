import streamlit as st
import os

# Function to read the contents of README.md
def read_readme(file_path):
    with open(file_path, 'r') as file:
        readme_content = file.read()
    return readme_content

# Function to extract sections from README content
def extract_section(file_content, section_name):
    lines = file_content.split('\n')
    section_content = []
    in_section = False

    for line in lines:
        if line.startswith(section_name):
            in_section = True
            section_content.append(line)
        elif in_section:
            if line.startswith("# ") and line != section_name:
                break
            section_content.append(line)

    return '\n'.join(section_content)

# Function to display README sections in Streamlit
def readme_sections():
    st.write("## About this project.")
    st.write("### Text from ../README.md")

    # Get the parent directory path
    parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    readme_file_path = os.path.join(parent_directory, 'README.md')  # Adjust the file path

    readme_content = read_readme(readme_file_path)

    sections_to_display = [
        "# Business understanding",
        "# Data Preparation",
        "## Business Requirements"
    ]

    for section_name in sections_to_display:
        extracted_section = extract_section(readme_content, section_name)
        st.markdown(extracted_section)