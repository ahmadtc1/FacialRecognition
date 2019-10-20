import face_recognition
import argparse
from PIL import Image
from pathlib import Path
from tqdm import tqdm

#Use argument parser to pass the known image as an argument
ap = argparse.ArgumentParser()
ap.add_argument(
    "-i",
    "--image",
    required=True,
    help="The image to be used"
)

args = vars(ap.parse_args())

#Load the known image into a np array and extract its face encodings
knownImage = face_recognition.load_image_file(args["image"])
knownImageEncoding = face_recognition.face_encodings(knownImage)[0]

bestFaceDistance = 1.0
bestFaceImage = None

for imagePath in tqdm(Path("people").glob("*.jpg")):
    print("The image path is {}".format(imagePath))
    unknownImage = face_recognition.load_image_file(imagePath)
    unknownFaceEncodings = face_recognition.face_encodings(unknownImage)
    faceDistance = face_recognition.face_distance(unknownFaceEncodings, knownImageEncoding)[0]
    print("The face distance is {}".format(faceDistance))

    if faceDistance < bestFaceDistance:
        bestFaceDistance = faceDistance
        bestFaceImage = imagePath

bestMatch = face_recognition.load_image_file(bestFaceImage)
pilBestMatchImage = Image.fromarray(bestMatch)

pilOriginalImage = Image.fromarray(knownImage)

pilOriginalImage.show()
pilBestMatchImage.show()

