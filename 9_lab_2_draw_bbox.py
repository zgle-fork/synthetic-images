import math 
from PIL import Image, ImageDraw 

img=Image.open('TrainingImages/1.png')
# img=Image.open('TrainingImages/2.png')
width, height = img.size
print(width, height)  

#1.png
w, h = 90, 150
x,y=1405, 681.0

# #2.png
# w, h = 180, 300
# x,y=1535.0, 686.0


shape = [(x-w/2, y-h/2), (x +w/2, y+h/2)] # two corner points: [(x0, y0), (x1, y1)]
  
# create rectangle image 
img1 = ImageDraw.Draw(img)   
img1.rectangle(shape, outline ="red") 
# img1.rectangle([(10,10),(100,100)], outline ="blue") 
img.show() 