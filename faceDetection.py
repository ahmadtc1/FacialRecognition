import PIL.Image
import PIL.ImageDraw
import face_recognition

#TODO: Add a command line argument to allow users to specify the picture they would like to run face detection on


#Load in the file as a numpy array
image = face_recognition.load_image_file("faces.jpg")

#Find all the faces in the image
#Run the face_detection HOG window slider to find faces
faceLocations = face_recognition.face_locations(image)

#Detemine and print the number of faces identified in the image
numberOfFaces = len(faceLocations)
print("I found %d faces in this photograph" % numberOfFaces)

pil_image = PIL.Image.fromarray(image)

for faceLocation in faceLocations:
    top, right, bottom, left = faceLocation
    print("A face is located at pixel location Top: %f, Right: %f, Bottom: %f, Left: %f" % (top, right, bottom, left))
    #Draw a bounding box surrounding the identified faces
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle([(left, top), (right, bottom)], outline="red")

pil_image.show()
