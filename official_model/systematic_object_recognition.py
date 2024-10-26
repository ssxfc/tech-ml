import numpy as np
import torchvision
import torchvision.transforms as transforms
from PIL import Image, ImageDraw

model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

image=Image.open(r'..\img\multi-cycle.jpg')
transform_d=transforms.Compose([transforms.ToTensor()])
image_t=transform_d(image)  #对图像进行变换
pred=model([image_t])

COCO_INSTANCE_CATEGORY_NAMES=[
    '__background__','person','bicycle','car','motorcycle',
    'airplane','bus','train','truck','boat','traffic light',
    'fire hydrant','N/A','stop sign','parking meter','bench',
    'bird','cat','dog','horse','sheep','cow','elephant',
    'bear','zebra','giraffe','N/A','backpack','umbrella','N/A',
    'N/A','handbag','tie','suitcase','frisbee','skis','snowboard',
    'surfboard','tennis racket','bottle','N/A','wine glass',
    'cup','fork','knife','spoon','bowl','banana','apple',
    'sandwich','orange','broccoli','carrot','hot dog','pizza',
    'donut','cake','chair','couch','potted plant','bed','N/A',
    'dining table','N/A','N/A','toilet','N/A','tv','laptop',
    'mouse','remote','keyboard','cell phone','microwave','oven',
    'toaster','sink','refrigerator','N/A','book','clock',
    'vase','scissors','teddy bear','hair drier','toothbrush'
]

#检测出目标的类别和得分
pred_class=[COCO_INSTANCE_CATEGORY_NAMES[i] for i in list(pred[0]['labels'].numpy())]
pred_score=list(pred[0]['scores'].detach().numpy())
#检测出目标的边界框
pred_boxes=[[i[0],i[1],i[2],i[3]] for i in list(pred[0]['boxes'].detach().numpy())]
#只保留识别的概率大于0.5的结果
pred_index=[pred_score.index(x) for x in pred_score if x > 0.8]
#设置图像显示的字体
fontsize=np.int16(image.size[1] / 30)
#可视化图像
draw=ImageDraw.Draw(image)
for index in pred_index:
    box=pred_boxes[index]
    draw.rectangle(box,outline='red')
    texts=pred_class[index]+':'+str(np.round(pred_score[index],2))
    draw.text((box[0],box[1]),texts,fill='red')
image.show()
