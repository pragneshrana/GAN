import cv2
import os
import time
import matplotlib.pyplot as plt

Video_Path = 'me.mp4'
video_Path = os.path.join(os.path.realpath('.'), Video_Path)
save_path = os.path.join(os.path.realpath('.'), './train/personB/')


cap = cv2.VideoCapture(video_Path)
n=0
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
frame_width = int(cap.get(3))
frame_height =  int(cap.get(4))
out = cv2.VideoWriter('~/Git/GAN/Ref/deepfake-pytorch/train/personA/liu_out.avi', fourcc, 10, (frame_width, frame_height),isColor=False)
while (cap.isOpened()) and n<100:
    ret, frame = cap.read()
    # frame = frame.reshape(frame.shape[1],frame.shape[0],3)
    save_images = os.path.join(save_path, str(n)+'.jpg')

    #Resizing the image ......

    #percent by which the image is resized
    scale_percent = 50

    #calculate the 50 percent of original dimensions
    width = 960
    height = 540

    # dsize
    dsize = (width, height)

    # resize image
    output = cv2.resize(frame, dsize)

    cv2.imwrite(save_images, output) #......change


    # n = n + 1
    if ret==True:
        # out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    n = n +1
    print(n)
cap.release()
out.release()
cv2.destroyAllWindows()

# # Check if camera opened successfully
# if (cap.isOpened() == False):
#     print("Unable to read camera feed")
#
# # Default resolutions of the frame are obtained.The default resolutions are system dependent.
# # We convert the resolutions from float to integer.
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
#
# # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
# out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
#
# while (True):
#     ret, frame = cap.read()
#
#     if ret == True:
#
#         # Write the frame into the file 'output.avi'
#         out.write(frame)
#
#         # Display the resulting frame
#         cv2.imshow('frame', frame)
#
#         # Press Q on keyboard to stop recording
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     # Break the loop
#     else:
#         break
#
#     # When everything done, release the video capture and video write objects
# cap.release()
# out.release()
#
# # Closes all the frames
# cv2.destroyAllWindows()
