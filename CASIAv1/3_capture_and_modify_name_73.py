import os
import shutil


if __name__ == '__main__':
    root = r'E:\tamper_dataset\casia-dataset\CASIAv1'
    mask_dir = os.path.join(root, 'CASIA 1.0 groundtruth')
    img_dir = os.path.join(root, 'Sp')

    """
    step1: To select images in CASIAv1_no_mask_imgs.txt(74 images)[generated by process_casia_1.py] 
    and copy them from Sp folder to no_mask_imgs"""
    # if not os.path.exists(r'E:\tamper_dataset\casia-dataset\CASIAv1\no_mask_imgs'):
    #     os.makedirs(r'E:\tamper_dataset\casia-dataset\CASIAv1\no_mask_imgs',exist_ok=True)
    # with open(os.path.join(root,'CASIAv1_no_mask_imgs.txt')) as file:
    #     lines = [line.strip() for line in file.readlines()]  # 74
    #     for line in lines:
    #         shutil.copy(os.path.join(root,'Sp',line),os.path.join(root,'no_mask_imgs',line))

    """
    step2: To ensure that there are no corresponding images for some masks 
    and extract these masks to the folder no_img_masks
    """
    # if not os.path.exists(r'E:\tamper_dataset\casia-dataset\CASIAv1\no_img_masks'):
    #     os.makedirs(r'E:\tamper_dataset\casia-dataset\CASIAv1\no_img_masks',exist_ok=True)
    # images = []
    # for img in os.listdir(img_dir):
    #     images.append(os.path.splitext(img)[0])
    # masks = []
    # for folder in [mask_dir+'/CM',mask_dir+'/Sp']:
    #     for mask in os.listdir(folder):
    #         masks.append(mask)
    # for mask in masks:
    #     if os.path.splitext(mask)[0][:-3] not in images:
    #         subdir = os.path.join(mask_dir,'Sp') if mask[3:4]=='D' else os.path.join(mask_dir,'CM')
    #         shutil.copy(os.path.join(subdir,mask),os.path.join(root,'no_img_masks',mask))
    #         with open(os.path.join(root,'CASIAv1_no_img_masks.txt'),'a') as file:
    #             file.write(mask+'\n')

    """
    step3: modify image name to match mask name
    mis_images:74 and mis_masks:73
    """
    # os.makedirs(r'E:\tamper_dataset\casia-dataset\CASIAv1\rename_img',exist_ok=True)
    # cnt = 0
    # mask_names = []
    # with open(os.path.join(root, 'CASIAv1_no_img_masks.txt')) as file:
    #     lines = [line.strip() for line in file.readlines()]
    #     for line in lines:
    #         mask_names.append(os.path.splitext(line)[0][:-3]) # Sp_D_NNN_A_cha0039_nat0019_0320_gt.png -> Sp_D_NNN_A_cha0039_nat0019_0320
    #
    # with open(os.path.join(root,'CASIAv1_no_mask_imgs.txt')) as file:
    #     lines = [line.strip() for line in file.readlines()]
    #     for img in lines:
    #         img_n,ext = os.path.splitext(img)
    #         # Sp_D_NNN_A_nat0019_cha0039_0320 -> Sp_D_NNN_A_cha0039_nat0019_0320
    #         img_modify = img_n[:11] + img_n[19:26] + '_' + img_n[11:18] + img_n[26:] + ext
    #         if os.path.splitext(img_modify)[0] in mask_names:
    #             try:
    #                 shutil.copy(os.path.join(img_dir,img),os.path.join(root,'rename_img',img_modify)) # for backup
    #                 shutil.copy(os.path.join(img_dir,img), os.path.join(img_dir, img_modify))
    #             except :
    #                 print("{} can not copy ".format(img))
    #             try:
    #                 os.remove(os.path.join(img_dir, img))
    #             except:
    #                 print('Do not delete file: {} '.format(img))
    #         else:
    #             print('{} can not exist in mask folder '.format(img))
    #             cnt += 1
    #             with open(root+os.sep+'img_mismatch_mask.txt','a') as file:
    #                 file.write(img+'\n')
    # print(cnt)

    """
    step4: utilize rename_img folder to select 1 mismatch masks from CASIAv1_no_img_masks.txt
    and save it 
    """
    # rename_dir = os.path.join(root,'rename_img')
    # img_list = []
    # for img in os.listdir(rename_dir):
    #     img_list.append(os.path.splitext(img)[0])
    # mismatch_cnt = 0
    # mismatch_mask = []
    # with open(r"E:\tamper_dataset\casia-dataset\CASIAv1\CASIAv1_no_img_masks.txt") as file:
    #     mask_lines = [line.strip() for line in file.readlines()]
    #     for line in mask_lines:
    #         if os.path.splitext(line)[0][:-3] not in img_list:
    #             mismatch_mask.append(line)
    #             mismatch_cnt += 1
    #             with open(r'E:\tamper_dataset\casia-dataset\CASIAv1\mask_mismatch_img.txt','a') as file:
    #                 file.write('mask_name: '+line+'\n')
    #     print('cnt：{}'.format(mismatch_cnt))
    """ 
    step5: modify [Sp_D_NRN_A_ant0063_nat0065_0443.jpg] -> [Sp_D_NRN_A_nat0063_nat0065_0443.jpg]
    for matching [ Sp_D_NRN_A_nat0063_nat0065_0443_gt.png] """
    # img = os.path.join(img_dir,'Sp_D_NRN_A_ant0063_nat0065_0443.jpg')
    # if os.path.isfile(img):
    #     shutil.copy(img,os.path.join(img_dir,'Sp_D_NRN_A_nat0063_nat0065_0443.jpg'))
    #     try:
    #         os.remove(img)
    #     except:
    #         print('{} can not delete!'.format(img))
    """
    step6 : delete image [Sp_D_NRN_A_sce0011_cha0011_0542.jpg]    
    """
    img = os.path.join(img_dir,'Sp_D_NRN_A_sce0011_cha0011_0542.jpg')
    if os.path.isfile(img):
        try:
            os.remove(img)
        except:
            print('{} can not delete!'.format(img))
