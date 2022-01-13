import cv2
import face_recognition

image_to_detect=cv2.imread('/Users/rahulmaddula/Downloads/images/testing/img4.jpeg')
#cv2.imshow("test",image_to_detect)
all_face_loactions=face_recognition.face_locations(image_to_detect,model="hog")
print("There are {} face(s) in this image".format(len(all_face_loactions)))
for index,current_face_loaction in enumerate(all_face_loactions):
         top_pos,right_pos,bottom_pos,left_pos=current_face_loaction
         print("Found face {} at top:{},right:{},bottom:{},left{}".format(index+1,top_pos,right_pos,bottom_pos,left_pos))
         current_face_image=image_to_detect[top_pos:bottom_pos,left_pos:right_pos]
         cv2.rectangle(image_to_detect,(left_pos,top_pos), (right_pos,bottom_pos), (0,0,255),2)
         cv2.imshow("Face Detected",image_to_detect)
    

          