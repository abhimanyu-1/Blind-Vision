import cv2
from simple_facerec import SimpleFacerec
import sys
sys.path.append('../Module-1')
from voice import *
sys.path.append('../')

sfr = SimpleFacerec()
sfr.load_encoding_images("Module-4/images/")
#sys.path.append('../')
#print("abcd")
def recognise(frame):
    frame = cv2.imread(frame, cv2.IMREAD_COLOR)
    face_locations, names = sfr.detect_known_faces(frame)
    for name in names:
        print(name)
        voice(name)
