import csv
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import ast

def authenticate():
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def upload_image(service, folder_id, image_path):
    file_ids = []
    try:
        # Safely evaluate the string as a literal
        image_paths = ast.literal_eval(image_path)

        # Iterate over each image path
        for path in image_paths:
            # Perform the upload for each image
            media = MediaFileUpload(path, mimetype='image/jpeg')
            file_metadata = {
                'name': os.path.basename(path),
                'parents': [folder_id],
            }
            file = service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()

            upLoded_file_id = file.get('id')
            print(f'File uploaded successfully. File ID: {upLoded_file_id}')
            file_ids.append(upLoded_file_id)

        return file_ids

    except Exception as e:
        print(f"Error uploading image: {str(e)}")
        return None

def main():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    # Load CSV and update image URLs
    csv_path = 'D:\\Scraping-tool\\HarScraping\\captured_data.csv'  # Replace with your CSV path
    rows = []

    with open(csv_path, 'r', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            gDrive_image_url = []
            image_path = row.get('Image Local Path', '')
            
            if image_path:
                # Upload image to Google Drive
                folder_id = '1_5nLWLHuKqRsPKYpIn6pOSAldyTWZmSt'  # Replace with your Google Drive folder ID
                file_ids = upload_image(service, folder_id, image_path)
                if file_ids is not None and len(file_ids) != 0:
                    for file_id in file_ids:
                        image_url = f'https://drive.google.com/uc?id={file_id}'
                        wordPressInsertUrl_p1 = '<figure class="wp-block-image size-large"><img src="'
                        wordPressInsertUrl_p2 = '" alt=""/></figure>'
                        wordPressInsertUrl_final = f'{wordPressInsertUrl_p1}{image_url}{wordPressInsertUrl_p2}'
                        gDrive_image_url.append(wordPressInsertUrl_final)
                    
            # Update CSV row with Google Drive image URL
            row['Image Local Path'] = gDrive_image_url

            rows.append(row)

    # Write updated rows back to CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Post Message', 'Image URL', 'Video URL', 'Image Local Path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore', delimiter=',', quotechar='"')
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':
    main()
