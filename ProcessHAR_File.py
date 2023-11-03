import json
import csv
import base64

# Function to extract user-generated content from HTML
def extract_user_content(html_text):
    try:
        # You might need to customize this based on the HTML structure
        return html_text

    except Exception as e:
        print(f"Error extracting user content: {e}")
        return ""

# Function to extract post data from GraphQL response
def extract_post_data(response_content):
    post_data = {
        "Text": "",
        "Images": [],
        "Videos": []
    }

    try:
        # Parse the response content as JSON
        response_data = json.loads(response_content)

        # Extract post text
        post_text_base64 = response_data.get("content", {}).get("text", "")
        if post_text_base64:
            post_text = base64.b64decode(post_text_base64).decode('utf-8')
            post_data["Text"] = extract_user_content(post_text)

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

    return post_data

# Load the entire HAR file
har_file_path = 'C:\\Users\\Mynamek9i8n7g6s1d2t3\\Downloads\\wwwfacebookcom280923.har'

# Create or open a CSV file to store the extracted data
csv_file = open('facebook_post_data.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.DictWriter(csv_file, fieldnames=["Text", "Images", "Videos"])
csv_writer.writeheader()

try:
    # Read the entire HAR file as JSON
    with open(har_file_path, 'r', encoding='utf-8') as har_file:
        har_data = json.load(har_file)
        print("HAR file loaded successfully.")

        # Process a subset of entries in the HAR file
        num_entries_to_process = 5  # You can adjust this number
        entries_processed = 0

        for entry in har_data.get('log', {}).get('entries', []):
            request = entry.get('request', {})
            response = entry.get('response', {})

            print(f"Processing entry - Request URL: {request.get('url', 'N/A')}")

            # Check if the request URL is for Facebook GraphQL
            if 'facebook.com/api/graphql/' in request.get('url', ''):
                print("Request URL matches Facebook GraphQL.")

                response_content = response.get('content', {}).get('text', '')

                # Extract post data from the GraphQL response
                post_data = extract_post_data(response_content)

                # Write the extracted data to the CSV file
                csv_writer.writerow(post_data)
                print("Data extracted and written to CSV.")

                entries_processed += 1

                if entries_processed >= num_entries_to_process:
                    break

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")

# Close the CSV file
csv_file.close()

print("Extraction and CSV writing complete.")
