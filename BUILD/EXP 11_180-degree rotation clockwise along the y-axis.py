import cv2
img = cv2.imread(r"C:\Users\Yavan\AppData\Local\Temp\2e8a9e5a-d5db-45ae-bf71-a10dd1e1909b_files.zip.09b\image5_house.png")
rotated = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow('Original', img)
cv2.imshow('180 Rotated', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
