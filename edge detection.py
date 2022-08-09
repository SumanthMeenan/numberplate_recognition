import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR'
img = cv2.imread('3.jpg',cv2.IMREAD_COLOR)
img = imutils.resize(img, width=500 )
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.bilateralFilter(gray, 11, 17, 17) 
edged = cv2.Canny(gray, 30, 200) 
cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
img1=img.copy()
cv2.drawContours(img1,cnts,-1,(0,255,0),3)
cv2.imshow("img1",img1)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
screenCnt = None 
img2 = img.copy()
cv2.drawContours(img2,cnts,-1,(255,255,255),3) 
cv2.imshow("img2",img2) 

count=0
idx=7

for c in cnts:
  
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
        if len(approx) == 4: 
                screenCnt = approx
                x,y,w,h = cv2.boundingRect(c) 
                new_img=img[y:y+h,x:x+w]
                cv2.imwrite('./'+str(idx)+'.png',new_img) 
                idx+=1
                break
                    
cv2.drawContours(img,screenCnt, -1, (0, 255, 0), 3)
cv2.imshow("Final image with plate detected",img)

Cropped_loc='7.png' 
cv2.imshow("cropped",cv2.imread(Cropped_loc))
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR"  

text=pytesseract.image_to_string(Cropped_loc,lang='eng') 
print("Number is:" ,text)
cv2.waitKey(0)
cv2.destroyAllWindows() 
