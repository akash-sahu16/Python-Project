import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
import cv2

# Load the image
image_path = r"D:\download.jpg"
image = Image.open(image_path)

# Convert the image to a NumPy array
image_array = np.array(image)

# Display the original image
plt.figure(figsize=(12, 8))
plt.subplot(2, 4, 1)
plt.imshow(image_array)
plt.title("Original Image")

# Apply a Gaussian filter to reduce noise
filtered_image = ndimage.gaussian_filter(image_array, sigma=2)

# Display the filtered image
plt.subplot(2, 4, 2)
plt.imshow(filtered_image)
plt.title("Filtered Image (Gaussian)")

# Apply a Sobel filter for edge detection
sobel_image = ndimage.sobel(image_array)

# Display the Sobel filtered image
plt.subplot(2, 4, 3)
plt.imshow(sobel_image)
plt.title("Sobel Filtered Image")

# Additional Filters

# Cartoon Filter
cartoon_image = np.array(image)
cartoon_image = cv2.cvtColor(cartoon_image, cv2.COLOR_RGB2BGR)
gray = cv2.cvtColor(cartoon_image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
color = cv2.bilateralFilter(cartoon_image, 9, 250, 250)
cartoon_image = cv2.bitwise_and(color, color, mask=edges)
cartoon_image = cv2.cvtColor(cartoon_image, cv2.COLOR_BGR2RGB)

# Display the Cartoon filtered image
plt.subplot(2, 4, 4)
plt.imshow(cartoon_image)
plt.title("Cartoon Filtered Image")

# Retro Filter
retro_image = np.array(image)
retro_image = cv2.cvtColor(retro_image, cv2.COLOR_RGB2BGR)
retro_image = cv2.cvtColor(retro_image, cv2.COLOR_BGR2RGB)

# Display the Retro filtered image
plt.subplot(2, 4, 5)
plt.imshow(retro_image)
plt.title("Retro Filtered Image")

# Paris Filter
paris_image = ImageEnhance.Color(image).enhance(0.8)

# Display the Paris filtered image
plt.subplot(2, 4, 6)
plt.imshow(paris_image)
plt.title("Paris Filtered Image")

# B&W Filter
bw_image = image.convert("L")

# Display the B&W filtered image
plt.subplot(2, 4, 7)
plt.imshow(bw_image, cmap='gray')
plt.title("B&W Filtered Image")

# KiraKira Effect
kirakira_image = np.array(image)
kirakira_image[..., :3] += 60

# Display the KiraKira effect image
plt.subplot(2, 4, 8)
plt.imshow(kirakira_image)
plt.title("KiraKira Effect")

# Save the processed images
filtered_image_path = r"D:\photos\filtered_image.jpg"
sobel_image_path = r"D:\photos\sobel_image.jpg"
cartoon_image_path = r"D:\photos\cartoon_image.jpg"
retro_image_path = r"D:\photos\retro_image.jpg"
paris_image_path = r"D:\photos\paris_image.jpg"
bw_image_path = r"D:\photos\bw_image.jpg"
kirakira_image_path = r"D:\photos\kirakira_image.jpg"

Image.fromarray(filtered_image).save(filtered_image_path)
Image.fromarray(sobel_image).save(sobel_image_path)
Image.fromarray(cartoon_image).save(cartoon_image_path)
Image.fromarray(retro_image).save(retro_image_path)
paris_image.save(paris_image_path)
bw_image.save(bw_image_path)
Image.fromarray(kirakira_image).save(kirakira_image_path)

# Show the plots
plt.tight_layout()
plt.show()
