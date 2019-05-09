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

* It is able to start training from imagenet + coco + voc pretrained weight

NWPU VHR-10 500 pictures for training, 150 for testing.

### yolov3
Iteration : 14651
Average loss : 0.223733

### yolov3-tiny
Iteration : 60356
Average loss : 0.255645

### Train yolov3 with a pre-train imagenet darknet53 weight

```
./darknet detector train /home/dl-linux/darknet/cfg/obj/obj.data  /home/dl-linux/darknet/cfg/obj/yolov3.cfg /home/dl-linux/darknet/cfg/obj/darknet53.conv.74
```

### Train yolov3-tiny with a pre-train imagenet yolov3-tiny weight

```
./darknet detector train /home/dl-linux/darknet/cfg/obj/obj.data  /home/dl-linux/darknet/cfg/obj/yolov3-tiny.cfg /home/dl-linux/darknet/cfg/obj/yolov3-tiny.conv.15
```

## Detect

1. yolov3 detect

```
./darknet detector test /home/dl-linux/darknet/cfg/obj/obj.data /home/dl-linux/darknet/cfg/obj/yolov3_deploy.cfg /home/dl-linux/darknet/backup/yolov3.backup /home/dl-linux/darknet/data/NWPU_VHR-10/515.jpg
```
<img src="https://raw.githubusercontent.com/yoyotv/YOLO-project/master/small_object_detection/figures/yolov3.jpg" >


2. yolov3-tiny detect
```
./darknet detector test /home/dl-linux/darknet/cfg/obj/obj.data /home/dl-linux/darknet/cfg/obj/yolov3-tiny_deploy.cfg /home/dl-linux/darknet/backup/yolov3-tiny.backup /home/dl-linux/darknet/data/NWPU_VHR-10/504.jpg

```
<img src="https://raw.githubusercontent.com/yoyotv/YOLO-project/master/small_object_detection/figures/yolov3-tiny.jpg" >


## Notice

1. The detect result only show the objection which confidence is higher than 0.25, set the threshold if you wanna see all detections.

 ```./darknet detector test /home/dl-linux/darknet/cfg/obj/obj.data /home/dl-linux/darknet/cfg/obj/yolov3-tiny_deploy.cfg /home/dl-linux/darknet/backup/yolov3-tiny.backup /home/dl-linux/darknet/data/NWPU_VHR-10/201.jpg -thresh 0.001```
 
## Extract pre-trained weight from yolo weight
 
https://github.com/pjreddie/darknet/issues/1115#issuecomment-420603848

## Evaluate the performance

```
./darknet detector valid /home/dl-linux/darknet/cfg/obj/obj_tem.data /home/dl-linux/darknet/cfg/obj/yolov3-tiny_deploy.cfg backup/yolov3-tiny.backup
```
Then you are able to find VOC type result under darknet/results.

