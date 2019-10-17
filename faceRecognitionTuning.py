import face_recognition

imageOne = face_recognition.load_image_file("person.jpg")
imageTwo = face_recognition.load_image_file("personTwo.jpg")
imageThree = face_recognition.load_image_file("personThree.jpg")

personOneFaceEncoding = face_recognition.face_encodings(imageOne)[0]
personTwoFaceEncoding = face_recognition.face_encodings(imageTwo)[0]
personThreeFaceEncoding = face_recognition.face_encodings(imageThree)[0]

knownFaceEncodings = [
    personOneFaceEncoding, 
    personTwoFaceEncoding, 
    #personThreeFaceEncoding
]

unknownImage = face_recognition.load_image_file("unknown.jpg")

faceLocations = face_recognition.face_locations(unknownImage, number_of_times_to_upsample=2)

unknownFaceEncodings = face_recognition.face_encodings(unknownImage, known_face_locations=faceLocations)

for unknownFaceEncoding in unknownFaceEncodings:
    #Compare face encodings to determine whether the faces are match
    results = face_recognition.compare_faces(knownFaceEncodings, unknownFaceEncoding)
    name = "Unknown"
    if results[0]:
        name = "Person 1"
    elif results[1]:
        name = "Person 2"
    elif results[2]:

        name = "Person 3"

    print("Found {} in the photo".format(name))