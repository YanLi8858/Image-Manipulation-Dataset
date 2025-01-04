"""
written by yan li
september 19, 2024

this function is mainly used to create data file,the content of file
is 'image_path,mask,jpg_path,label', if image format is not jpg,
compress image to jpg format and saved to specific dir.

"""
import os
from PIL import Image
import numpy as np


def _dump_file(img_dir,mask_dir,jpg_dir):

    img_list = []
    mismatch_cnt = 0
    convert_cnt = 0
    noMask = 0
    label = '0'
    sp_cnt, cp_cnt = 0, 0
    for file in os.listdir(img_dir):

        # if file in ['Tp_D_NRD_S_B_ani20002_nat20042_02437.tif']:
        #     continue  # stupid file
        mask_file = os.path.splitext(file)[0]+'_gt.png'
        if not os.path.isfile(mask_dir+'/'+mask_file):
            noMask += 1
            print('-'*50)
            print(f'the image {file} does not exist mask')
            print('-' * 50)
            continue
        label = '1' if file[3:4] == 'S' else '2'  # Truth:0, Copy_move:1, Splicing:2
        if file[3:4] == 'S':
            cp_cnt += 1
        else:
            sp_cnt += 1
        if file.lower().endswith('.jpg'):
            if valid_image_shape(img_dir+'/'+file,mask_dir+'/'+mask_file):
                img_list.append(['CASIAv2/Tp/'+file,
                                 'CASIAv2/CASIA2.0_Groundtruth/'+mask_file,
                                 'CASIAv2/Tp/'+file,
                                 label])
            else:
                mismatch_cnt += 1
        else:

            if not file.lower().endswith('.tif'):
                continue
            # change image format to jpg
            # img = Image.open(os.path.join(img_dir,file))
            # img.save(jpg_dir+'/'+(os.path.splitext(file)[0]+".jpg"), quality=100, subsampling=0)
            convert_cnt += 1
            if valid_image_shape(img_dir+'/'+file,mask_dir+'/'+mask_file):
                img_list.append(['CASIAv2/Tp/'+file,
                                 'CASIAv2/CASIA2.0_Groundtruth/'+mask_file,
                                 'CASIAv2/jpg/'+os.path.splitext(file)[0]+".jpg",
                                 label])
            else:
                mismatch_cnt += 1

    print(f'total match data is {len(img_list)}')
    print(f'mismatch count: {mismatch_cnt}')
    print(f'image does not have Mask count:{noMask}')
    print(f'convert image format from tif to jpg count : {convert_cnt} ')
    print(f'copy-move count: {cp_cnt}, splice count: {sp_cnt}')

    return img_list

def valid_image_shape(img_path,mask_path):
    img = np.array(Image.open(img_path))
    mask = np.array(Image.open(mask_path))
    if img.shape[0] == mask.shape[0] and img.shape[1] == mask.shape[1]:
        return True
    else:
        print(f'The image {os.path.basename(img_path)} is not matched the mask {os.path.basename(mask_path)}')
        print(f'image shape is {img.shape[0]}x{img.shape[1]},mask shape is {mask.shape[0]}x{mask.shape[1]}')
        return False


if __name__ == '__main__':

    #process CASIAv2 tampering data
    root_path = r'E:\tamper_dataset\casia-dataset'
    tamp_dir = os.path.join(root_path,'CASIAv2/Tp')
    mask_dir = os.path.join(root_path,'CASIAv2','CASIA2.0_Groundtruth')
    jpg_dir = os.path.join(root_path,'CASIAv2','jpg')
    if not os.path.exists(jpg_dir):
        os.makedirs(jpg_dir,exist_ok=True)

    img_list = _dump_file(tamp_dir,mask_dir,jpg_dir) #5102


    # with open(os.path.join(root_path,'CASIAv2','CASIAv2_tamper.txt'),'w') as file :
    #     for elem in img_list:
    #         file.write(','.join(elem)+'\n')

    print('Finish tampering data process!')
    #
    #
    # #process CASIAv2 authentic data
    # aut_dir = os.path.join(root_path,'CASIAv2/Au')
    # jpg_dir  = os.path.join(root_path,'CASIAv2/Au_jpg')
    # aut_img_list = []
    # label = '0'
    # if not os.path.exists(jpg_dir):
    #     os.makedirs(jpg_dir,exist_ok=True)
    #
    # for img in os.listdir(aut_dir):
    #     if not img.lower().endswith('jpg'):
    #         if not img.lower().endswith('bmp'):
    #             print(f'image format is not jpg or bmp {img}')
    #             continue
    #
    #         i = Image.open(os.path.join(aut_dir,img))
    #         i.save(os.path.splitext(img)[0]+'.jpg', quality=100, subsampling=0)
    #         aut_img_list.append(','.join(['CASIAv2/Au/'+img,
    #                                       'none',
    #                                       'CASIAv2/Au_jpg/'+os.path.splitext(img)[0]+'.jpg',
    #                                       label,]))
    #     else:
    #         aut_img_list.append(','.join(['CASIAv2/Au/'+img,
    #                                       'none',
    #                                       'CASIAv2/Au/'+img,
    #                                       label,]))
    #
    # print(f'total authentic data is {len(aut_img_list)}') #7491
    # with open(os.path.join(root_path,'CASIAv2','CASIAv2_authentic.txt'),'w') as file :
    #     file.write('\n'.join(aut_img_list))
    #
    # print('Finish authentic data process!')



    ## train_valid_split for tamper data
    # import random
    #
    # random.seed(42)
    # root_path = r'E:\tamper_dataset\casia-dataset\CASIAv2'
    # with open(os.path.join(root_path,'CASIAv2_tamper.txt'),'r') as file:
    #     data = [line.strip() for line in file]
    #
    # random.shuffle(data)
    # with open(os.path.join(root_path,'CASIAv2_tamper_train.txt'),'w') as file:
    #     file.write('\n'.join(data[:-400]))
    # with open(os.path.join(root_path,'CASIAv2_tamper_valid.txt'),'w') as file:
    #     file.write('\n'.join(data[-400:]))


    ##train_valid_split for authentic data
    # with open(os.path.join(root_path,'CASIAv2_authentic.txt'),'r') as file:
    #     data = [line.strip() for line in file]
    #
    # random.shuffle(data)
    # with open(os.path.join(root_path,'CASIAv2_authentic_train.txt'),'w') as file:
    #     for item in data[:-400]:
    #         print(type(item))
    #         file.write(item+'\n')
    #
    # with open(os.path.join(root_path,'CASIAv2_authentic_valid.txt'),'w') as file:
    #     file.write('\n'.join(data[-400:]))





