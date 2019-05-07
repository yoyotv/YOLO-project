import random


num = list(range(1,650+1))
random.shuffle(num)
print num

with open('/home/dl-linux/small_object/NWPU VHR-10 dataset/train_file_list.txt','a') as file:
  for i in range(1,650+1):
    current_img_path = '/home/dl-linux/darknet/data/NWPU_VHR-10/%03d.jpg\n' %num[i-1]
    file.write(current_img_path)
file.close()






