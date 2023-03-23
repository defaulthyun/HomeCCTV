import cv2
import mediapipe as mp
import pandas as pd
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

col = ['nose_x', 'nose_y', 'nose_z', 'left_shoulder_x', 'left_shoulder_y', 'left_shoulder_z','right_shoulder_x','right_shoulder_y', 'right_shoulder_z',
      'left_elbow_x','left_elbow_y',' left_elbow_z','right_elbow_x','right_elbow_y','right_elbow_z',
       'left_wrist_x','left_wrist_y','left_wrist_z','right_wrist_x','right_wrist_y','right_wrist_z',
       'left_hip_x','left_hip_y','left_hip_z', 'right_hip_x', 'right_hip_y','right_hip_z','left_knee_x','left_knee_y','left_knee_z',
       'right_knee_x','right_knee_y','right_knee_z','left_ankle_x','left_ankle_y','left_ankle_z','right_ankle_x','right_ankle_y','right_ankle_z']

# data = pd.DataFrame(columns=col)

data = pd.DataFrame()
for i in range(1,11):
  # 0 ~ 4523
  img1 = f'project_3\project_3\predict_frame\predict ({i}).png'
    #train_images/frame_0.jpg
  IMAGE_FILES = [img1]    
  BG_COLOR = (192, 192, 192)  # 회색
  with mp_pose.Pose(
          static_image_mode=True,
          model_complexity=2,
          enable_segmentation=True,
          min_detection_confidence=0.5) as pose:
      for idx, file in enumerate(IMAGE_FILES):
          image = cv2.imread(file)
          image_height, image_width, _ = image.shape
          # 처리 전 BGR 이미지를 RGB로 변환합니다.
          results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
          if not results.pose_landmarks:
              continue

          datas = []
          for n in range(0,39,3):
            cate = col[n][:-2].upper()
            datas.append([results.pose_landmarks.landmark[mp_pose.PoseLandmark[cate]].x])
            datas.append([results.pose_landmarks.landmark[mp_pose.PoseLandmark[cate]].y])
            datas.append([results.pose_landmarks.landmark[mp_pose.PoseLandmark[cate]].z])
          data = data.append(pd.Series(datas), ignore_index=True)

data.to_csv('predict.csv', index=False)