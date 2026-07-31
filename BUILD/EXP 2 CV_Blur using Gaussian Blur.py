import cv2

# Read the image
img = cv2.imread(r"C:\Users\Yavan\OneDrive\Pictures\Screenshots\Screenshot 2026-07-27 203351.png")

# Apply Gaussian Blur (larger kernel)
blur = cv2.GaussianBlur(img, (31, 31), 0)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
