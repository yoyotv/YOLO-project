# Small object detection


## Get started

1. Install darknet
```
git clone https://github.com/pjreddie/darknet.git
cd darknet
make
```

2. Put the cfg folder files  under darknet/cfg

3. Use `set_label_txt.py` to convert original label txt which are under `NWPU VHR-10 dataset/ground truth` into darknet label type
  
4. Put the image and label under the same folder

5. Use `set_img_path.py` to generate training files path txt

## Train

1. Train yolov3 with a pre-train imagenet darknet53 weight

```
./darknet detector train /home/dl-linux/darknet/cfg/obj/obj.data  /home/dl-linux/darknet/cfg/obj/yolov3.cfg /home/dl-linux/darknet/cfg/obj/darknet53.conv.74
```

2. Train yolov3-tiny with a pre-train imagenet yolov3-tiny weight

```
./darknet detector train /home/dl-linux/darknet/cfg/obj/obj.data  /home/dl-linux/darknet/cfg/obj/yolov3-tiny.cfg /home/dl-linux/darknet/cfg/obj/yolov3-tiny.conv.15
```

## Detect

1. yolov3 detect

```
./darknet detector test /home/dl-linux/darknet/cfg/obj/obj.data /home/dl-linux/darknet/cfg/obj/yolov3_deploy.cfg /home/dl-linux/darknet/backup/yolov3.backup /home/dl-linux/darknet/data/NWPU_VHR-10/307.jpg
```

2. yolov3-tiny detect
```
./darknet detector test /home/dl-linux/darknet/cfg/obj/obj.data /home/dl-linux/darknet/cfg/obj/yolov3-tiny_deploy.cfg /home/dl-linux/darknet/backup/yolov3-tiny.backup /home/dl-linux/darknet/data/NWPU_VHR-10/201.jpg -thresh 0.001

```


## Notice

1. The detect result only show the objection which confidence is higher than 0.25, set the threshold if you wanna see all detections.

 ```./darknet detector test /home/dl-linux/darknet/cfg/obj/obj.data /home/dl-linux/darknet/cfg/obj/yolov3-tiny_deploy.cfg /home/dl-linux/darknet/backup/yolov3-tiny.backup /home/dl-linux/darknet/data/NWPU_VHR-10/201.jpg -thresh 0.001```
 
 ## Extract pre-trained weight from yolo weight
 
https://github.com/pjreddie/darknet/issues/1115#issuecomment-420603848
