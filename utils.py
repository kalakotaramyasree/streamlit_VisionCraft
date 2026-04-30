from PIL import Image
import numpy as np
import cv2
import io

def read_image(file):
    return cv2.cvtColor(np.array(Image.open(file)), cv2.COLOR_RGB2BGR)

def convert_to_bytes(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    buf = io.BytesIO()
    Image.fromarray(img).save(buf, format="PNG")
    return buf.getvalue()