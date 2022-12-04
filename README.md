### Project--Mushroom
Recongnizing whether mushroom is poisonous or not.

## :technologist: :student:  User Interface
<br />

>Home page
![Home Page](https://github.com/varunsalunkhe/Project--Mushroom/blob/6fbebefa3f99c69270ee0ae33fa8dc45d2fd9a47/Screenshots/HomePage.png)
>Login Page
![Login Page](https://github.com/varunsalunkhe/Project--Mushroom/blob/6fbebefa3f99c69270ee0ae33fa8dc45d2fd9a47/Screenshots/Login%20page.png)
>Signup Page
![Signup Page](https://github.com/varunsalunkhe/Project--Mushroom/blob/6fbebefa3f99c69270ee0ae33fa8dc45d2fd9a47/Screenshots/Signup%20Page.png)
>Prediction Page
![Prediction Page](https://github.com/varunsalunkhe/Project--Mushroom/blob/6fbebefa3f99c69270ee0ae33fa8dc45d2fd9a47/Screenshots/Prediction%20Model%20page.png)

- This repository represents **" Mushroom Classification "**.
- With the help of this project we can detect whether mushroom with provided specifications is **Poisonous** or not.
  
## 📝 Description
- This implemantation is based on official **Alphapose** repository https://github.com/MVIG-SJTU/AlphaPose 
- In this project we have used **RandomForestClassifier** for classification of mushrooms.

## ⏳ Dataset
- Download the dataset for custom training
- [kaggle link](https://www.kaggle.com/datasets/uciml/mushroom-classification)
- [Repo link](https://github.com/varunsalunkhe/Project--Mushroom/blob/master/mushrooms.csv)

## 🏽‍ Download Object Detection Model
- Download the object detection model manually : **yolov3-spp.weights** file from following Drive Link
- https://drive.google.com/file/d/1h2g_wQ270_pckpRCHJb9K78uDf-2PsPd/view?usp=sharing
- Download the weight file and Place it into **" detector/yolo/data/ "** folder.

##  🏽‍ For Pose Tracking, Download the object tracking model
- For pose tracking, download the object tracking model manually: **" JDE-1088x608-uncertainty "** from following Drive Link 
- https://drive.google.com/file/d/1oeK1aj9t7pTi1u70nSIwx0qNVWvEvRrf/view?usp=sharing
- Download the file and Place it into **" detector/tracker/data/ ".** folder.

## 🏽‍ Download Fast.res50.pt file
- Download the **" fast.res50.pth "** file from following Drive Link 
- https://drive.google.com/file/d/1WrvycZnVWwltSa6cjeTznEFOyNAwHEZu/view?usp=sharing
- Download the file and Place it into **" pretrained_models/ ".** folder.

## :desktop_computer:	Installation

### :hammer_and_wrench: Requirements
* Python 3.5+
* Cython
* PyTorch 1.1+
* torchvision 0.3.0+
* Linux
* GCC<6.0, check https://github.com/facebookresearch/maskrcnn-benchmark/issues/25

## :gear: Setup
1. Install PyTorch :-
```bash
$ pip3 install torch==1.1.0 torchvision==0.3.0

```
2. Install :-
```bash
$ export PATH=/usr/local/cuda/bin/:$PATH

```
```bash
$ export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:$LD_LIBRARY_PATH

```
```bash
$ pip install cython

```
```bash
$ sudo apt-get install libyaml-dev

```
```bash
$ python setup.py build develop --user

```
```bash
$ python -m pip install Pillow==6.2.1

```
```bash
$ pip install -U PyYAML

```
## 🎯 Inference demo
1. Testing with **Images** ( Put test images in **AlphaPose/examples/demo/** )  :-
```bash
$ python scripts/demo_inference.py --cfg configs/coco/resnet/256x192_res50_lr1e-3_1x.yaml --checkpoint pretrained_models/fast_res50_256x192.pth --indir examples/demo/ --save_img

```
2. Testing with **Video** ( Put test video in **AlphaPose/examples/demo/** )  :-
```bash
$ python scripts/demo_inference.py --cfg configs/coco/resnet/256x192_res50_lr1e-3_1x.yaml --checkpoint pretrained_models/fast_res50_256x192.pth --video examples/demo/3.mp4 --outdir examples/res1 --save_video --gpus 0

```


### :book: Please Go through [Pose_With_Action_HLD2.docx](https://github.com/iNeuron-ai/Pose-with-Action/blob/main/doc/Pose_With_Action_HLD2.docx) for more info.


## Contributors <img src="https://raw.githubusercontent.com/TheDudeThatCode/TheDudeThatCode/master/Assets/Developer.gif" width=35 height=25> 
- Akshay Kumar Prasad	
- Akshay Namdev Kadam	
- Arjun K	
- ATUL KUMAR	
- Deepak Kumar Behera	
- Jerryl Davis	
- Kancharla Bharath Kumar	
- Karthik P	
- Madhavi Patel	
- Mukesh	
- Oinam Bhobendra	
- pamita singh kandari	
- Sameer sudhir Deshmukh	
- Sasidharan M	
- shrinivas kandlikar
