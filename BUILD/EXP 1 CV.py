import cv2

# Read the image
image = cv2.imread(r"C:\Users\Yavan\OneDrive\Pictures\Screenshots\Screenshot 2026-07-27 203351.png")

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original image
    cv2.imshow("Original Image", image)

    # Display the grayscale image
    cv2.imshow("Gray-scale Image", gray)

    # Save the grayscale image
    cv2.imwrite("gray_image.jpg", gray)

    print("Gray-scale image saved as 'gray_image.jpg'.")

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
