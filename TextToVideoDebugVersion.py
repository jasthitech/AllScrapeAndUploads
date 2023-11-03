from moviepy.editor import ImageClip, TextClip, concatenate_videoclips
from moviepy.editor import VideoClip
import cv2
import os

from moviepy.video.compositing.concatenate import np

# Path to the FFmpeg binary (replace 'path/to/ffmpeg' with the actual path)
ffmpeg_path = "C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\ffmpeg.exe"
os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path

# Path to the folder containing images
image_folder = 'D:\\Scraping-tool\\MinimaxiFirewall\\output\\texttovideo\\imagesforvideo'

# Path to the text file containing the product description
text_file = 'D:\\Scraping-tool\\MinimaxiFirewall\\output\\texttovideo\\productDesicription.txt'

# # Read text from the file
# with open(text_file, 'r') as file:
#     product_description = file.read()

# # Define a function that returns an image as a NumPy array
# def make_frame_text(t):
#     img = np.zeros((480, 640, 3), dtype=np.uint8)
#     text = product_description
#     cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
#     return img

# # Create a VideoClip using the function for text
# text_clip = VideoClip(make_frame_text, duration=5)

# Get a list of image files in the folder
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Sort the image files to ensure proper sequence
image_files.sort()

# # Define a function that returns an image as a NumPy array for images
# def make_frame_image(t):
#     img_path = os.path.join(image_folder, image_files[int(t * len(image_files))])
#     img = cv2.imread(img_path)
#     return img

def make_frame_image(t):
    index = int(t * len(image_files)) % len(image_files)
    img_path = os.path.join(image_folder, image_files[index])
    img = ImageClip(img_path, duration=1)
    return img.get_frame(t)


# Create a VideoClip using the function for images
# Create a list of image clips
#image_clips = [ImageClip(os.path.join(image_folder, img), duration=1) for img in image_files]
image_clips = [ImageClip(os.path.join(image_folder, img), duration=2) for img in image_files]

# Concatenate only the image clips
final_clip = concatenate_videoclips(image_clips, method="compose")

# Write the video file
final_clip.write_videofile('output.mp4', codec='libx264', fps=24)