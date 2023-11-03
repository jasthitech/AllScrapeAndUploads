import json
import base64
import os
import csv
import re
from urllib.parse import urlparse
import urllib.parse

import urllib3

def extract_text_content(har_entry):
    # Extract request and response information
    request = har_entry.get('request', {})
    response = har_entry.get('response', {})
    desired_content = ''

    # Extract relevant information
    url = har_entry.get('url', '')
    content_type = har_entry.get('content', {}).get('mimeType', '')
    #*************************************************************
    if 'text' in content_type.lower():
    #if text_content:
        text_content = har_entry.get('content', {}).get('text', '')
        start_index = text_content.find('"story":{"message":{"text":')
        end_index = text_content.find('}', start_index)
        
        if start_index != -1 and end_index != -1:
            dsrd_content = desired_content.join(text_content[start_index:end_index + 1])
            # Split the data string based on the 'https' pattern
            desired_content = re.split(r'"story":{"message":{"text":', dsrd_content)[1]
            #desired_content = clean_string(desired_content)
    #*************************************************************

    # Check if the response contains user-generated content
    if is_user_generated_content(content_type):
        content = extract_content(har_entry)
        extracted_content = {
            'url': url,
            'content_type': content_type,
            'content': content
        }
    else:
        extracted_content = 'No matching structure found'
    return extracted_content, desired_content

def process_string(input_string):

    if len(input_string) < 150:
        return input_string
    else:
        # Trim the input string to 147 characters and add "..."
        return input_string[:150] + "..."

def clean_string(input_string):

    cleaned_string = input_string
    if input_string:
        youtube_pattern = r'https:\\/\\/youtu.be\\/(?:[a-zA-Z0-9_-]{11})'
        match = re.search(youtube_pattern, input_string)
    
        if match:
            # Extract the matched YouTube URL
            clean_youtube_url = match.group(0)
            # Convert the URL to a clear format
            cleaned_string = input_string.replace(clean_youtube_url, 'Watch below video for property')

     # Replace escaped newline characters with actual newline characters
    cleaned_string = cleaned_string.replace('\\n', '\n')

    # Remove extra spaces and newline characters
    cleaned_string = ' '.join(cleaned_string.split())

    # Remove curly brackets
    cleaned_string = re.sub(r'[{}]', '', cleaned_string)

    # Remove newline characters
    # Remove all newline characters
    cleaned_string = cleaned_string.replace('\\n', ' ')
    cleaned_string = cleaned_string.replace('\n\n', ' ')

    # Remove double quotes at the beginning and end of the string
    cleaned_string = cleaned_string.strip('\"')

    return cleaned_string

def is_user_generated_content(content_type):
    return 'text' in content_type.lower()

def extract_content(response):
    content_type = response.get('content', {}).get('mimeType', '')

    if 'text' in content_type.lower():
        text_content = response.get('content', {}).get('text', '')
        return text_content
    elif 'image' in content_type:
        # For image content
        return 'image data'  # Replace with your logic to extract image data
    elif 'video' in content_type:
        # For video content
        return 'video data'  # Replace with your logic to extract video data
    else:
        return 'unsupported content type'

def clean_and_extract_urls(data):

    if len(data) != 0:
        # Convert the list to a single string
        data_string = ' '.join(data)

        # Split the data string based on the 'https' pattern
        url_segments = re.split(r'https', data_string)

        # Define a regex pattern for extracting URLs
        url_pattern = r'https[^\s]+?\.(?:jpg|png)[^\s]*'

        # Initialize an empty list to store the cleaned URLs
        cleaned_urls = []

        # Process each segment
        for segment in url_segments:
            # Use regex to find the URL in the segment
            match = re.search(url_pattern, 'https' + segment)
            if match:
                # Get the matched URL
                url = match.group(0)
                # Strip out any unwanted data after the first comma in the URL
                cleaned_url = url.split('",', 1)[0]
                # Append the cleaned URL to the result list
                cleaned_urls.append(cleaned_url)

        #return cleaned_urls
        return set(cleaned_urls)

def extract_filename(url):
    parsed_url = urllib.parse.urlparse(url)
    # Extract the path component and get the base name
    filename = os.path.basename(parsed_url.path)
    return filename

def extract_media_urls(text_content):
        
    all_urls = re.findall(r'https?://[^\s]+\.jpg|https?://[^\s]+\.png|https?://[^\s]+\.mp4', text_content)

    # Using a set to store unique URLs
    #unique_urls_set = set(all_urls)

            # Filter URLs based on file extension
    video_urls = [re.search(r'https?://[^\s]+\.mp4', url).group() for url in all_urls if url.endswith('.mp4')]
    image_urls = [url for url in all_urls if url.endswith('.jpg') or url.endswith('.png')]

    if not image_urls:
       image_urls = []


    return image_urls

