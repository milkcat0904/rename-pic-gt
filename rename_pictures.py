import os
import sys
root_folder = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.abspath(root_folder))
dataset_path = '/home/catidog/work/rename/subset_new/'

seq_names = os.listdir(dataset_path)
for item in seq_names :

    seq_nums_path = os.path.join('subset_new' , item)+'/'

    seq_nums = os.listdir(seq_nums_path)


    for nums in seq_nums:

        images_path =  os.path.join('subset_new', item, nums, 'images')+'/'
        images = os.listdir(images_path)

        for i in images :
            oldname = images_path+i
            i=i.split('.')[0]
            #i=i.split('_')[1]
            i=int(i)
            if i<=10:
                newname =  images_path+'0000'+str(i)+'.jpg'
            elif i>100 :
                newname = images_path + '00' + str(i)+'.jpg'
            else:
                newname = images_path + '000'+str(i)+'.jpg'
            os.rename(oldname,newname)
            print(newname)


