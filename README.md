[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5893854.svg)](https://doi.org/10.5281/zenodo.5893854)


# Region-based Annotation Data of Fire Images for Intelligent Surveillance System

This Annotation Dataset was used on

**Real-Time Fire Detection Based on Color-Motion Feature for Video Surveillance System**\
Wahyono, Faisal Dharma Adhinata, Gamma Kosala, Agus Harjoko, Andi Dharmawan, and Kang Hyun Jo\
[MDPI Fire](https://www.mdpi.com/2571-6255/5/1/23), 2022. 

This work was supported by the Ministry of Education Culture, Research and Technology, Republic of Indonesia under World Class Research (WCR) Grant 111/E4.1/AK.04.PT/2021 and 4506/UN1/DITLIT/DIT-LIT/PT/2021.  

## Overview
This dataset provides fire segmentation data on 12 common fire classification video. This dataset was obtained by per-frame, manual hand annotation with total of 2,684 annotated frames.

The original raw video data was obtained from [A. E. Çetin. “Computer Vision Based Fire Detection Dataset.” 2014](http://signal.ee.bilkent.edu.tr/VisiFire/Demo/FireClips). We provide seamless integration of the original data (which are not included in this repository) to ours, with [download_vid2img.py](./Scripts/download_vid2img.py) script, that download, then extract the original dataset, and modified it to fit our environment settings. To open our annotation project files, we use [VIA (VGG Image Annotator)](https://www.robots.ox.ac.uk/~vgg/software/via/) version 2.0.10.

## Fire Video Segmentation VisiFire Video origin and specification used.

| Fire   Segmentation Video | Visifire Dataset          | FPS | Total Frame |
|---------------------------|---------------------------|-----|-------------|
| Video01                   | controlled1.avi           | 15  | 260         |
| Video02                   | controlled2.avi           | 15  | 246         |
| Video03                   | controlled3.avi           | 15  | 208         |
| Video04                   | forest1.avi               | 15  | 200         |
| Video05                   | forest2.avi               | 15  | 245         |
| Video06                   | forest3.avi               | 15  | 255         |
| Video07                   | forest4.avi               | 15  | 219         |
| Video08                   | forest5.avi               | 15  | 216         |
| Video09                   | fBackYardFire.avi | 2   | 241         |
| Video10                   | forestfire.avi            | 15  | 218         |
| Video11                   | fire1.avi         | 5   | 236         |
| Video12                   | 40m_PanFire_20060824.avi  | 29.97  | 140         |

## Download VisiFire Dataset
> python ./Scripts/download_vid2img.py

This command will download the original videos with parameters in the table above, and extract them into each video folder in the dataset automatically.

## Usage Example
| VisiFire Video (A. E. Çetin, 2014) | Fire Segmentation Video Ground Truth      | Fire Detection Based on Color-Motion (Wahyono et al., 2021) |
| ----------- | ----------- | ----------- |
| ![Alt Text](./README/Video01.gif)      | ![Alt Text](./README/Video01_GT.gif)       | ![Alt Text](./README/Video01_ML.gif)       |
| ![Alt Text](./README/Video02.gif)      | ![Alt Text](./README/Video02_GT.gif)       | ![Alt Text](./README/Video02_ML.gif)       |
| ![Alt Text](./README/Video04.gif)      | ![Alt Text](./README/Video04_GT.gif)       | ![Alt Text](./README/Video04_ML.gif)       |
| ![Alt Text](./README/Video05.gif)      | ![Alt Text](./README/Video05_GT.gif)       | ![Alt Text](./README/Video05_ML.gif)       |

## Requirements

- Tested on 64-bit Python 3.8
- Python Lib: PIL, OpenCV2, tqdm, numpy.

## Citations
If you use the following dataset please do not forget to cite the following:
> Wahyono, Dharmawan, A., Harjoko, A., Chrystian, & Adhinata, F. D. (2022). Region-based Annotation Data of Fire Images for Intelligent Surveillance System. Data in Brief, 107925. doi:10.1016/j.dib.2022.107925
> 
> Wahyono, Harjoko A, Dharmawan A, Adhinata FD, Kosala G, Jo K-H. Real-Time Forest Fire Detection Framework Based on Artificial Intelligence Using Color Probability Model and Motion Feature Analysis. Fire. 2022; 5(1):23. https://doi.org/10.3390/fire5010023
> 
> A. E. Çetin. “Computer Vision Based Fire Detection Dataset.” 2014

or in BibTeX
```
@article{WAHYONO2022107925,
title = {Region-based Annotation Data of Fire Images for Intelligent Surveillance System},
journal = {Data in Brief},
pages = {107925},
year = {2022},
doi = {https://doi.org/10.1016/j.dib.2022.107925},
author = {Wahyono and Andi Dharmawan and Agus Harjoko and  Chrystian and Faisal Dharma Adhinata}
}
@Article{fire5010023,
AUTHOR = {Wahyono and Harjoko, Agus and Dharmawan, Andi and Adhinata, Faisal Dharma and Kosala, Gamma and Jo, Kang-Hyun},
TITLE = {Real-Time Forest Fire Detection Framework Based on Artificial Intelligence Using Color Probability Model and Motion Feature Analysis},
JOURNAL = {Fire},
VOLUME = {5},
YEAR = {2022},
NUMBER = {1},
ARTICLE-NUMBER = {23},
URL = {https://www.mdpi.com/2571-6255/5/1/23},
ISSN = {2571-6255},
DOI = {10.3390/fire5010023}
}
```
