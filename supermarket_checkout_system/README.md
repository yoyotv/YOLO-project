# Supermarket checkout system


## Get started

1. Install AlexeyAB darknet
```
git clone https://github.com/AlexeyAB/darknet.git
cd darknet
make
```

2. Put the cfg/supermarket folder files  under darknet/cfg

3. Put the backup/supermarket/weights under backup

## Training 

Go to darknet folder

1. Use `pycocoDemo.py` to convert original coco format label into darknet format label 

    1.1. Go to https://github.com/cocodataset/cocoapi.git and install the coco api
  
    1.2. Put the training image under coco/images
  
    1.3. Put `pycocoDemo.py` under PythonAPI and run `python pycocoDemo.py`
  
    1.4. The darknet format label will be generated under coco/images

2. Create an folder named D2S under /darknet/data/

3. Copy all files (images and label.txt) to coco/images/D2S

4. Run

```
./detector train 
```

## Activate the system

Right now we are under supermarknet folder

```
sh run.sh
```
1. The system will read the image in the test_image, you may change the ipout image in "run.sh" line 4.

2. Darknet engine will apply YOLOv3 to predict the locationa and the class of the input image, then save the result in "current record" folder which named "predictions.txt"

3. System will use "calculate.py" to read the predictions and calculate the total price of image. (You may revise the price list in "calculate.py")

4. The final price will be printed on the command window and saved with the prediction in a txt file and saved under records with a format Year_Month_Date_Hour:Minute:Second.txt.




