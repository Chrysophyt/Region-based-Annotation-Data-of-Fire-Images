import cv2
import os

IMAGE_FOLDER = 'Video12/Video12_GT'
VIDEO_NAME = 'Video12/Video12_GT.avi'
FPS = 30

images = [img for img in os.listdir(IMAGE_FOLDER) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(IMAGE_FOLDER, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(VIDEO_NAME, 0, FPS, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(IMAGE_FOLDER, image)))

cv2.destroyAllWindows()
video.release()