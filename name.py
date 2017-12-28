import os
import sys
root_folder = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(root_folder))
dataset_path = '/home/catidog/work/rename/Results_subset_new/'

seq_names = os.listdir(dataset_path)
for item in seq_names :
    seq_name = item
    seq_nums_path = os.path.join('Results_subset_new' , item)+'/'

    seq_nums = os.listdir(seq_nums_path)


    for nums in seq_nums:
        seq_num = nums
        images_path =  os.path.join('Results_subset_new', item,  seq_num)+'/'
        images = os.listdir(images_path)

        for i in images :
            oldname = images_path+i
            i=i.split('.')[0]
            #i=i.split('_')[1]
            i=int(i)
            if i<=10:
                newname =  images_path+str(i)+'.png'
            elif i>100 :
                newname = images_path + str(i)+'.png'
            else:
                newname = images_path +str(i)+'.png'
            os.rename(oldname,newname)
            print(newname)