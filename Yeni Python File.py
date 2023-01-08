import cv2
import numpy as np
import imutils
 


# Grab the image
while True:
    img = cv2.imread("foto.jpg")
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #maskeleme-- kirmizi secmesi icin.
    ki_alt=np.array([0,120,100]) #arraye cevirdik  #arttirarak 
    ki_ust=np.array([10,255,255])
    
    mask=cv2.inRange(hsv,ki_alt,ki_ust)  #search high and low hsv val of red bu alan ici deger
    
    cnts=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts) #kirmizi alan bulan konturler
    
    sayac=0
    for c in cnts:
        alan=cv2.contourArea(c) #kontur alani
        print("alan",alan)
        if alan>1000:
            sayac+=1
        
        cv2.drawContours(img,[c],-1,(0,255,0),3) #kontur ciz
        
    print("kırmızı semsiye sayısı :",sayac)
        
        
        
    key=cv2.waitKey(1)
    if key==27:
        break
    
    cv2.imshow("img",img)
    cv2.waitKey(1)



