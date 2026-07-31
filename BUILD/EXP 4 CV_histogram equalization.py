import cv2

# Read the image
img = cv2.imread(r"C:\Users\Yavan\OneDrive\Pictures\Screenshots\Screenshot 2026-07-27 203351.png")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Histogram Equalization
    equalized = cv2.equalizeHist(gray)

    # Display Original and Equalized images
    cv2.imshow("Original Grayscale Image", gray)
    cv2.imshow("Histogram Equalized Image", equalized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
