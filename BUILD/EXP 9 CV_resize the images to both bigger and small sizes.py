import cv2

# Read the image
img = cv2.imread(r"C:\Users\Yavan\OneDrive\Pictures\Screenshots\Screenshot 2026-07-30 231121.png")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Resize to bigger size (2 times)
    bigger = cv2.resize(img, None, fx=2, fy=2)

    # Resize to smaller size (0.5 times)
    smaller = cv2.resize(img, None, fx=0.5, fy=0.5)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
