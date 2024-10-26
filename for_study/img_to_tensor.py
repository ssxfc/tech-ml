import torch
from torchvision import transforms
from PIL import Image
import cv2
import numpy as np

trans_chain = transforms.Compose([transforms.ToTensor()])

# 将PIL图片转为tensor
pil_img = Image.open("../images/cycle.jpg")
pil_img
pil_img_tensor = trans_chain(pil_img)
pil_img_tensor
pil_img_tensor = pil_img_tensor.permute(1, 2, 0)
x =pil_img_tensor.detach().numpy()
x=(x * 255).astype(np.uint8)
x = x[:,:,2]
x = Image.fromarray(x)
x
# 灰度图或者单通道图转三通道图
three_channels = np.zeros([1365, 2048, 3], dtype=np.uint8)
three_channels[..., 2] = x
Image.fromarray(three_channels)