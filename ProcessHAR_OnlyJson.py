import pandas as pd
from haralyzer import HarParser

# Load the HAR file using haralyzer
har_parser = HarParser("C:\\Users\\Mynamek9i8n7g6s1d2t3\\Downloads\\www.facebook.com_Archive [23-09-21 17-18-32].har")

# Extract entries from the HAR file
entries = har_parser.har_data['log']['entries']

# Initialize a list to store post data
posts = []

# Process and organize the entries as needed
for entry in entries:
    # Check if the response content contains keywords indicating a Facebook post
    response_content = entry['response']['content']['text']
    
    # You should adjust these keywords based on the structure of Facebook posts in your HAR file
    if 'data-testid="fbfeed_story"' in response_content and 'data-testid="post_message"' in response_content:
        timestamp = entry['startedDateTime']
        post_content = response_content

        # Add the post data to the list
        posts.append([timestamp, post_content])

# Create a DataFrame from the list of posts
df = pd.DataFrame(posts, columns=['Timestamp', 'Post Content'])

# Save the post data to a CSV file
df.to_csv('facebook_posts.csv', index=False, encoding='utf-8')
