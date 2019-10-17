import PIL.Image
import PIL.ImageDraw
import face_recognition

#Load the image into a numpy array
image = face_recognition.load_image_file("faces.jpg")

#Find all the facial landmarks in the image using a face landmark detection algorithm
faceLandmarksList = face_recognition.face_landmarks(image)

numberOfFaces = len(faceLandmarksList)

print("%d faces were found within the image" % numberOfFaces)

editedImage = PIL.Image.fromarray(image)

draw = PIL.ImageDraw.Draw(editedImage)

for face in  faceLandmarksList:
    for name, listOfPoints in face.items():
        print("The {} in this face has the following points{}".format(name, listOfPoints))
        draw.line(listOfPoints, fill="red", width=2)

editedImage.show()