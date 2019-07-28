# Furniture Removal

Download [ADE20K](https://groups.csail.mit.edu/vision/datasets/ADE20K/) dataset 

## Requirements

Install the dependencies of this project as listed in `requirements_network.txt` and `requirements_preprocess.txt`.

## Prepare input
### 1. Define configuration

The configuration is in `config.py`
* **considered_obj:** a list of considered objects to be removed

### 2. Extract segments and create masks

Follow steps in `extract_segment.ipynb`

## Feed the prepared input to the network

Follow steps in `prediction.ipynb`

---

This is the project of my research internship at school of Information Science and Technology (IST), [VISTEC](https://www.vistec.ac.th/home/) under the supervision of Prof. [Supasorn Suwajanakorn](https://www.supasorn.com/).
