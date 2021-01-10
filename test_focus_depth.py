import cv2
from matplotlib import pyplot as plt
import sys
import os
import time
WIDTH, HEIGHT   = 1280, 720
DEFAULT_DEVICE_PATH = "/dev/video0"
DEVICE_PATH_ROOT = "/dev/video"

if len(sys.argv) > 1:
    id = int(sys.argv[1])
else:
    id = 0    
device_path = DEVICE_PATH_ROOT + str(id)
cap = cv2.VideoCapture(id)
#Check if camera was opened correctly
if not (cap.isOpened()):
    print("Could not open video device", device_path)
    exit()

#Set the resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

#v4l2-ctl -d /dev/video0 -c exposure_auto=1 -c exposure_auto_priority=0 -c exposure_absolute=500

def set_focus_absolute(device_path: str, focus_step: int):
    os.system(f"v4l2-ctl -d {device_path} -c focus_absolute={str(focus_step)}")
    time.sleep(0.1)


# cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
# cap.set(cv2.CAP_PROP_EXPOSURE, 1)
# print(cap.get(cv2.CAP_PROP_EXPOSURE))

need_creating_window = True
# Capture frame-by-frame
FOCUS_STEP_MIN = 0
FOCUS_STEP_MAX = 255
FOCUS_STEP = 5

for focus in range(FOCUS_STEP_MIN,FOCUS_STEP_MAX, FOCUS_STEP):
    set_focus_absolute(device_path, focus)

    ret, frame = cap.read()

    # Display the resulting frame
    
    # cv2.imshow("preview",frame)
    # plt.clf()
    # plt.plot(frame[310,:])
    
    # if need_creating_window:
    #     plt.show(block=False)
    #     need_creating_window = False
    # else:
    #     plt.draw()

    cv2.imwrite(f"shot-{focus}.jpg", frame)
    #print(type(frame), ret)

    sharpness = cv2.Laplacian(frame, cv2.CV_64F).var()
    print(focus, sharpness)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
