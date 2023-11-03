import requests

# Set your Pixabay API key here
API_KEY = "38961345-d39b58537cbfb99cc4d199c93"

# Set the search query
search_query = "cat"

# Set the API URL
api_url = f"https://pixabay.com/api/?key={API_KEY}&q={search_query}&image_type=photo"

# Send an HTTP GET request to the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    images = data["hits"]

    # Download the images
    for image_info in images:
        image_url = image_info["webformatURL"]
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            image_data = image_response.content
            with open(f"{image_info['id']}.jpg", "wb") as f:
                f.write(image_data)
            print(f"Image {image_info['id']} downloaded successfully.")
        else:
            print(f"Failed to download image {image_info['id']}.")
else:
    print("Failed to fetch images from Pixabay API.")
