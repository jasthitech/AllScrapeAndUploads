import requests
import os

# Set your Pixabay API key here
API_KEY = "38961345-d39b58537cbfb99cc4d199c93"

# Set the search queries for animals
animal_queries = ["Ring","Tailed Lemur"]

# Set the number of images to download for each animal
num_images_per_animal = 3

# Initialize the global counter
global_counter = 1

# Loop through each animal query
for query in animal_queries:
    # Set the API URL
    api_url = f"https://pixabay.com/api/?key={API_KEY}&q={query}&image_type=photo&per_page={num_images_per_animal}"

    # Send an HTTP GET request to the API
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        images = data["hits"]

        # Download the specified number of images
        for image_info in images:
            image_url = image_info["webformatURL"]
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                image_data = image_response.content
                image_filename = f"{global_counter:02d}_{query}_{image_info['id']}.jpg"  # Using global_counter with leading zeros
                with open(image_filename, "wb") as f:
                    f.write(image_data)
                print(f"Image {image_filename} downloaded successfully.")
                global_counter += 1  # Increment the global counter
            else:
                print(f"Failed to download image {image_info['id']} for {query}.")
    else:
        print(f"Failed to fetch images from Pixabay API for {query} status code {response.status_code}.")
