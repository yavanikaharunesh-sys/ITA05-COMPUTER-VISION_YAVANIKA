import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\Yavan\OneDrive\Pictures\Screenshots\Screenshot 2026-07-30 224719.png")

# Check if the image is loaded
if img is None:
    print("Image not found!")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5,5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(img, kernel, iterations=1)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Eroded Image", eroded)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
