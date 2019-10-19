from PIL import Image, ImageDraw
import face_recognition
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", 
                required=True, 
                help="Path to the image to be used"
)
args = vars(ap.parse_args())

#Load the image as a np array and find the face landmarks in the picture
image = face_recognition.load_image_file(args["image"])
faceLandmarksList = face_recognition.face_landmarks(image)

#Load the image so it can be drawn on using the PIL library
pilImage = Image.fromarray(image)
draw = ImageDraw.Draw(pilImage, 'RGBA')

for faceLandmark in faceLandmarksList:
    draw.polygon(faceLandmark["left_eyebrow"], fill=(128,0,128,100))
    draw.polygon(faceLandmark["right_eyebrow"], fill=(128,0,128,100))
    draw.polygon(faceLandmark["top_lip"], fill=(128,0,128,100))
    draw.polygon(faceLandmark["bottom_lip"], fill=(128,0,128,100))
    draw.line(faceLandmark["nose_bridge"], fill = (128,0,128, 100), width=7)

pilImage.show()