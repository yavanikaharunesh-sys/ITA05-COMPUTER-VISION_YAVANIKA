import cv2
import numpy as np

img = cv2.imread(r'C:\Users\Yavan\AppData\Local\Temp\b2afe96b-6ba8-42e0-9ec9-abd35f74118f_files.zip.18f\image3_checkerboard.png')
rows, cols = img.shape[:2]

pts1 = np.float32([[0,0],[cols-1,0],[0,rows-1],[cols-1,rows-1]])
pts2 = np.float32([[0,0],[cols-1,0],[int(0.2*cols),rows-1],[int(0.8*cols),rows-1]])

M = cv2.getPerspectiveTransform(pts1, pts2)
perspective = cv2.warpPerspective(img, M, (cols, rows))

cv2.imshow('Original', img)
cv2.imshow('Perspective Transformed', perspective)
cv2.waitKey(0)
cv2.destroyAllWindows()
