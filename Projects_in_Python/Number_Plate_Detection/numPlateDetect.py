import cv2
frameWidth = 700
frameHeight = 500
# number plate cascade
numPlateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
# Threshold for area
minArea = 200
color = (255,0,255)
# video on using webcam
cap = cv2.VideoCapture(0)
cap.set(3, 700) #setting width
cap.set(4, 500) #setting height
cap.set(10,100) #setting brightness
count = 0

while True:
    success, img = cap.read()
    # converting image to gray scale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detecting the number plates
    numberPlates = numPlateCascade.detectMultiScale(imgGray, 1.1, 10)
    # drawing a rectangle and writing "Number plate" around all the detected number plates
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area >minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img,"Number Plate",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgNP = img[y:y+h,x:x+w]
            cv2.imshow("NP", imgNP)
    # Display the output image in the "Result" window
    cv2.imshow("Result", img)
    # Press "s" to save the image
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("NumberPlates/NumPlate_"+str(count)+".jpg",imgNP)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count +=1
        cv2.waitKey(1)
    # Press "q" to escape 
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
# close all windows
cv2.destroyAllWindows()
  