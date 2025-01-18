"""
written by yan li
September 19, 2024

this function is mainly used to create data file,the content of file
is 'image_path,mask,original image,label',
label: # Truth:0, Copy_move:1, Splicing:2, removal:3

"""

import numpy as np
import os
import csv


if __name__ == '__main__':

    root_path = r'E:\tamper_dataset\nist16\NC2016_Test0613'
    mani_path = os.path.join(root_path,'reference\manipulation','NC2016-manipulation-ref.csv')

    rem_cnt,spli_cnt,copy_cnt = 0,0,0
    rem_list,spli_list,copy_list = [],[],[]
    label = '0'
    with open(mani_path,'r') as file:
        data = csv.reader(file)
        for i,line in enumerate(data):
            if i == 0:
                print(line)
                rem_index = line[0].split('|').index('IsManipulationTypeRemoval')
                splice_index = line[0].split('|').index('IsManipulationTypeSplice')
                copy_index = line[0].split('|').index('IsManipulationTypeCopyClone')
                probe_index = line[0].split('|').index('ProbeFileName')
                mask_index = line[0].split('|').index('ProbeMaskFileName')
                basefile_index = line[0].split('|').index('BaseFileName')
            """
                data format: [manipulated image, mask, original image, label]
            """
            # process removal data
            if line[0].split('|')[rem_index] == 'Y':
                rem_cnt += 1
                label = '3'
                rem_list.append([str(line[0].split('|')[probe_index]),
                                 str(line[0].split('|')[mask_index].replace('manipulation','removal')),
                                 str(line[0].split('|')[basefile_index]),
                                 label])

            # process splicing data
            if line[0].split('|')[splice_index] == 'Y':
                spli_cnt += 1
                label = '2'
                spli_list.append([str(line[0].split('|')[probe_index]),
                                 str(line[0].split('|')[mask_index]),
                                 str(line[0].split('|')[basefile_index]),
                                  label])

            # process manipulated data
            if line[0].split('|')[copy_index] == 'Y':
                copy_cnt += 1
                label = '1'
                copy_list.append([str(line[0].split('|')[probe_index]),
                                 str(line[0].split('|')[mask_index]),
                                 str(line[0].split('|')[basefile_index]),
                                    label])

    print(f'removal data count is :{rem_cnt}')
    print(f'splicing data count is :{spli_cnt}')
    print(f'copy data count is :{copy_cnt}')
    #
    # with open(os.path.join(root_path,'NIST16_removal.txt'),'w') as file:
    #     for elem in rem_list:
    #         file.write(','.join(elem)+'\n')
    #
    # with open(os.path.join(root_path,'NIST16_splice.txt'),'w') as file:
    #     for elem in spli_list:
    #         file.write(','.join(elem)+'\n')
    #
    # with open(os.path.join(root_path,'NIST16_copy.txt'),'w') as file:
    #     for elem in copy_list:
    #         file.write(','.join(elem)+'\n')
    
    total_list = rem_list+spli_list+copy_list
    print(f'total data count is : {len(total_list)}')

    import random
    random.seed(42)
    random.shuffle(total_list)

    with open(os.path.join(root_path, 'NIST16_pretrain.txt'), 'w') as file:
        for elem in total_list:
                file.write(','.join(elem)+'\n')

    
    
    '''
    Check if two datasets have duplicated data
    '''
    # validate duplicate data
    # print('removal and splice data duplicate validation')
    # rem_spli_cnt,rem_copy_cnt,spli_copy_cnt = 0,0,0
    # rem_spli_name,rem_copy_name,spli_copy_name = [],[],[]
    # for item in rem_list:
    #     for spli_item in spli_list:
    #         rem_name = os.path.basename(item[1])
    #         spli_name = os.path.basename(spli_item[1])
    #         if rem_name == spli_name:
    #             rem_spli_cnt +=1
    #             rem_spli_name.append(item[1])
    #
    # for item in rem_list:
    #     for copy_item in copy_list:
    #         rem_name = os.path.basename(item[1])
    #         copy_name = os.path.basename(copy_item[1])
    #         if rem_name == copy_name:
    #             rem_copy_cnt +=1
    #             rem_copy_name.append(item[1])
    #
    # for item in spli_list:
    #     for copy_item in copy_list:
    #         spli_name = os.path.basename(item[1])
    #         copy_name = os.path.basename(copy_item[1])
    #         if spli_name == copy_name:
    #             spli_copy_cnt +=1
    #             spli_copy_name.append(item[1])
    #
    # with open(os.path.join(root_path,'duplicate.txt'),'a') as file:
    #     file.write('removal and splicing is duplicate\n')
    #     file.write(','.join(rem_spli_name)+'\n')
    #     file.write('removal and copy is duplicate\n')
    #     file.write(','.join(rem_copy_name)+'\n')
    #     file.write('splicing and copy is duplicate\n')
    #     file.write(','.join(spli_copy_name)+'\n')

    # print(f'removal and splicing is duplicate count is:{rem_spli_cnt}')
    # print(f'removal and copy is duplicate count is:{rem_copy_cnt}')
    # print(f'splicing and copy  is duplicate count is:{spli_copy_cnt}')

    # with open(os.path.join(root_path,'removal.txt'),'r') as file:
    #     dataset = [line.strip().split(',')[1] for line in file]
    #     new_dataset = []
    #     for i in dataset:
    #         if i not in new_dataset:
    #             new_dataset.append(i)
    #     print(len(dataset),len(new_dataset))
    #     if len(dataset) != len(new_dataset):
    #         print('The dataset removal.txt has duplicated data ! ')
    #
    # with open(os.path.join(root_path,'splice.txt'),'r') as file:
    #     dataset = [line.strip().split(',')[1] for line in file]
    #     new_dataset = []
    #     for i in dataset:
    #         if i not in new_dataset:
    #             new_dataset.append(i)
    #     print(len(dataset),len(new_dataset))
    #     if len(dataset) != len(new_dataset):
    #         print('The dataset has duplicated data ! ')



