import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\Yavan\OneDrive\Pictures\Screenshots\Screenshot 2026-07-30 230807.png")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5,5), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(img, kernel, iterations=1)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Dilated Image", dilated)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
