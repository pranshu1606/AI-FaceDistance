#we use the basics of a camera first find the focal length f = (w*d)/W

import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0) #this is the videocam object
detector = FaceMeshDetector(maxFaces=1)

while True:
    sucess, img = cap.read()
    img, faces = detector.findFaceMesh(img,draw = True)

    if faces:
        face = faces[0]
        pointLeft = face[145]  #exact point of the eye
        pointRight = face[374]  #exact point of other eye

        cv2.circle(img,pointLeft,5,(255,0,255), cv2.FILLED)
        cv2.circle(img,pointRight,5,(255,0,255), cv2.FILLED)
        cv2.line(img,pointLeft,pointRight,(0,200,0),3)
        w, _ = detector.findDistance(pointLeft,pointRight)
        #finding the focal length
       # f = (w*d)/W
        W = 6.3  #width of the eyes
        #Finding distance
        f = 840
        d = (W*f)/w
        print(d)

        cvzone.putTextRect(img, f"Depth: {d}cm", (face[10][0]-75,face[10][1]-50),scale=2)



    cv2.imshow("Image",img)
    cv2.waitKey(1)