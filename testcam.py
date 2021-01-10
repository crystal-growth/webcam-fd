import cv2
from matplotlib import pyplot as plt
import sys


WIDTH, HEIGHT   = 1280, 720
#WIDTH, HEIGHT   = 352, 288


if len(sys.argv) > 1:
    id = int(sys.argv[1])
else:
    id = 0    
cap = cv2.VideoCapture(id)
#Check if camera was opened correctly
if not (cap.isOpened()):
    print("Could not open video device")
    exit()

#Set the resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)

#v4l2-ctl -d /dev/video0 -c exposure_auto=1 -c exposure_auto_priority=0 -c exposure_absolute=500

# cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
# cap.set(cv2.CAP_PROP_EXPOSURE, 1)
# print(cap.get(cv2.CAP_PROP_EXPOSURE))

need_creating_window = True
# Capture frame-by-frame
while(True):
    ret, frame = cap.read()

    # Display the resulting frame
    
    cv2.imshow("preview",frame)
    plt.clf()
    plt.plot(frame[310,:])
    
    if need_creating_window:
        plt.show(block=False)
        need_creating_window = False
    else:
        plt.draw()

#    cv2.imwrite("outputImage.jpg", frame)
    #print(type(frame), ret)

    sharpness = cv2.Laplacian(frame, cv2.CV_64F).var()
    print(sharpness)
    #Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
