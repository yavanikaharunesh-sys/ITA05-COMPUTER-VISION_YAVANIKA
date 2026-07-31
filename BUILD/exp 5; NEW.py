import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread(r"C:\Users\Yavan\OneDrive\Pictures\Screenshots\Screenshot 2026-07-30 224719.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10,5))

# Original Image
plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

# Histogram
plt.subplot(1,2,2)
colors = ('r','g','b')

for i, color in enumerate(colors):
    hist = cv2.calcHist([cv2.cvtColor(img, cv2.COLOR_RGB2BGR)], [i], None, [256], [0,256])
    plt.plot(hist, color=color)

plt.title("Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim([0,256])
plt.grid()

plt.tight_layout()
plt.show()
