import cv2

count = 0

vidcap = cv2.VideoCapture(f'project_3\train\cam1.avi')
 
# 영상기준 0.4 초에 들어가는 Frame수
print(vidcap.get(cv2.CAP_PROP_FPS))
vid_fps = 0.4 / ( 1 / float(vidcap.get(cv2.CAP_PROP_FPS)))
print(vid_fps)
while(vidcap.isOpened()):
    ret, image = vidcap.read()
    
    if(int(vidcap.get(1)) % vid_fps  == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        cv2.imwrite("project_3/images/frame%d.jpg" % count, image)
        print('Saved frame%d.jpg' % count)
        count += 1

vidcap.release()