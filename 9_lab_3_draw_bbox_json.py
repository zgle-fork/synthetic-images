import os, math 
from PIL import Image, ImageDraw 
import json


def draw_bbs(img_fp, annotations):
    img=Image.open(img_fp)
    for a in annotations:
        c=a['coordinates']
        x, y, w, h =c['x'], c['y'],c['width'],c['height']
        label=a['label'] 

        shape = [(x-w/2, y-h/2), (x +w/2, y+h/2)] 
    
        # create rectangle image 
        img1 = ImageDraw.Draw(img)   
        img1.rectangle(shape, outline ="red") 
    
    # img.show() 
    img.save(os.path.join('Out',img_fp))      


def draw_bb(img_fp, x,y,w,h):
    img=Image.open(img_fp)
    shape = [(x-w/2, y-h/2), (x +w/2, y+h/2)] # two corner points: [(x0, y0), (x1, y1)]
    
    # create rectangle image 
    img1 = ImageDraw.Draw(img)   
    img1.rectangle(shape, outline ="red") 
    # img.show() 
    img.save(os.path.join('Out',img_fp))

# img_fp='TrainingImages/1.png'
# x, y, w, h =1405, 681, 90, 150
# draw_bb(img_fp, x, y, w, h)
json_fp='annotations.json'
data=json.load(open(json_fp))
for x in data:
    print(x)
    img_fp=x['path']
    draw_bbs(img_fp, x['annotations'])
    # for a in x['annotations']:
    #     c=a['coordinates']
    #     x, y, w, h =c['x'], c['y'],c['width'],c['height']
    #     label=a['label']        
    #     # draw_bb(img_fp, x, y, w, h)
