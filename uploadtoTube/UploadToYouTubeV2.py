import os
import json
import time
import google.oauth2.credentials
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Define the YouTube API constants
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# Specify the path to the folder containing the videos to upload
VIDEO_FOLDER_PATH = "C:\\Users\\Mynamek9i8n7g6s1d2t3\\Downloads\\FunnyTikTok\\120923"

def authorize_youtube_api():
    # Check for existing OAuth 2.0 credentials (token.json)
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        # If not found, perform OAuth 2.0 authorization
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
        creds = flow.run_local_server(port=0)

        # Save the credentials for future use
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    # Build the YouTube API client
    youtube = build(API_SERVICE_NAME, API_VERSION, credentials=creds)

    return youtube

def upload_video_and_delete(youtube, video_path):
    video_filename = os.path.basename(video_path)
    video_title = os.path.splitext(video_filename)[0]
    video_description = video_title  # Use the filename as the description

    request_body = {
        "snippet": {
            "title": video_title,
            "description": video_description,
            "tags": [],  # You can add tags here if needed
            "categoryId": "22",  # Category ID for Entertainment
            "defaultLanguage": "en",  # Set video language to English
        },
        "status": {
            "privacyStatus": "public",  # Set to "public" to publish the video
            "selfDeclaredMadeForKids": False,  # Set to False for "Not Made for Kids"
        },
    }

    # Print the request metadata
    print("Request Metadata:")
    print(json.dumps(request_body, indent=2))

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)

    response = youtube.videos().insert(part="snippet,status", body=request_body, media_body=media).execute()
    print(f"Uploaded video: {video_path}")

    # Delete the video file locally
    # Sleep for 15 minutes
    time.sleep(1 * 15)
    os.remove(video_path)
    print(f"Deleted video: {video_path}")

def main():
    youtube = authorize_youtube_api()

    # List video files in the specified folder
    video_files = [f for f in os.listdir(VIDEO_FOLDER_PATH) if f.endswith(".mp4")]

    for video_file in video_files:
        video_path = os.path.join(VIDEO_FOLDER_PATH, video_file)
        upload_video_and_delete(youtube, video_path)

if __name__ == "__main__":
    main()
