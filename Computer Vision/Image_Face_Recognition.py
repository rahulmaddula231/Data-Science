import cv2
import face_recognition
original_image=cv2.imread('/Users/rahulmaddula/Downloads/code/Images/testing/trump-modi.jpg')
modi_image=face_recognition.load_image_file('/Users/rahulmaddula/Downloads/code/Images/samples/modi.jpg')
modi_face_encodings=face_recognition.face_encodings(modi_image)[0]

trump_image=face_recognition.load_image_file('/Users/rahulmaddula/Downloads/code/Images/samples/trump.jpg')
trump_face_encodings=face_recognition.face_encodings(trump_image)[0]
know_face_encodings=[modi_face_encodings,trump_face_encodings]
know_face_names=["Narendra Modi","Donald Trump"]
image_to_recognize=face_recognition.load_image_file('/Users/rahulmaddula/Downloads/code/Images/testing/trump-modi.jpg')
all_face_locations=face_recognition.face_locations(image_to_recognize,model="hog")
all_face_encodings=face_recognition.face_encodings(image_to_recognize,all_face_locations )
print("There are {} face(s) in this image".format(len(all_face_locations)))
for current_face_location,current_face_encoding in zip(all_face_locations,all_face_encodings):
    top_pos,right_pos,bottom_pos,left_pos=current_face_location
    print("Found face at location top:{},right:{},bottom:{},left{}".format(top_pos,right_pos,bottom_pos,left_pos))
    
    all_matches=face_recognition.compare_faces(know_face_encodings, current_face_encoding )
    name="Unkown Face"
    if True in all_matches:
        first_match_index=all_matches.index(True)
        name=know_face_names[first_match_index]
    cv2.rectangle(original_image,(left_pos,top_pos), (right_pos,bottom_pos), (255,0,0),2)
    font=cv2.FONT_ITALIC
    cv2.putText(original_image,name,(left_pos,top_pos),font,0.5,(255,255,255),1)
    cv2.imshow("Face Identifies",original_image)
         
        
























          