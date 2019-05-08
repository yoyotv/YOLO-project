import os
from PIL import Image
import time
import numpy as np



for i in range(1,650+1):
  current_label_path = '/home/dl-linux/small_object/NWPU VHR-10 dataset/ground truth/%03d.txt' %i
  current_img_path = '/home/dl-linux/small_object/NWPU VHR-10 dataset/positive image set/%03d.jpg' %i
  current_label_txt_path = '/home/dl-linux/small_object/NWPU VHR-10 dataset/label/%03d.txt' %i

  current_img = Image.open(current_img_path)
  current_img_w = float(current_img.size[0])
  current_img_h = float(current_img.size[1])

  with open(current_label_path) as file:
    all_lines=file.readlines()
    file.close()

  bounding_box_numbers = len(all_lines)
  for j in range(bounding_box_numbers):
    tem = all_lines[j].split(',')
    print tem
    x1 =  float(tem[0][1:])
    y1 =  float(tem[1][:-1])
    x2 =  float(tem[2][1:])
    y2 =  float(tem[3][:-1])
    class_label = int(tem[4])

    x = ((x1 + x2)/2.0)/current_img_w
    y = ((y1 + y2)/2.0)/current_img_h
    w = (abs(x2 - x1))/current_img_w
    h = (abs(y2 - y1))/current_img_h

    print x
    print y
    print w
    print h
    print class_label

    with open(current_label_txt_path,'a') as file:
      file.write(str(class_label-1) + ' ' + str(x) + ' ' + str(y) + ' ' + str(w) + ' ' + str(h) + '\n' )
    file.close()

  #time.sleep(5)



  


