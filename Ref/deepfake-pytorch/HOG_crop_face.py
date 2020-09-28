# import required packages
import cv2
import dlib
import argparse
import time
import os

Images_Folder = 'train/personB'
OutFace_Folder = 'train/personB_face/'

Images_Path = os.path.join(os.path.realpath('.'), Images_Folder)
Out_Path = os.path.join(os.path.realpath('.'), OutFace_Folder)

pictures = os.listdir(Images_Path)

print(pictures)

for f in pictures:

    # load input image
    image = cv2.imread(os.path.join(Images_Path,f), cv2.IMREAD_COLOR)

    if image is None:
        print("Could not read input image")
        continue
        
    # initialize hog + svm based face detector
    hog_face_detector = dlib.get_frontal_face_detector()


    start = time.time()

    # apply face detection (hog)
    faces_hog = hog_face_detector(image, 1)

    end = time.time()
    print("Execution Time (in seconds) :")
    print("HOG : ", format(end - start, '.2f'))

    # loop over detected faces
    for face in faces_hog:
        x = face.left()
        y = face.top()
        w = face.right() 
        h = face.bottom() 

        # # draw box over face
        # cv2.rectangle(image, (x,y), (w,h), (0,255,0), 2)
        


    start = time.time()

    # write at the top left corner of the image
    # for color identification
    img_height, img_width = image.shape[:2]
    cv2.putText(image, "HOG", (img_width-50,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0,255,0), 2)

    # display output image
    cv2.imshow("face detection with dlib", image)
    cv2.imwrite(OutFace_Folder+f[:-4]+"_face.jpg", image)

    crop_img = image[y:h, x:w]
    cv2.imwrite(OutFace_Folder+f[:-4]+"_face.jpg", crop_img)

    # close all windows
    cv2.destroyAllWindows()