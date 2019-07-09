# Furniture Removal

Download [ADE20K](https://groups.csail.mit.edu/vision/datasets/ADE20K/) dataset 

## Prepare an input image
### 1. Define configurations

The configurations are in `config.py`
* **img_name:** image name
* **considered_obj:** a list of considered objects to be removed

### 2. Load segment files

```
python load_segment.py
```

Outputs are stored in `loaded_segmentation` and should be the following files:
* om.npy
* oi.npy
* pi.npy
* pm.npy
* objects.csv
* parts.csv

### 3. Extract segments and create masks

```
python extract_segment.py
```

Example of extrated segments
<p align="center">
  <kbd>
    <img src="https://github.com/Skydddoogg/furniture-removal/blob/master/extracted_segments/ADE_train_000002418.0.png" height="220" width="400">
  </kbd>
  <kbd>
  <img src="https://github.com/Skydddoogg/furniture-removal/blob/master/extracted_segments/ADE_train_0000024112.0.png" height="220" width="400" border="5px">
  </kbd>
</p>

The extracted segments will be utilised to create masks as an example below.

<p align="center">
  <img src="https://github.com/Skydddoogg/furniture-removal/blob/master/network_input/ADE_train_00000241.png" height="220" width="400">
</p>

This image will be fed to [image inpainting network](https://arxiv.org/abs/1804.07723).

## Feed the prepared input to the network

Release soon...

---

This project is the main part of my research internship at [VISTEC](https://www.vistec.ac.th/home/) under the supervision of Prof. [Supasorn Suwajanakorn](https://www.supasorn.com/).
