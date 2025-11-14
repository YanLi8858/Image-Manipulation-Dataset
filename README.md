# Image Manipulated Detection Dataset Correction 
 ![Static Badge](https://img.shields.io/badge/python-3.7.0-blue)
 ![GitHub last commit](https://img.shields.io/github/last-commit/YanLi8858/Image-Manipulation-Dataset)
![GitHub License](https://img.shields.io/github/license/YanLi8858/Image-Manipulation-Dataset)
![visitors](https://visitor-badge.laobi.icu/badge?page_id=YanLi8858.Image-Manipulation-Dataset)
 ![GitHub Repo stars](https://img.shields.io/github/stars/YanLi8858/Image-Manipulation-Dataset) 


[[**English version**]](./README.md) | [[**Chinese version**]](./README-zh.md)  


## 1 Introduction

CASIAv1, CASIAv2, COVERAGE, and NIST16 are public datasets for image tampering detection, used for training and testing models. However, there are various issues in these public datasets. This repository mainly addresses these problems. The original datasets of CASIAv1 and CASIAv2 are from [[kaggle link]](https://www.kaggle.com/datasets/sophatvathana/casia-dataset?select=CASIA1), the masks for CASIAv1 are from [[github]](https://github.com/CauchyComplete/casia1groundtruth), and the masks for CASIAv2 are from [[github]](https://github.com/CauchyComplete/casia2groundtruth). The COVERAGE dataset is from [[github]](https://github.com/wenbihan/coverage).


## 2 Dataset Processing Procedure

### 2.1 CASIAv1 
- Case 1: The classification of some image manipulation categories is inaccurate.,e.g., in the image  `[Sp_D_NND_A_nat0054_nat0054_0189.jpg]`, the fourth letter 'D' means 'difference', indicating a splicing manipulation. It should be changed to `[Sp_S_NND_A_nat0054_nat0054_0189.jpg]`, where 'S' means 'same', indicating a copy-move manipulation. A total of 29 images had their manipulation types changed, and 4 images modified their names .  
- Solution:  
Run `./CASIAv1/1_modify_name_casia1.py` to modify the image file names using the file "./casia1groundtruth-master/CASIA 1.0 groundtruth/FileNameCorrection.xlsx" from the [CASIAv1 mask repository](https://github.com/CauchyComplete/casia1groundtruth).  
- Case 2: Some image file names in the "./CASIAv1/Sp" folder do not match corresponding mask file names.  
- Solution:  
Run the `./CASIAv1/2_process_casia_1.py` script to find the unmatched images and save them to  "./73 images process/CASIAv1_no_mask_imgs.txt".  
Run `./CASIAv1/3_capture_and_modify_name_73.py` to modify the image names to match the mask names. A total of 73 images were processed.  
- Case 3:  
The image `Sp_D_NRN_A_sce0011_cha0011_0542.jpg` has no mask and should be deleted.  
- Note:  
Real images: 800, tampered images: 920 (921 images contain 1 image should be deleted).  
The processed dataset can be downloaded from [[Baidu Netdisk]](https://pan.baidu.com/s/1iiIVKMuyNj75b8JFm8IQDA?pwd=pkb7) , extraction code: pkb7.


### 2.2 CASIAv2 

- Case 1: The classification of some image manipulation categories is inaccurate. A total of 99 photos have incorrect transformation operation types, and 42 photos have incorrect names.  
- Solution:  
Run `modify_name_casia2.py` to modify the image file names using the file "./casia2groundtruth-master/Notes/fileNamesCorrection.xlsx" from the [CASIAv2 mask repository](https://github.com/CauchyComplete/casia2groundtruth).  
- Case 2: The resolutions of some images in the image folder  "./casia-dataset/CASIAv2/Tp" are different from corresponding masks.  
- Solution:  
A total of 17 images need to modify their resolutions . For reference, see [[github]](https://github.com/SunnyHaze/IML-Dataset-Corrections/blob/main/README-zh.md)  
- Case 3: Three images without mask
`[Tp_D_NNN_M_B_art00037_nat10103_10108.tif]` <br>
`[Tp_D_NNN_M_N_nat10103_pla10110_10116.tif]` <br>
`[Tp_D_NNN_S_N_nat00042_nat00042_00961.tif]` <br>
Based on the suggestion from @Ephemeral-rose [CASIAv2 Case 3 Solution #2
](https://github.com/YanLi8858/Image-Manipulation-Dataset/issues/2#issue-2893521488), we can avoid deleting the aforementioned three files and instead modify their filenames after download the `CASIAv2.zip` <br>
`[Tp_D_NNN_M_B_art00037_nat10103_10108.tif -> Tp_D_NNN_M_B_art00037_txt10112_10108.tif]`<br>
`[Tp_D_NNN_M_N_nat10103_pla10110_10116.tif -> Tp_D_NNN_M_N_pla10110_nat10103_10116.tif]`<br>
`[Tp_D_NNN_S_N_nat00042_nat00042_00961.tif -> Tp_D_NNN_S_N_nat00042_nat00034_00961.tif]`<br>

- Note:<br>
  Real images: 7491, tampered images: 5123.<br>
  The processed dataset can be downloaded from [[Baidu Netdisk]](https://pan.baidu.com/s/1xlGanuW49gQE3hKvDkhulQ?pwd=c8m2),extraction code: c8m2.


### 2.3 COVERAGE 
- Case: There are 9 images (27 masks) with mismatched resolutions
- Solution: You can refer to [[Github]](https://github.com/SunnyHaze/IML-Dataset-Corrections).
- Note:<br>
  Real image: 100, tampered image: 100<br>
  The processed dataset can be downloaded  from [[Baidu Netdisk]](https://pan.baidu.com/s/1QWdvqoHUe972jV-jBc_7zQ?pwd=x4uh) ,extract code: x4uh .

### 2.4 NIST16 
- Note:<br>
  tampered image: 564<br>
  The processed dataset can be downloaded  from 
[[Baidu Netdisk]](https://pan.baidu.com/s/1XMPZnnrO2lnyMhfvoGqdyA?pwd=yx7w), extract code:  yx7w .

## 3  The click rate statistics of the GitHub repository
If you feel that this repository is helpful to you, please remember to light up the stars 😁😁

Star History

[![Star History Chart](https://api.star-history.com/svg?repos=YanLi8858/Image-Manipulation-Dataset&type=Date)](https://star-history.com/#YanLi8858/Image-Manipulation-Dataset&Date)

<a href="https://info.flagcounter.com/Fp4e"><img src="https://s01.flagcounter.com/count2/Fp4e/bg_FFFFFF/txt_000000/border_CCCCCC/columns_2/maxflags_10/viewers_0/labels_0/pageviews_0/flags_0/percent_0/" alt="Flag Counter" border="0"></a>
