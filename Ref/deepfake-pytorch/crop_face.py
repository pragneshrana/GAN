##################################################################
# This script crop faces from a folder contains many human figures
##################################################################

import sys
import dlib
import cv2
import os
import argparse
import largest_face_detector
import copy

Images_Folder = 'train/personB'
OutFace_Folder = 'train/personB_face/'

Images_Path = os.path.join(os.path.realpath('.'), Images_Folder)
Out_Path = os.path.join(os.path.realpath('.'), OutFace_Folder)

pictures = os.listdir(Images_Path)


# initialize hog + svm based face detector
detector = dlib.get_frontal_face_detector()

# # handle command line arguments
# ap = argparse.ArgumentParser()
# ap.add_argument('-w', '--weights', default='./mmod_human_face_detector.dat',
#                 help='path to weights file')
# args = ap.parse_args()


# # initialize CNN based face detector
# detector = dlib.cnn_face_detection_model_v1(args.weights)

print(pictures)

def rotate(img):
    rows,cols,_ = img.shape
    M = cv2.getRotationMatrix2D((cols, rows ), 0, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst

for f in pictures:


    print('processing image')
    img = cv2.imread(os.path.join(Images_Path,f), cv2.IMREAD_COLOR)
    b, g, r = cv2.split(img)
    img2 = cv2.merge([r, g, b])
    img = rotate(img)

    # f_copy = copy.deepcopy(f)
    # image = largest_face_detector.detect_largest_face(str(Images_Path)+'/'+str(f_copy))
    # cv2.imwrite(OutFace_Folder+f_copy[:-4]+"_large_face.jpg", image)


    print(' processing image 2')
    dets = detector(img, 1)
    print("Number of faces detected: {}".format(len(dets)))

    for idx, face in enumerate(dets):
        # print('face{}; left{}; top {}; right {}; bot {}'.format(idx, face.left(). face.top(), face.right(), face.bottom()))

        left = face.left()
        top = face.top()
        right = face.right()
        bot = face.bottom()
        #print(left, top, right, bot)
        #cv2.rectangle(img, (left, top), (right, bot), (0, 255, 0), 3)
        #print(img.shape)
        crop_img = img[top:bot, left:right]
        #cv2.imshow(f, img)
        #cv2.imshow(f, crop_img)
        print(OutFace_Folder,f[:-4],"_face.jpg")
        cv2.imwrite(OutFace_Folder+f[:-4]+"_face.jpg", crop_img)

        #k = cv2.waitKey(1000)
        #cv2.destroyAllWindows()


