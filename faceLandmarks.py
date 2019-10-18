#USAGE
#python3 faceLandmarks.py --image person.jpg

import PIL.Image
import PIL.ImageDraw
import face_recognition
import argparse


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help="Path to the image to be landmarked"
)
args = vars(ap.parse_args())

#Load the image into a numpy array
image = face_recognition.load_image_file(args["image"])

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