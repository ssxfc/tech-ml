import cv2
from PIL import Image

def cv2_image(img):
    """
    :param img:
    :return:
    """
    return cv2.imread(img)


def pil_image(img):
    return Image.open(img)
