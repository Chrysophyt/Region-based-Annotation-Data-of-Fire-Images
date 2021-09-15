import cv2
import os

IMAGE_FOLDER = 'Video01_GT'
VIDEO_NAME = 'Video01_GT.avi'

images = [img for img in os.listdir(IMAGE_FOLDER) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(IMAGE_FOLDER, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(VIDEO_NAME, 0, 5.0, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(IMAGE_FOLDER, image)))

cv2.destroyAllWindows()
video.release()