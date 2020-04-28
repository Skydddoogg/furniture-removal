# FurNet: A Deep-Learning-Based Framework for Removing Furniture Objects in Room Image
This is a mini project during my research internship at school of Information Science and Technology (IST), [VISTEC](https://www.vistec.ac.th/home/), under the supervision of Prof. [Supasorn Suwajanakorn](https://www.supasorn.com/).

## About FurNet
<p align="center">
  <img src="https://github.com/Skydddoogg/furniture-removal/blob/master/project_images/furnet1.png" width="300"/>
</p>

The literature [Image Inpainting for Irregular Holes Using Partial Convolutions](https://arxiv.org/abs/1804.07723) shows that image inpainting network can be utilised for object removal task. Hence, an image inpainting network is used in this project.

In this project partial convolutions for image inpainting with pre-trained weight on ImageNet is used to perform the furniture removal task. Technically, to remove furniture objects in an image, a mask image of furniture objects in the image needs to be created first. The mask image and the original image will be fed into the network, and the network will then output the image with no the furniture objects which are represented in the mask image.

## Dataset

Download [ADE20K](https://groups.csail.mit.edu/vision/datasets/ADE20K/) dataset 

## Requirements

Install the dependencies of this project as listed in `requirements_network.txt` and `requirements_preprocess.txt`.

## Try FurNet
### 1. Prepare input
#### 1.1. Define configuration

The configuration is in `config.py`
* **considered_obj:** a list of considered objects to be removed

#### 1.2. Extract segments and create masks

Follow steps in `extract_segment.ipynb`

### 2. Feed the prepared input to the network

Follow steps in `prediction.ipynb`