def extract_youtube_urls(text):
    # Use a regex pattern to check if the text has a YouTube URL
    #youtube_pattern = r'https?://(?:www\.)?(?:youtu\.be/|youtube\.com/(?:[^/\n\s]+/[\S]*?/|(?:v|e(?:mbed)?)?/|.*[?&]v=)|youtu\.be/)([a-zA-Z0-9_-]{11})'
    #youtube_pattern = r'https?:\\/\\/(?:www\\.)?(?:youtu\\.be/|youtube\\.com/(?:[^/\\n\\s]+/[\\S]*?/|(?:v|e(?:mbed)?)?/|.*[?&]v=)|youtu\\.be/)([a-zA-Z0-9_-]{11})'
    if text:
        youtube_pattern = r'https:\\/\\/youtu.be\\/(?:[a-zA-Z0-9_-]{11})'
        match = re.search(youtube_pattern, text)
    
        if match:
            # Extract the matched YouTube URL
            clean_youtube_url = match.group(0)
            # Convert the URL to a clear format
            clean_youtube_url = clean_youtube_url.replace('\\/', '/')
                    # Extract the video ID from the clean URL
            video_id_match = re.search(r'/([a-zA-Z0-9_-]{11})$', clean_youtube_url)
            if video_id_match:
                video_id = video_id_match.group(1)
                # Construct the clean YouTube URL with '.com'
                clean_youtube_url = f'https://www.youtube.com/watch?v={video_id}'
                return clean_youtube_url
            else:
                return None
        else:
            return None

import os
import base64

def save_media_content(media_urls, entries, desrd_text):
    media_data = []
    image_paths = []
    unique_image_paths = []

    # Create 'output' folder in the code execution directory
    output_folder = os.path.join(os.getcwd(), 'output')
    media_folder = os.path.join(output_folder, 'media')
    os.makedirs(media_folder, exist_ok=True)

    if desrd_text:
        if media_urls is not None and len(media_urls) != 0:
            for url in media_urls:
                for entry in entries:
                    if url in entry['request']['url']:
                        media_data.append({
                            'url': url,
                            'content': entry['response']['content']['text']
                        })

            for data in media_data:
                # file_extension = os.path.splitext(data['url'])[1]
                # file_name = f"{data['url'].replace('/', '_').replace(':', '_')}{file_extension}"
                file_name = extract_filename(data['url'])
                file_path = os.path.join(media_folder, file_name)

                with open(file_path, 'wb') as file:
                    file.write(base64.b64decode(data['content']))
                    image_paths.append(file_path)
    unique_image_paths = set(image_paths)    
    return unique_image_paths

def filter_youtube_videos(media_urls):
    if media_urls is not None and len(media_urls) != 0:
       return [url for url in media_urls if 'youtube.com' in urlparse(url).netloc]

def create_csv(posts):
    with open('captured_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Post Message', 'Image URL', 'Video URL', 'Image Local Path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for post in posts:
                #if post['text_content'] is not None and post['text_content'] != '':
                    writer.writerow({
                        'Title': post['title'],
                        'Post Message': post['text_content'],
                        'Image URL': post['media_urls'],
                        'Video URL': post['youtube_videos'],
                        'Image Local Path': post['Image Local Path']
                    })

def process_har(har_data):
    entries = har_data['log']['entries']
    posts = []

    for entry in entries:
        url = entry['request']['url']
        image_paths = []
        media_urls = ''
        clnd_media_urls = ''
        text_content = ''

        if 'https://www.facebook.com/api/graphql/' in url:
            response = entry['response']

            tupleTextContent = extract_text_content(response)
            extracted_content, desired_text = tupleTextContent[0], tupleTextContent[1]

            # Now you can access extracted_content and desired_content as separate variables
            text_content = extracted_content.get('content', [])

            if text_content:
                print(f"desired_text: {desired_text}")
                media_urls = extract_media_urls(text_content)
                print(f"Before Cln Media Urls: {media_urls}")
                clnd_media_urls = clean_and_extract_urls(media_urls)
                print(f"After Cln Media Urls: {clnd_media_urls}")
                if desired_text is not None and desired_text != '':
                    image_paths = save_media_content(clnd_media_urls, entries, desired_text)
                    #if clnd_media_urls is not None and len(clnd_media_urls) != 0:
                
                youtube_videos = extract_youtube_urls(desired_text)
                if youtube_videos is not None and len(youtube_videos) != 0:
                    clnd_media_urls = youtube_videos
                    image_paths = youtube_videos
                clnd_user_text = clean_string(desired_text)
                title = process_string(clnd_user_text)
                posts.append({
                        'title': title,
                        'text_content': clnd_user_text,
                        'media_urls': clnd_media_urls,
                        'youtube_videos': youtube_videos,
                        'Image Local Path': image_paths
                    })
    create_csv(posts)

if __name__ == "__main__":
    with open('F:\\HarFiles\\www.facebook.com_Archive [23-10-15 19-35-13].har', 'r', encoding='utf-8') as har_file:
        har_data = json.load(har_file)

    process_har(har_data)
