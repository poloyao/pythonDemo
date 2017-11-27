
import cv2
import face_recognition_models
# face_recognition 死活就是安装不上啊
# 卡在了cmake上了啊 
# c++都装了啊，就是按不上啊
video_capture = cv2.video_capture(0)
obama_image = face_recognition_models.load