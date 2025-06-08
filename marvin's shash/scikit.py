import matplotlib.pyplot as plt
from skimage import io, color, filters, morphology, feature, exposure
import numpy as np

image = io.imread('grid2.png')
if image.shape[-1] == 4:
    image = image[..., :3]  # Keep only the first 3 channels (RGB)

gray = color.rgb2gray(image)  # Convert to grayscale

gray = filters.gaussian(gray, sigma=1)

white_mask = np.all(image >= 50, axis=-1)

white_mask = morphology.closing(white_mask, morphology.square(5))  # Closing operation to fill gaps

edges = feature.canny(white_mask, sigma=2)

closed = morphology.closing(edges, morphology.square(3))

skeleton = morphology.thin(closed)

skeleton_enhanced = exposure.rescale_intensity(skeleton.astype(float), in_range='image', out_range=(0, 1))

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(white_mask, cmap='gray')
axes[0].set_title("Grayscale Image")
axes[1].imshow(edges, cmap='gray')
axes[1].set_title("Canny Edges")
axes[2].imshow(closed, cmap='gray')
axes[2].set_title("Detected Streets (Skeleton)")

for ax in axes:
    ax.axis('off')
plt.tight_layout()
plt.show()