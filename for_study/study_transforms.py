from torchvision import transforms
import cv2
from PIL import Image
import numpy as np
import torch


def cv2_image(img):
    """
    :param img:
    :return:
    """
    return cv2.imread(img)


def pil_image(img):
    return Image.open(img)


# 打开一张图片
image = cv2_image("cycle.jpg")

trans_chain = transforms.Compose([transforms.ToTensor()])
output = trans_chain(image)
image = (output.permute(1, 2, 0).numpy() * 256).astype(np.uint8)
cv2.imshow("", image)

# 等待中断事件
cv2.waitKey()
cv2.destroyAllWindows()
