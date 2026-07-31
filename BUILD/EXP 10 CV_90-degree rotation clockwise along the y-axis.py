import cv2

# Read the image
img = cv2.imread(r"C:\Users\Yavan\OneDrive\Pictures\Screenshots\Screenshot 2026-07-30 231529.png")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Rotate the image 90 degrees clockwise
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("90 Degree Clockwise Rotation", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
