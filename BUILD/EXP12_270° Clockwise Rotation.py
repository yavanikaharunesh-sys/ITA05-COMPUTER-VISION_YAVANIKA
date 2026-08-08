import cv2
img = cv2.imread(r'C:\Users\Yavan\AppData\Local\Temp\bf0382e7-1448-4870-85c8-073d8b2c09cd_files.zip.9cd\image2_triangles.png' )
rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 270° CW = 90° CCW
cv2.imshow('Original', img)
cv2.imshow('270 Rotated', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
