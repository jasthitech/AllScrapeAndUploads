import json
import csv
import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

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
    return 'text' in content_type.lower()

def extract_content(response):
    content_type = response.get('content', {}).get('mimeType', '')

    if 'text' in content_type.lower():
        text_content = response.get('content', {}).get('text', '')
        start_index = text_content.find('"story":{"message":{"text":')
        end_index = text_content.find('}', start_index)
        
        if start_index != -1 and end_index != -1:
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


def extract_images_and_videos(response):
    content_type = response.get('content', {}).get('mimeType', '')
    images = []
    videos = []

    if 'text' in content_type.lower():
        text_content = response.get('content', {}).get('text', '')

        # Extract all URLs with various file extensions
        all_urls = re.findall(r"'(https?://[^\s]+\.(jpg|jpeg|png|gif))'", text_content)

        # Retain only the URLs
        image_urls = [url[0] for url in all_urls]

        # Parse HTML content to find images
        soup = BeautifulSoup(text_content, 'html.parser')
        img_tags = soup.find_all('img')

        for img_tag in img_tags:
            src = img_tag.get('src')
            if src:
                image_urls.append(src)

        # Remove duplicates
        image_urls = list(set(image_urls))

        images.extend(image_urls)

    return images, videos

def main():
    # Read the HAR file
    har_file_path = 'F:\\Downloads\\www.facebook.com_Archive [23-09-21 17-18-32].har'

    try:
        with open(har_file_path, 'r', encoding='utf-8') as har_file:
            har_data = json.load(har_file)
    except FileNotFoundError:
        print(f"Error: HAR file not found at {har_file_path}")
        return
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON from {har_file_path}")
        return

    user_content_list = []

    # Iterate through entries
    for entry in har_data.get('log', {}).get('entries', []):
        # Extract user-generated content
        user_content = extract_user_content(entry)

        if user_content:
            # Extract images and videos
            images, videos = extract_images_and_videos(entry['response'])

            # Add user-generated content, images, and videos to the list
            user_content_list.append({
                'url': user_content['url'],
                'text_content': user_content['content'],
                'images': images,
                'videos': videos
            })

    # Specify the location for the CSV file
    csv_file_path = 'F:\\formatedHar\\user_content.csv'

    # Ensure the directory exists, create if not
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

    # Delete and recreate the file if it already exists
    if os.path.exists(csv_file_path):
        os.remove(csv_file_path)
        print(f"Existing file '{csv_file_path}' deleted.")

    # Store user-generated content in a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'text_content', 'images', 'videos']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for user_content in user_content_list:
            writer.writerow(user_content)

    print(f"User-generated content has been saved to: {os.path.abspath(csv_file_path)}")

if __name__ == "__main__":
    main()
#Working well, tuning is required.