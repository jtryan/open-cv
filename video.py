#use webcam

import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 1st webcam load filename for file
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
while True:
    ret, frame = cap.read()
    # mods
    gray = cv2.cvtColor(frame, cv2COLOR_BGR2GRAY)
    out.write(frame)
    # show 2 frames original and the modified one.
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
