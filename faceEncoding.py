import face_recognition

#Load the image file into a numpy array using face_recognition
image = face_recognition.load_image_file("faces.jpg")

faceEncodings = face_recognition.face_encodings(image)

if len(faceEncodings) == 0:
    print("No faces found in the image")

else:
    #Print the encodings for the first face found in the image
    firstFaceEncoding = faceEncodings[0]
    print(firstFaceEncoding)