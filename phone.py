import requests
import numpy as np
import cv2
import sys
from imutils import face_utils 
import imutils 

sys.path.append('Module-1')
from voice import *
sys.path.append('Module-2')
from OCR import *
from OCR_Live import *
sys.path.append('Module-3')
from Image_Captioning import *
sys.path.append('Module-4')
from reco import *

url = "http://192.168.253.190:8080///shot.jpg"  # URL for mobile camera feed
mode = 0
count = 0
prev_caption = ""  # Store the previous caption

def capture_frame():
    global count
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    frame = cv2.imdecode(img_arr, -1)
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    frame = imutils.resize(frame, width=350)
    #cv2.putText(frame, "PRESS 'q' TO EXIT", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 3)
    nm = f"Frames/frame{count}.jpg"
    cv2.imwrite(nm, frame)
    count += 1
    return frame, nm

def camera():
    global mode
    global count
    global prev_caption
    
    while True:
        frame, nm = capture_frame()

        if mode == 0:
            voice("Please activate any mode, press 1 for surrounding, press 2 for face recognition, press 3 for OCR ,press 4 for live OCR ,  press 5 for restart")
            mode = 5
        elif mode == 5:
            pass  # Adjust according to your logic
        elif mode == 1:
            caption = predict_caption([nm])
            if caption != prev_caption:  # Check if the new caption is different from the previous one
                voice(caption)
                prev_caption = caption
            
        elif mode == 2:
            recognise(nm)  # Check the function definition
        elif mode == 3:
            # Automatically detect the latest uploaded file in the 'uploads' folder
            upload_folder = 'E:/Project/MAJOR/blind/uploads'
            files = os.listdir(upload_folder)
            if files:
                images = [os.path.join(upload_folder, file) for file in files]
                ocr(images)

                for file in files:
                    os.remove(os.path.join(upload_folder, file))
                mode = 5
            else:
                voice("No file found in the upload folder.")
                mode = 5
        elif mode == 4:
            ocr_live(nm)

        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)

        if key == 49:
            voice("Surrounding Description Mode Activated")
            mode = 1
        elif key == 50:
            voice('Facial Recognition Mode Activated')
            mode = 2
        elif key == 51:
            voice('OCR Mode Activated')
            mode = 3
        elif key == 53:  # Press '5' to stop captioning
            prev_caption = ""  # Reset the previous caption
            voice('Restarted')
            mode = 5
        elif key == 52:
            voice("Live OCR mode activated")
            mode = 4
        elif key == 27 or key == ord('q'):
            break
        
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera()
