import cv2
import numpy as np

img = cv2.imread('Image4.jpg')
font = cv2.FONT_HERSHEY_COMPLEX
img2 = img[:415,:415,:]         ## This for telling the no. of rows and coloumns to show 
cv2.imshow('im',img2)
img[:415,:415,:] = [255,255,255] 
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	#definig the range of red color
red_lower=np.array([0,70,50],np.uint8)
red_upper=np.array([8,255,255],np.uint8)

	#defining the Range of Blue color
blue_lower=np.array([110,50,50],np.uint8)
blue_upper=np.array([130,255,255],np.uint8)
	
	#defining the Range of yellow color
green_lower=np.array([20,100,100],np.uint8)
green_upper=np.array([60,255,255],np.uint8)

	#finding the range of red,blue and yellow color in the image
red=cv2.inRange(hsv, red_lower, red_upper)
blue=cv2.inRange(hsv,blue_lower,blue_upper)
green=cv2.inRange(hsv,green_lower,green_upper)
	
	#Morphological transformation, Dilation  	
kernal = np.ones((5 ,5), "uint8")

red=cv2.dilate(red, kernal)
res=cv2.bitwise_and(img, img, mask = red)

blue=cv2.dilate(blue,kernal)
res1=cv2.bitwise_and(img, img, mask = blue)

green=cv2.dilate(green,kernal)
res2=cv2.bitwise_and(img, img, mask = green)    


	#Tracking the Red Color
(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,0),25)
print (len(contours))
M = cv2.moments(contours[0])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print ("Centroid = ", cx, ", ", cy)
cv2.putText(img,("hello"),(cx,cy),font,1,255)
			
	#Tracking the Blue Color
(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,0),25)
print (len(contours))
M = cv2.moments(contours[0])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print ("Centroid = ", cx, ", ", cy)
cv2.putText(img,("hello"),(cx,cy),font,1,255)



    	#Tracking the yellow Color
(_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,0),25)
print (len(contours))
M = cv2.moments(contours[0])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print ("Centroid = ", cx, ", ", cy)
cv2.putText(img,("hello"),(cx,cy),font,1,255)


cv2.imshow('ima',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
