import cv2
import numpy as np
from io import BytesIO
from PIL import Image

def detect_skin_tone_from_image(image_bytes):
    image = Image.open(BytesIO(image_bytes)).convert('RGB')
    image_np = np.array(image)

    height, width, _ = image_np.shape
    center = image_np[height//3:height//2, width//3:width//2]

    avg_color = np.mean(center, axis=(0, 1))
    r, g, b = avg_color

    if r > 180 and g > 160:
        return "Fair"
    elif r > 120 and g > 100:
        return "Medium"
    else:
        return "Dark"
 
