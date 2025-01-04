"""
written by yan li
September 19, 2024

this function is mainly used to create data file,the content of file
is 'image_path,mask,jpg_path,label', if image format is not jpg,
compress image to jpg format and saved to specific dir.
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

            # process manipulation data
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

    test_ratio=0.2
    train_set = total_list[:-int(len(total_list)*test_ratio)]   # 452
    test_set = total_list[-int(len(total_list)*test_ratio):]    # 112
    print(f'finetune train count is : {len(train_set)}')
    print(f'finetune test count is : {len(test_set)}')
    with open(os.path.join(root_path, 'NIST16_finetune_train.txt'), 'w') as file:
        for elem in train_set:
                file.write(','.join(elem)+'\n')
    with open(os.path.join(root_path, 'NIST16_finetune_test.txt'), 'w') as file:
        for elem in test_set:
                file.write(','.join(elem)+'\n')
    
    
    '''verify if the file exists in the folder'''
    # with open(os.path.join(root_path, 'NIST16_removal.txt'), 'r') as file:
    #     mask_data = [line.strip().split(',')[1] for line in file]
    #     mani_data = [line.strip().split(',')[0] for line in file]
    #     for item in mask_data:
    #         if not os.path.exists(os.path.join(root_path, item)):
    #             print(f'removal mask does not exist {item}')
    #     for item in mani_data:
    #         if not os.path.exists(os.path.join(root_path, item)):
    #             print(f'removal image does not exist {item}')
    #
    # with open(os.path.join(root_path, 'NIST16_splice.txt'), 'r') as file:
    #     mask_data = [line.strip().split(',')[1] for line in file]
    #     mani_data = [line.strip().split(',')[0] for line in file]
    #     for item in mask_data:
    #         if not os.path.exists(os.path.join(root_path, item)):
    #             print(f'splice mask does not exist {item}')
    #     for item in mani_data:
    #         if not os.path.exists(os.path.join(root_path, item)):
    #             print(f'splice image does not exist {item}')
    #
    # with open(os.path.join(root_path, 'NIST16_copy.txt'), 'r') as file:
    #     mask_data = [line.strip().split(',')[1] for line in file]
    #     mani_data = [line.strip().split(',')[0] for line in file]
    #     for item in mask_data:
    #         if not os.path.exists(os.path.join(root_path, item)):
    #             print(f'copy mask does not exist {item}')
    #     for item in mani_data:
    #         if not os.path.exists(os.path.join(root_path, item)):
    #             print(f'copy image does not exist {item}')


    # '''split dataset for train 50%（325） ,valid 20%（79） and test 30%（160）'''
    # import random
    # random.seed(42)
    # random.shuffle(rem_list)
    # random.shuffle(spli_list)
    # random.shuffle(copy_list)
    # with open(os.path.join(root_path, 'NIST16_test.txt'), 'w') as file:
    #     for elem in rem_list[-60:]:
    #         file.write(','.join(elem)+'\n')
    # 
    #     for elem in spli_list[-60:]:
    #         file.write(','.join(elem)+'\n')
    # 
    #     for elem in copy_list[-40:]:
    #         file.write(','.join(elem)+'\n')
    # 
    # rem_valid_size = int(len(rem_list[:-60])*0.2)
    # spli_valid_size = int(len(spli_list[:-60])*0.2)
    # copy_valid_size = int(len(copy_list[:-40])*0.2)
    # print("valid data from rem,spli,copy count: ",rem_valid_size,spli_valid_size,copy_valid_size)
    # with open(os.path.join(root_path, 'NIST16_valid.txt'), 'w') as file:
    #     for elem in rem_list[-60-rem_valid_size:-60]:
    #         file.write(','.join(elem)+'\n')
    # 
    #     for elem in spli_list[-60-spli_valid_size:-60]:
    #         file.write(','.join(elem)+'\n')
    # 
    #     for elem in copy_list[-40-copy_valid_size:-40]:
    #         file.write(','.join(elem)+'\n')
    # 
    # with open(os.path.join(root_path, 'NIST16_train.txt'), 'w') as file:
    #     for elem in rem_list[:-60-rem_valid_size]:
    #         file.write(','.join(elem)+'\n')
    # 
    #     for elem in spli_list[:-60-spli_valid_size]:
    #         file.write(','.join(elem)+'\n')
    # 
    #     for elem in copy_list[:-40-copy_valid_size]:
    #         file.write(','.join(elem)+'\n')


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



    '''
    make dataset from removal folder
    '''
    # rem_path = os.path.join(root_path, r'reference\removal', 'NC2016-removal-ref.csv')
    #
    # rem_cnt,spli_cnt,copy_cnt = 0,0,0
    # rem_list,spli_list,copy_list = [],[],[]
    # with open(rem_path,'r') as file:
    #     data = csv.reader(file)
    #     for i,line in enumerate(data):
    #         if i == 0:
    #             print(line)
    #             rem_index = line[0].split('|').index('IsManipulationTypeRemoval')
    #             splice_index = line[0].split('|').index('IsManipulationTypeSplice')
    #             copy_index = line[0].split('|').index('IsManipulationTypeCopyClone')
    #             probe_index = line[0].split('|').index('ProbeFileName')
    #             mask_index = line[0].split('|').index('ProbeMaskFileName')
    #             basefile_index = line[0].split('|').index('BaseFileName')
    #
    #         # process removal data
    #         if line[0].split('|')[rem_index] == 'Y':
    #             rem_cnt += 1
    #             rem_list.append([str(line[0].split('|')[probe_index]),
    #                              str(line[0].split('|')[mask_index]),
    #                              str(line[0].split('|')[basefile_index])])
    #         # process splicing data
    #         if line[0].split('|')[splice_index] == 'Y':
    #             spli_cnt += 1
    #             spli_list.append([str(line[0].split('|')[probe_index]),
    #                              str(line[0].split('|')[mask_index]),
    #                              str(line[0].split('|')[basefile_index])])
    #         # process manipulation data
    #         if line[0].split('|')[copy_index] == 'Y':
    #             copy_cnt += 1
    #             copy_list.append([str(line[0].split('|')[probe_index]),
    #                              str(line[0].split('|')[mask_index]),
    #                              str(line[0].split('|')[basefile_index])])
    #
    # print(f'removal data count is :{rem_cnt}')
    # print(f'splicing data count is :{spli_cnt}')
    # print(f'copy data count is :{copy_cnt}')
    #
    # with open(os.path.join(root_path,'removal.txt'),'w') as file:
    #     for elem in rem_list:
    #         file.write(','.join(elem)+'\n')
    #
    # with open(os.path.join(root_path,'splice.txt'),'w') as file:
    #     for elem in spli_list:
    #         file.write(','.join(elem)+'\n')
    #
    # with open(os.path.join(root_path,'copy.txt'),'w') as file:
    #     for elem in copy_list:
    #         file.write(','.join(elem)+'\n')



    # import pandas as pd
    #
    # df  = pd.read_csv(r'E:\tamper_dataset\nist16\NC2016_Test0613\manipulate_create\copy.txt',sep=',')
    # df.to_excel(r'E:\tamper_dataset\nist16\NC2016_Test0613\manipulate_create\copy.xlsx',index=False)


