import cv2
import numpy as np
import h5py
import json
import os

PATH_h5 = 'C:\\Users\\konstantin.savelev\\Desktop\\HSI\\archive (1)\\hsi\\artery.h5'
PATH_IMAGES = 'C:\\Users\\konstantin.savelev\\Desktop\\HSI\\archive (1)\\source\\images\\images\\'
PATH_JSON = 'C:\\Users\\konstantin.savelev\\Desktop\\HSI\\archive (1)\\source\\build_metadata.json'
arr = []

def read_h5(path):
    with h5py.File(PATH_h5, "r") as f:
        a_group_key = list(f.keys())[0]
        data = list(f[a_group_key])
        # print(data)
        ds_arr = f[a_group_key][()]
        print(ds_arr)


# read_h5(PATH_h5)

def read_images(path):
    images = []
    i = 0
    for filename in os.listdir(path):
        img = cv2.imread((os.path.join(path, 'img_' + str(i) + '.png')))
        i += 1
        arr = np.array(img)
        images.append(arr)
    return np.transpose(np.array(images))

# print(read_images(PATH_IMAGES))
# sp.savemat('C:\\Users\\konstantin.savelev\\Desktop\\HSI\\archive (1)\\hsi\\test.mat',{'matrix':read_images(PATH_IMAGES)})

def read_json(path):
    f = open(path)
    data = json.load(f)
    for i in data['wavelengths']:
        print(i)
        arr.append(i)

def save_json():
    with open('C:\\Users\\konstantin.savelev\\Desktop\\HSI\\archive (1)\\hsi\\test.json', 'w') as wr_file:
        json.dump({'wavelengths':arr}, wr_file)



# read_json(PATH_JSON)
# save_json()
