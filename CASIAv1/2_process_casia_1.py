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


def process_file(img_dir,mask_dir,valid=False):

    img_list = []
    mismatch_cnt = 0
    convert_cnt = 0
    noMask = 0
    label = '0'
    mask_folder = [mask_dir+'/CM',mask_dir+'/Sp']
    Masks = []
    nomask_list = []
    for folder in mask_folder:
        for mask in os.listdir(folder):
            Masks.append(mask)

    print(f'Masks count is: {len(Masks)}')

    for file in os.listdir(img_dir):

        if file[3:4] == 'S':
            mask_subdir = mask_dir+'/CM'
        else:
            mask_subdir = mask_dir+'/Sp'

        if file.lower().endswith('.jpg'):
            mask_file = os.path.splitext(file)[0]+'_gt.png'        # avoid missing [Sp_D_NNN_A_ani0099_ani0100.0288_gt.png]
            if mask_file not in Masks:
                noMask += 1
                nomask_list.append(file)
                print('-'*50)
                print(f'the image {file} does not exist mask')
                print('-' * 50)
                continue
            label = '1' if file[3:4] == 'S' else '2'  # Truth:0, Copy_move:1, Splicing:2
            if valid:
                if not valid_image_shape(img_dir+'/'+file,mask_subdir+'/'+mask_file):
                    mismatch_cnt += 1
                    # with open('./mismatch.txt','a') as file:
                    #     file.write(mask_file+'\n')
                    continue
            img_list.append(['CASIAv1/Sp/' + file,
                              'CASIAv1/CASIA1.0_Groundtruth/CM'+mask_file if file[3:4] == 'S'
                              else 'CASIAv1/CASIA1.0_Groundtruth/Sp'+mask_file,
                              label])

    print(f'total match data is {len(img_list)}')
    print(f'mismatch count: {mismatch_cnt}')
    print(f'image does not have Mask count:{noMask}')
    print(f'convert image format from tif to jpg count : {convert_cnt} ')
    # with open(r'E:\tamper_dataset\casia-dataset\CASIAv1\CASIAv1_no_mask_imgs.txt','w') as file :
    #     for elem in nomask_list:
    #         file.write(elem+'\n')

    return img_list

def valid_image_shape(img_path,mask_path):
    """
    The function is used to verify whether the shape
    of the image matches the shape of the mask
    """
    img = np.array(Image.open(img_path))
    mask = np.array(Image.open(mask_path))
    if img.shape[0] == mask.shape[0] and img.shape[1] == mask.shape[1]:
        return True
    else:
        print(f'The image {os.path.basename(img_path)} is not matched the mask {os.path.basename(mask_path)}')
        print(f'image shape is {img.shape[0]}x{img.shape[1]},mask shape is {mask.shape[0]}x{mask.shape[1]}')
        return False


if __name__ == '__main__':

    #process CASIAv1 tampering data
    root_path = r'E:\tamper_dataset\casia-dataset'
    tamp_dir = os.path.join(root_path,'CASIAv1\Sp')
    mask_dir = os.path.join(root_path,'CASIAv1','CASIA 1.0 groundtruth')
    img_list = process_file(tamp_dir,mask_dir)
    # with open(os.path.join(root_path,'CASIAv1','CASIAv1_tamper.txt'),'w') as file :
    #     for elem in img_list:
    #         file.write(','.join(elem)+'\n')
    print('Finish tampering data process!')
    #
    # #process CASIAv1 authentic data
    # aut_dir = os.path.join(root_path,'CASIAv1/Au')
    # aut_img_list = []
    # label = '0'
    # for img in os.listdir(aut_dir):
    #     aut_img_list.append(','.join(['CASIAv1/Au/'+img,
    #                                   'None',
    #                                   label,]))
    # print(f'total authentic data is {len(aut_img_list)}') #
    # with open(os.path.join(root_path,'CASIAv1','CASIAv1_authentic.txt'),'w') as file :
    #     file.write('\n'.join(aut_img_list))
    #
    # print('Finish authentic data process!')


    '''validate the image in CASIAv1 whether is contained in CASIAv2 or not'''
    # root_path = r'E:\tamper_dataset\casia-dataset'
    # tamp_casia1_dir = os.path.join(root_path, 'CASIAv1\Sp')
    # tamp_casia2_dir = os.path.join(root_path, 'CASIAv2\Tp')
    # casia_1_list = []
    # for img in os.listdir(tamp_casia1_dir):
    #     casia_1_list.append(os.path.splitext(img)[0][11:])
    #
    # casia_2_list = []
    # for img in os.listdir(tamp_casia2_dir):
    #     casia_2_list.append(os.path.splitext(img)[0][13:])
    #
    # duplicate_count = 0
    # dup_name = []
    # for name in casia_1_list:
    #     if name in casia_2_list:
    #         dup_name.append(name)
    #         duplicate_count += 1
    #
    # print(f'duplicate name is:{dup_name}')
    # print(f'duplicate count is {duplicate_count}')

