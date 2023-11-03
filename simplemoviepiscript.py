from moviepy.editor import VideoClip
import numpy as np
import cv2

# Define a function that returns an image as a NumPy array
def make_frame(t):
    # Create a simple black image with white text
    img = np.zeros((480, 640, 3), dtype=np.uint8)
    text = f"Frame at {t}"
    cv2.putText(img, text, (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    return img

# Create a VideoClip using the function
clip = VideoClip(make_frame, duration=5)

# Write the video file
clip.write_videofile("output.mp4", codec='libx264', fps=24)
