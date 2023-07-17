from skimage import io, img_as_float
from skimage.metrics import structural_similarity as ssim
import numpy as np
import cv2
import os 
import cv2
import os


def compare_images(img_path1, img_path2):
    # Load images
    img1 = img_as_float(io.imread(img_path1, as_gray=True))
    img2 = img_as_float(io.imread(img_path2, as_gray=True))

    # Check if images are the same size
    if img1.shape != img2.shape:
        print("Images must be the same shape!")
        return

    # Compute SSIM between two images
    ssim_value = ssim(img1, img2, data_range=img1.max() - img1.min())

    # Because SSIM index returns a value in range [-1, 1]
    # where -1 indicates no correlation (0% similarity) and 1 indicates a perfect match (100% similarity),
    # We normalize it to [0, 1] range and make it a percentage
    percent_match = ((ssim_value + 1) / 2) * 100

    print(f"The images are {percent_match}% a match.")
    if percent_match < 99:
        return False
    else:
        return True


def video_to_frames(video_path, output_dir="frames"):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Create output directory path
    output_dir = os.path.join(script_dir, output_dir)

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Capture video
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        # Save frame as JPEG file
        output_path = os.path.join(output_dir, f"frame{count}.jpg")
        write_success = cv2.imwrite(output_path, image)
        if write_success:
            print(f'Successfully wrote frame{count}.jpg')
        else:
            print(f'Failed to write frame{count}.jpg')
        success, image = vidcap.read()
        count += 1


def framify():
    video_to_frames('fish.mp4')
def remfakes():
    images_to_remove = []
    files = os.listdir("frames")
 
    for filename in range(1, len(files)):
        print(filename, filename-1)
        img1 = os.path.join("frames", "frame"+str(filename-1)+".jpg")
        img2 = os.path.join("frames", "frame"+str(filename)+".jpg")
    
    # Compare the images
        if compare_images(img1, img2):
        # If the images are the same, add the current image to the removal list
            images_to_remove.append(img2)

    return images_to_remove

def delFiles(images_to_remove):
    for image in images_to_remove:
        try:
            os.remove(image)
            print(f"File {image} has been removed successfully")
        except Exception as e:
            print(f"Error occurred while trying to remove file {image}. Error message: {e}")

def checklen():
    files = os.listdir("frames")
    print(len(files))