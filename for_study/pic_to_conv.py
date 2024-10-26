from torchvision import transforms
import cv2
from PIL import Image
import numpy as np
import torch
import pathlib as pl
import shutil

tmp_dir = pl.Path("./tmp")


loader = transforms.Compose([
    transforms.ToTensor()])  

unloader = transforms.ToPILImage()

def cv2_image(img):
    return cv2.imread(img)


def pil_image(img):
    image = Image.open(img).convert('RGB')
    image = loader(image).unsqueeze(0)
    return image.to(torch.float)


image = pil_image("../images/cycle.jpg")
# 生成一个conv2d
conv1 = torch.nn.Conv2d(3, 24, 3, 1, 1)
conv2 = torch.nn.Conv2d(24, 48, 3, 1, 1)
output = conv1(image)
output = conv2(output)
idx = 0
shutil.rmtree("./tmp")
tmp_dir.mkdir()
for i in range(8):
    one_pic = output[:, idx:idx + 3, :, :]
    idx += 3
    x = unloader(one_pic[0])
    x.save("tmp/%d.jpg" % idx)