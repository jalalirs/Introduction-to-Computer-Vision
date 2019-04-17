import os
import timeit
import cv2
from skimage import io as io
import face_recognition as fr
import numpy as np
import pickle
from tqdm import tqdm
from sklearn import datasets, svm, metrics
from PIL import Image, ImageOps

def main():
    gender_data = list()
    for fn in tqdm(os.listdir('nottingham')):
        try:
            if fn.split('.')[1] == 'gif':
                # print('Processing {}'.format(fn))
                gender_label = fn[0]
                img = np.asarray(Image.open(os.path.join('nottingham', fn)).convert('RGB'))
                face_embedding = fr.face_encodings(img)
                if len(face_embedding) != 1:
                    # print('Above one face in an image, skip..')
                    continue
                single_data = list()
                single_data.append(face_embedding[0])
                single_data.append(gender_label)
                single_data.append(os.path.join('nottingham', fn))
                gender_data.append(single_data)
            else:
                continue
        except:
            raise
            continue

    print('Saving as a pkl file')
    with open('gender_data.pkl','wb') as f:
        pickle.dump(gender_data, f)
    print('Finished')


if __name__ == '__main__':
    main()



