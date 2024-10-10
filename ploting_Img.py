import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob

image_paths = glob.glob("D:/VSproject/FlaskAPI/uploads/*.jpg")

images = []
for img_path in image_paths:
    img = cv2.imread(img_path)
     # Convert BGR (OpenCV format) to RGB for correct plotting
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    images.append(img_rgb)


n_images = len(images)
cols = 3  # Number of columns (change based on preference)
rows = (n_images // cols) + (n_images % cols > 0) 

# Subplots
fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))

axes = axes.ravel()

for i in range(n_images):
    axes[i].imshow(images[i])
    axes[i].set_title(f"Image {i+1}")
    

# Remove any extra subplots that aren't used
for i in range(n_images, rows * cols):
    fig.delaxes(axes[i])

plt.tight_layout()
plt.show()