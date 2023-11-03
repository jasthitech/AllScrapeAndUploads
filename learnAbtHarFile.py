import json

def process_har_file(har_file_path, output_lines=50):
    try:
        # Read the entire HAR file as JSON
        with open(har_file_path, 'r', encoding='utf-8') as har_file:
            har_data = json.load(har_file)
            print("HAR file loaded successfully.")

            # Print basic information about the HAR file
            print(f"Number of entries: {len(har_data.get('log', {}).get('entries', []))}")

            # Process each entry in the HAR file
            for i, entry in enumerate(har_data.get('log', {}).get('entries', [])):
                print(f"\nEntry {i + 1}:")

                # Print request information
                request = entry.get('request', {})
                print(f"Request URL: {request.get('url', 'N/A')}")
                print(f"Request Method: {request.get('method', 'N/A')}")

                # Print response information
                response = entry.get('response', {})
                print(f"Response Status: {response.get('status', 'N/A')}")
                print(f"Content Type: {response.get('content', {}).get('mimeType', 'N/A')}")

                # Limit the number of printed lines
                if i + 1 == output_lines:
                    print("\nOutput limit reached. Please share this summary.")
                    break

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

# Specify the path to your HAR file
har_file_path = 'C:\\Users\\Mynamek9i8n7g6s1d2t3\\Downloads\\www.facebook.com_Archive [23-09-21 17-18-32].har'

# Process the HAR file and print a summary
process_har_file(har_file_path)
