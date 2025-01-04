# Image Manipulated Detection Dataset Correction 
## 1 简介
CASIAv1 、CASIAv2、COVERAGE、NIST16 作为图像篡改检测的公开数据集，用于训练和测试模型。然而，公开数据集中存在不同情况的问题，本仓库主要解决这些问题，原始数据集CASIAv1 和 CASIAv2来自[[kaggle link]](https://www.kaggle.com/datasets/sophatvathana/casia-dataset?select=CASIA1)，CASIAv1的mask来自[[github]](https://github.com/CauchyComplete/casia1groundtruth)，CASIAv2的mask来自[[github]](https://github.com/CauchyComplete/casia2groundtruth)。
COVERAGE数据集来自[[github]](https://github.com/wenbihan/coverage)。


## 2 数据集处理过程

### 2.1 CASIAv1
- 情况1：部分图像操作类别分类不准确，例如，`Sp_D_NND_A_nat0054_nat0054_0189.jpg`，图像名称中第4位的字母'D'含义difference，表示splicing操作，转换成`Sp_S_NND_A_nat0054_nat0054_0189.jpg`,'S'含义same，表示copy-move操作。总共转换操作类型照片29张，更改名字照片4张。
- 解决方案：
运行`1_modify_name_casia1.py`，通过使用 CASIAv1的mask仓库中的文件".\casia1groundtruth-master\CASIA 1.0 groundtruth\FileNameCorrection.xlsx"修改图像文件名称。
- 情况2：图像库中的"casia-dataset\CASIAv1\Sp"的部分图像没有对应的mask名称。
- 解决方案：
运行`2_process_casia_1.py`脚本，查找出不匹配图像并且存入".\73 images process\CASIAv1_no_mask_imgs.txt"。
运行`3_capture_and_modify_name_73.py`修改图像名称匹配mask名称。处理73张图片。
- 情况3：
`Sp_D_NRN_A_sce0011_cha0011_0542.jpg` 没有掩码，删除该图像。
- 提示：
真实图像：800，篡改图像：920(921张图片删除1张图片)。
处理后的数据集，可以从[百度网盘](
https://pan.baidu.com/s/1iiIVKMuyNj75b8JFm8IQDA?pwd=pkb7 ) 提取码: pkb7 下载。


### 2.2 CASIAv2
- 情况1：部分图像操作类别分类不准确，总共转换操作类型照片99张，更改名字照片42张。
- 解决方案：
运行`modify_name_casia2.py`，通过使用 CASIAv2的mask仓库中的文件".\casia2groundtruth-master\Notes\fileNamesCorrection.xlsx"修改图像文件名称。
- 情况2：图像文件夹中的".\casia-dataset\CASIAv2\Tp"的部分图像分辨率与对应名称的掩码分辨率不同。
- 解决方案：
一共17张图像需要修改分辨率，参考[github](https://github.com/SunnyHaze/IML-Dataset-Corrections/blob/main/README-zh.md)
- 情况3：
`Tp_D_NNN_M_B_art00037_nat10103_10108.tif` 
`Tp_D_NNN_M_N_nat10103_pla10110_10116.tif`
`Tp_D_NNN_S_N_nat00042_nat00042_00961.tif`没有掩码，可以删除这些图像。
- 提示：
真实图像：7491，篡改图像：5123(其中3张图像没有掩码)。
处理后的数据集，可以从[百度网盘]( https://pan.baidu.com/s/1xlGanuW49gQE3hKvDkhulQ?pwd=c8m2 ) 提取码: c8m2 下载。

### 2.3 COVERAGE 
- 情况：有9张图像(27张mask)分辨率不匹配
- 解决方案：可以参考[[github]](https://github.com/SunnyHaze/IML-Dataset-Corrections)。
- 提示：
真实图像：100，篡改图像：100
处理后的数据集，可以从[百度网盘](通过百度网盘分享的文件：https://pan.baidu.com/s/1QWdvqoHUe972jV-jBc_7zQ?pwd=x4uh 
) 提取码：x4uh 下载。
### 2.4 NIST16 
- 提示：
真实图像：0，篡改图像：564
处理后的数据集，可以从[百度网盘](https://pan.baidu.com/s/1XMPZnnrO2lnyMhfvoGqdyA?pwd=yx7w 
) 提取码：yx7w 下载。