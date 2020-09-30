import numpy
import cv2
import cv2.aruco as aruco

WHITE = [255,0,0]
def aruco_gen(id_aruco, num_pixels):
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)     #replace n with no. of bits per pixel and C with the no. of combinations                                                 #select n and C from the list mentioned above
    img = aruco.drawMarker(aruco_dict,id_aruco,num_pixels)
  #  constant= cv2.copyMakeBorder(img,25,25,25,25,cv2.BORDER_CONSTANT,value=WHITE)    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'ArUco ID =4',(180,17), font,0.5,(255,0,255),1,cv2.LINE_AA)
   # cv2.imwrite('arUco4.jpg',constant)
    cv2.imshow('ArUco',img)
    cv2.waitKey(0)
    

    '''
    code here for saving the Aruco image as a "jpg" by following the steps below:
    1. save the image as a colour RGB image in OpenCV color image format
    2. embed a boundary of 25 pixels on all four sides and three channels of the image
    3. save the image as "ArUcoID.jpg" where ID is the digits of id_aruco i.e. if the ID is 26 the name should be: ArUco26.jpg
    4. APIs which are permitted to be used are:
    a. cvtColor
    b. imwrite
    and other OpenCV APIs.
    5. You are permitted to modify n, C and variables id_aruco and num_pixels
    '''
    
    cv2.destroyAllWindows()


if __name__ == "__main__":    
    aruco_gen(4, 400)
    
