import os


folder_path = '/home/dl-linux/coco/tem/'

file = os.listdir(folder_path)

print len(file)

print file[0][1]
for i in range(len(file)):
  current = file[i][:-4]
  with open('/home/dl-linux/darknet/cfg/new/train_file_list.txt','a') as file1:
    file1.write('/home/dl-linux/darknet/data/D2S/' + current + '.jpg' + '\n')
  file1.close()
