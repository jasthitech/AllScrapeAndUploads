import csv
import json
import logging
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the logging level to DEBUG

def extract_user_content(har_entry):
    # Extract request and response information
    request = har_entry.get('request', {})
    response = har_entry.get('response', {})

    # Extract relevant information
    url = request.get('url', '')
    content_type = response.get('content', {}).get('mimeType', '')

    # Check if the response contains user-generated content
    if is_user_generated_content(content_type):
        content = extract_content(response)
        return {
            'url': url,
            'content_type': content_type,
            'content': content
        }
    else:
        return None

def is_user_generated_content(content_type):
    # Implement logic to check if the content is user-generated
    # You might check the content type, URL pattern, or other criteria
    return 'text' in content_type.lower()  # Case-insensitive check for 'text' in content type

def extract_content(response):
    # Implement logic to extract content based on content type
    # Adjust this based on the actual structure of your responses
    content_type = response.get('content', {}).get('mimeType', '')

    if 'text' in content_type.lower():
        text_content = response.get('content', {}).get('text', '')
        
        # Check if the text content has the desired structure
        start_index = text_content.find('"story":{"message":{"text":')
        end_index = text_content.find('}', start_index)
        
        if start_index != -1 and end_index != -1:
            # Extract the content within the specified section
            desired_content = text_content[start_index:end_index + 1]
            return desired_content
        else:
            return 'No matching structure found'
    elif 'image' in content_type:
        # For image content
        return 'image data'  # Replace with your logic to extract image data
    elif 'video' in content_type:
        # For video content
        return 'video data'  # Replace with your logic to extract video data
    else:
        return 'unsupported content type'

def main():
    # Read the HAR file
    har_file_path = 'F:\\Downloads\\www.facebook.com_Archive [23-09-21 17-18-32].har'

    try:
        with open(har_file_path, 'r', encoding='utf-8') as har_file:
            har_data = json.load(har_file)
    except FileNotFoundError:
        logging.error(f"HAR file not found at {har_file_path}")
        return
    except json.JSONDecodeError:
        logging.error(f"Unable to decode JSON from {har_file_path}")
        return

    user_content_list = []

    # Iterate through entries
    for entry in har_data.get('log', {}).get('entries', []):
        # Extract user-generated content
        user_content = extract_user_content(entry)

        if user_content:
            user_content_list.append(user_content)
            logging.debug(f"Identified user-generated content for URL: {user_content['url']}")

    # Specify the location for the CSV file
    csv_file_path = 'F:\\formatedHar\\user_content.csv'

    # Ensure the directory exists, create if not
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

    # Delete and recreate the file if it already exists
    if os.path.exists(csv_file_path):
        os.remove(csv_file_path)
        logging.debug(f"Existing file '{csv_file_path}' deleted.")

    # Store user-generated content in a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'content_type', 'content']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for user_content in user_content_list:
            writer.writerow(user_content)
            logging.debug(f"Row written to CSV: {user_content}")

    logging.info(f"User-generated content has been saved to: {os.path.abspath(csv_file_path)}")

if __name__ == "__main__":
    main()

#This is the working version for the text.