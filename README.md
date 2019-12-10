# FacialRecognition

This repository is a fun introduction for myself to the world of **facial recognition** and **image processing**. 

It's taught me loads about implementing an **image recognition pipeline** as well as some fun checkpoints along the way!

# Get Groovy With Your Own Digital Makeup
To use the digital makeup filter, simply download the digitalMakeup.py file and install requirements using the requirements.txt file.
To run it on an image of your choice, just point to the image as a command line argument like so:
    
    python3 facialRecognition.py -i Harold.png
    
To list options or for clarification with usage, go ahead and use the -h flag
    
    python3 facialRecognition.py -h

## Digital Makeup

![Harold Pre-Makeup](./Harold.png)   ![Harold Post-Makeup](./HaroldMakeup.png) 

Face filters aren't as difficult as you think once you learn about  **facial landmarks**. This is one of the fun use-cases I implemented after using a **HOG sliding window face detection** and **landmark estimation with transformations** Using the 68 landmarked points on the human face, there's loads of filters we can apply!

## Facial Recognition

Moving forward in the pipeling, we eventually reach the point of **facial encoding** which generates 128 measurements to represent a human face for us. In this part of the pipeline, I learned about the problem of **model interpretability** which can lead to hidden biases as we can't understand the inner workings of these models.
Once we have our encodings, we can calculate face similarity using some good ole euclidean distance calculations!
