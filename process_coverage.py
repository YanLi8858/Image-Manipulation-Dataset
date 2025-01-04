"""
written by yan li
september 19, 2024

this function is mainly used to create data file,the content of file
is 'image_path,mask,jpg_path,label', if image format is not jpg,
compress image to jpg format and saved to specific dir.

"""

import os
import numpy as np
from PIL import Image
import glob


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

    root_path = r'E:\tamper_dataset\COVERAGE'
    img_dir = os.path.join(root_path,'image')
    mask_dir = os.path.join(root_path,'mask')
    jpg_dir = os.path.join(root_path,'jpg')
    if not os.path.exists(jpg_dir):
        os.makedirs(jpg_dir,exist_ok=True)

    # process tampering data
    img_list = []
    mismatch_cnt = 0
    convert_cnt = 0
    noMask = 0
    label = '1'
    for file in glob.glob(img_dir+'/*t.tif'):

        file = os.path.basename(file)
        # change image format to jpg
        img = Image.open(os.path.join(img_dir,file))
        img.save(jpg_dir+'/'+(file.split('.')[0]+".jpg"), quality=100, subsampling=0)
        convert_cnt += 1

        maskfile = '{}forged.tif'.format(file.rsplit('.')[0][:-1])
        if not os.path.isfile(mask_dir+'/'+maskfile):
            noMask += 1
            print('-'*50)
            print(f'the image {file} does not exist mask')
            print('-' * 50)
            continue

        if valid_image_shape(img_dir+'/'+file,mask_dir+'/'+maskfile):
            img_list.append(','.join(['image/'+file,
                                        'mask/'+maskfile,
                                        'jpg/'+file.split('.')[0]+".jpg",
                                        label]))
        else:
            mismatch_cnt += 1


    print(f'total match tampering data is {len(img_list)}')
    print(f'mismatch count: {mismatch_cnt}')
    print(f'image does not have Mask count:{noMask}')
    print(f'convert image format from tif to jpg count : {convert_cnt} ')

    # with open(os.path.join(root_path,'coverage_tamper.txt'),'w') as file:
    #     file.write('\n'.join(img_list)+'\n')

    ## process authentic data
    aut_img_list = []
    convert_cnt = 0
    label = '0'
    for file in glob.glob(img_dir + '/*.tif'):
        file = os.path.basename(file)
        if file.split('.')[0][-1] is not 't':
            # change image format to jpg
            img = Image.open(os.path.join(img_dir, file))
            img.save(jpg_dir + '/' + (file.split('.')[0] + ".jpg"), quality=100, subsampling=0)
            convert_cnt += 1
            aut_img_list.append(','.join(['image/' + file,
                                            'none',
                                            'jpg/' + file.split('.')[0] + ".jpg",
                                            label]))


    print(f'total match authentic data is {len(aut_img_list)}')
    print(f'convert authentic image format from tif to jpg count : {convert_cnt} ')

    # with open(os.path.join(root_path,'coverage_authentic.txt'), 'w') as file:
    #     file.write('\n'.join(aut_img_list))





