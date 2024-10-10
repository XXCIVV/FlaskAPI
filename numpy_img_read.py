import numpy as np
import cv2
import matplotlib.pyplot as plt
import glob

image_paths = glob.glob("D:/VSproject/FlaskAPI/uploads/*.jpg")
for img_path in image_paths:
    img = cv2.imread(img_path)
    img_numpy = np.array(img)
    img_dimention = img_numpy.shape

    print(f"Image at {image_paths} has dimention: {img_dimention}")

    # Resize
    width = 480
    height = 800
    dim = (width, height)

    resized_img = cv2.resize(img_numpy, dim, interpolation = cv2.INTER_AREA)

    cv2.imshow(f'Image: {image_paths}', resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()