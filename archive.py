import cv2
import numpy as np
import json

PATH_JSON = 'C:\\Users\\konstantin.savelev\\Desktop\\HSI\\archive\\source\\build_metadata.json'
PATH = 'C:\\Users\\konstantin.savelev\\Desktop\\HSI\\archive\\hsi\\tablets_copy.mat'
video_name = 'C:\\Users\\konstantin.savelev\\Desktop\\HSI\\archive\\source\\source_tablet_9.avi'

def read_video(path):
    cap = cv2.VideoCapture(path)
    while cap.isOpened():
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0XFF == ord('f'):
            break

    cap.release()
    cv2.destroyAllWindows()

# read_video(video_name)

def print_video_nparr(path):
    cap = cv2.VideoCapture(path)
    all = []
    i = 0
    while cap.isOpened() and i < 1000:
        ret, frame = cap.read()
        arr = np.array(frame)
        all.append(arr)
        i += 1
    return np.array(all)

# print(np.transpose(print_video_nparr(video_name)))
# sp.savemat('C:\\Users\\konstantin.savelev\\Desktop\\HSI\\archive\\hsi\\test.mat',{'matrix':np.transpose(print_video_nparr(video_name))})

# mat = sp.loadmat(PATH)
# print(mat)




arr = []
def read_json(path):
    f = open(path)
    data = json.load(f)
    for i in data['wavelengths']:
        print(i)
        arr.append(i)

def save_json():
    with open('C:\\Users\\konstantin.savelev\\Desktop\\HSI\\archive\\hsi\\test.json', 'w') as wr_file:
        json.dump({'wavelengths':arr}, wr_file)



# read_json(PATH_JSON)
# save_json()

