import cv2
import numpy as np


print("Package imported")
# img read
'''
img = cv2.imread("Resources/lena.png")


cv2.imshow("Output",img)
cv2.waitKey(0)'''
# video code
'''
cap = cv2.VideoCapture("Resources/test_video.mp4")
while True:
    success,img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break'''

# camera detection webcam
'''
cap = cv2.VideoCapture(0)  # 0  to capture by camera
cap.set(3, 640)  # 3 = id no 3 and 640 width
cap.set(4, 480)  # 4= id no 4 480 is height
cap.set(10, 100)  # 10= id no 1o for brightness 100

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break'''
# basic functions
'''
img = cv2.imread("Resources/lena.png")
kernal = np.ones((5,5),np.int8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,200,200)
imgDilation = cv2.dilate(imgCanny,kernal,iterations=1)
imgerodded = cv2.erode(imgDilation,kernal,iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("canny Image",imgCanny)
cv2.imshow("Dilation Image",imgDilation)
cv2.imshow("erosion Image",imgerodded)
cv2.waitKey(0)
'''
# Resizing
'''
img = cv2.imread("Resources/lena.png")
print(img.shape)
imgResize = cv2.resize(img,(300,250))#in open cv function width comes first then the height
print(imgResize.shape)
cv2.imshow("Resize image",imgResize)
cv2.imshow("image",img)

cv2.waitKey(0)
'''
# Croping
'''
img = cv2.imread("Resources/lena.png")
print(img.shape)
imgCropped = img[0:170,20:175]#height comes first and then the width
cv2.imshow("before img",img)
cv2.imshow("Cropped img",imgCropped)
print(imgCropped.shape)

cv2.waitKey(0)
'''
# Shapes and text
'''
img = np.zeros((512,512,3),np.uint8)
#img[200:300,100:500] = 255,0,0#comment first 78 line and next 79 line to see different result
#img[:] = 255,0,0
print(img.shape)
cv2.line(img,(0,0),(300,300),(0,0,255),3)
#cv2.line(img,(0,0)initials,img.shape[height : weidth :channel]
#refer video to see this part https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=10s 40:50 time stramp
cv2.imshow("Image",img)
cv2.waitKey(0)
'''
# wrap perspective
'''
img = cv2.imread("Resources/Cards.jpg")

width , height = 250,350

pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[height,0],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Warp Image",imgOutput)

cv2.waitKey(0)
'''
# joining images
'''
verticle stack and horizontal stack
refer video to see this part https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=10s 50:13 time stramp
'''
# color detection
'''
refer video to see this part https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=10s 56:36 time stramp

'''
# counters and shap detection
# face dectection
'''
cap = cv2.VideoCapture(1)# 0  to capture by camera
cap.set(3,1366)# 3 = id no 3 and 640 width
cap.set(4,768)# 4= id no 4 480 is height
cap.set(10,500)# 10= id no 1o for brightness 100


while True:
    success,img = cap.read()
    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
      #  cv2.putText(img,"Aditya",(x.y-5),cv2.Font_HERSHEY_COMPLEX_SMALL,1,(255,0,255),1)
        cv2.imshow("video",img)
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
     '''       '''
cap = cv2.VideoCapture(0)# 0  to capture by camera
cap.set(3,640)# 3 = id no 3 and 640 width
cap.set(4,480)# 4= id no 4 480 is height
cap.set(10,100)# 10= id no 1o for brightness 100


while True:
    success,img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break'''
