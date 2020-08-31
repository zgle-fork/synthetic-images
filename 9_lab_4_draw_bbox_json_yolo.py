import os, math 
from PIL import Image, ImageDraw, ImageFont
import json
import pathlib

def get_output_file_path(img_fp):
    # path=pathlib.Path(img_fp)
    fn=os.path.basename(img_fp)
    parent_path=os.path.dirname(img_fp)
    new_parent_path=parent_path+'_yolo_anno'
    os.makedirs(new_parent_path, mode=0o777, exist_ok=True)
    return os.path.join(new_parent_path,fn)

def draw_bbs(img_fp, annotations):
    img=Image.open(img_fp)
    annotation_lines=[]
    for a in annotations:
        c=a['coordinates']
        x, y, w, h =c['x'], c['y'],c['width'],c['height']
        label=a['label'][0] 
        font = ImageFont.truetype("arial.ttf", 15)
        
        shape = [(x-w/2, y-h/2), (x +w/2, y+h/2)] 
    
        # create rectangle image 
        img1 = ImageDraw.Draw(img)   
        img1.rectangle(shape, outline ="red") 

        img1.text((x, y), label,(255,255,255),font=font)

        #annotation
        img_w, img_h=img.size
        class_id=0 if label=='N' else 1
        annotation_line='{} {} {} {} {}\n'.format(class_id, float(x/img_w), float(y/img_h), float(w/img_w), float(h/img_h))
        annotation_lines.append(annotation_line)        
    
    # img.show() 
    out_img_fp=get_output_file_path(img_fp)
    # print('out_img_fp',out_img_fp)
    # img.save(out_img_fp)   
    generate_annotation_file(out_img_fp, annotation_lines)   

def generate_annotation_file(out_img_fp, annotation_lines):
    # img_w, img_h=img_size
    # class_id=0 if label=='N' else 1
    # line='{}'.format(class_id, float(x/img_w), float(y/img_h), float(w/img_w), float(h/img_h))
    txt_fp=out_img_fp[:-4]+'.txt'
    with open(txt_fp, 'w') as tf:
        tf.writelines(annotation_lines)


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
