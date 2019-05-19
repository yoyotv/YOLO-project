#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from pycocotools import coco
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

from PIL import Image

def show(id):
  imgid= coco.getImgIds(id)
  #print imgid
  Imgs = coco.loadImgs(id)[0]
  #print Imgs
  imagefile = "/home/dl-linux/coco/images/"
  imageurl = imagefile + Imgs['file_name']
  #print imageurl
  I = io.imread(imageurl)

  plt.imshow(I)
  plt.show()

  return Imgs, I ,Imgs['file_name']


dataDir='..'
dataType='val2017'
annFile='{}/annotations/instances_{}.json'.format(dataDir,dataType)
annFile = "/home/dl-linux/coco/annotations/annotations/D2S_training.json"
coco=coco.COCO(annFile)

#print coco.loadAnns(coco.getAnnIds())

print len(coco.getCatIds())
print coco.getAnnIds()[0]

cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
for i in range(len(nms)):
  print nms[i]


#time.sleep(100)
I_w = 1920.0
I_h = 1440.0
#print coco.loadAnns(coco.getAnnIds()[0])
for i in range(len(coco.getAnnIds())):
  #print coco.loadAnns(ids=coco.getAnnIds()[i])[0]['bbox'][0]
  image_id =  coco.loadAnns(ids=coco.getAnnIds()[i])[0]['image_id']
  #print coco.loadAnns(ids=coco.getAnnIds()[i])[0]['image_id']


  x1 = float(coco.loadAnns(ids=coco.getAnnIds()[i])[0]['bbox'][0])
  y1 = float(coco.loadAnns(ids=coco.getAnnIds()[i])[0]['bbox'][1])
  w1 = float(coco.loadAnns(ids=coco.getAnnIds()[i])[0]['bbox'][2])
  h1 = float(coco.loadAnns(ids=coco.getAnnIds()[i])[0]['bbox'][3])
  #print x1,y1,w1,h1
  x = ((x1 + x1 + w1)/2)/I_w
  y = ((y1 + y1 + h1)/2)/I_h
  w = w1 / I_w
  h = h1 / I_h
  #print x,y,w,h

  category_id = coco.loadAnns(ids=coco.getAnnIds()[i])[0]['category_id']
  #print category_id

  #time.sleep(0.01)


  if int(image_id)<100000:
    txt = "/home/dl-linux/coco/images/" + "D2S_" + "%06d.txt" %image_id
  elif int(image_id)<100000000:
    txt = "/home/dl-linux/coco/images/" + "D2S_" + "%08d.txt" %image_id

  with open(txt,'a') as file:
    file.write(str(category_id-1) + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) +  '\n' )
  file.close()
  #time.sleep(5)



"""
plt.imshow(I)
plt.show()

  with open() as file:
    file.write()
  file.close()
"""
