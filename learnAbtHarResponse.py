import json

def load_har_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        har_data = json.load(file)
    return har_data

def extract_response_text(entry):
    if 'response' in entry and 'content' in entry['response']:
        content = entry['response']['content']
        if 'text' in content:
            text = content['text']
            return text[:200]  # Extracting the first 200 characters
    return None

def process_har_entries(har_data):
    if 'log' in har_data and 'entries' in har_data['log']:
        entries = har_data['log']['entries']
        for i, entry in enumerate(entries, start=1):
            url = entry['request']['url']
            method = entry['request']['method']
            status = entry['response']['status']
            content_type = entry['response']['content']['mimeType']
            response_text = extract_response_text(entry)

            print(f"\nEntry {i}:")
            print(f"Request URL: {url}")
            print(f"Request Method: {method}")
            print(f"Response Status: {status}")
            print(f"Content Type: {content_type}")
            print(f"Response Text: {response_text}")

def main():
    file_path = r'C:\\Users\\Mynamek9i8n7g6s1d2t3\\Downloads\\www.facebook.com_Archive [23-09-21 17-18-32].har'  # Replace with your HAR file path
    har_data = load_har_file(file_path)

    if har_data:
        process_har_entries(har_data)
    else:
        print("Failed to load the HAR file.")

if __name__ == "__main__":
    main()
