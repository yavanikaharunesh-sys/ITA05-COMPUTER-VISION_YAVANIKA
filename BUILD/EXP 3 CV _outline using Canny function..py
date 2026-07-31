import cv2

# Read the image
img = cv2.imread(r"C:\Users\Yavan\OneDrive\Pictures\Screenshots\Screenshot 2026-07-27 203351.png")

# Check if the image is loaded
if img is None:
    print("Image not found!")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Display the original image
    cv2.imshow("Original Image", img)

    # Display the edge-detected image
    cv2.imshow("Canny Edge Image", edges)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
