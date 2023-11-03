import os
import random
import time
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# YouTube Data API version and API key
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"
#API_KEY = "AIzaSyDrqXX3QsDFcz6n0k1XH5qzZhi4oY8tvAs"  # Replace with your API key
API_KEY = "AIzaSyDKRozVmu3VDl3zWdHHFc5uWM0555O_4IY"

# Folder path containing video files
VIDEO_FOLDER = "C:\\Users\\Mynamek9i8n7g6s1d2t3\\Downloads\\FunnyTikTok\\120923"

# Function to authorize the script to access the YouTube API
def authorize_youtube_api():
    SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
    creds = None

    if os.path.exists("token.json"):
        creds = google.oauth2.credentials.Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
        creds = flow.run_local_server(port=0)

    with open("token.json", "w") as token:
        token.write(creds.to_json())

    return build(API_SERVICE_NAME, API_VERSION, credentials=creds)

# Function to pick a random video file from the folder
def pick_random_video():
    video_files = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(".mp4")]
    if video_files:
        return os.path.join(VIDEO_FOLDER, random.choice(video_files))
    else:
        return None

# Function to upload a video to YouTube and delete it locally
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
        },
        "status": {
            "privacyStatus": "public",  # Set to "public" to publish the video
            "selfDeclaredMadeForKids": False,  # Set to False for "Not Made for Kids"
        },
    }

    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)

    response = youtube.videos().insert(part="snippet,status", body=request_body, media_body=media).execute()
    print(f"Uploaded video: {video_path}")

    # Delete the video file locally
    os.remove(video_path)
    print(f"Deleted video: {video_path}")

if __name__ == "__main__":
    youtube = authorize_youtube_api()
    
    while True:
        video_path = pick_random_video()
        if video_path:
            upload_video_and_delete(youtube, video_path)
        else:
            print("No video files found in the folder.")

        # Sleep for 15 minutes
        time.sleep(15 * 60)
