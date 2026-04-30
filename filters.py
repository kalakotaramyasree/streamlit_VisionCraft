import cv2
import numpy as np

def apply_blur(img, ksize):
    if ksize > 1:
        return cv2.GaussianBlur(img, (ksize, ksize), 0)
    return img

def apply_sharpness(img, alpha):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    sharp = cv2.filter2D(img, -1, kernel)
    return cv2.addWeighted(img, 1 - alpha, sharp, alpha, 0)

def apply_brightness(img, beta):
    return cv2.convertScaleAbs(img, alpha=1, beta=beta)

def apply_contrast(img, alpha):
    return cv2.convertScaleAbs(img, alpha=alpha, beta=0)

def apply_edge(img, t1, t2):
    edges = cv2.Canny(img, t1, t2)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

def apply_gray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)