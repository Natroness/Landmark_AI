'''importing necessary libraries '''
import tensorflow as tf
import numpy as np
import json
import sys
import os
from tensorflow.keras.preprocessing import image




#constant from last main file
IMAGE_SIZE= (224,224)

#telling which model to work with
model = tf.keras.models.load_model("Landmark_AI.h5")

#loading class indices to know which number means which class 
with open("class_indices.json", "r") as f:
    class_indices = json.load(f)
#Invert class_indices to get index -> name mapping
index_to_class = {v:k for k,v in class_indices.items()}

#getting image from the commandline 
#it lets us to use directory from the terminal
if len(sys.argv)<2:
    #so when we run python3 predict_landmark.py (direcotry to image)
    print("Usage: python predict_landmark.py path_to_image.jpg")
    
    sys.exit()

img_path = sys.argv[1]

#if image not found it exits
if not os.path.exists(img_path):
    print(f"Error: File '{img_path}' not found.")
    sys.exit()

#Load and Preprocess the image
img = image.load_img(img_path,target_size = IMAGE_SIZE)
#converting image to a numpy array 
#bunch of numbers representing the pixels
img_array = image.img_to_array(img)
#pixel dividing by 255 so values go from 0-255 -> 0-1
img_array = img_array / 255.0
#adding a new dimension to make it like a batch of 1 image
img_array = np.expand_dims(img_array , axis = 0)

#Making prediction
#we running preprocessed image into the model with (.predict())
predictions = model.predict(img_array)
predicted_index = np.argmax(predictions[0])
#finding the index of the highest probability
predicted_class = index_to_class[predicted_index]
#predicted index to a landmark name
confidence = predictions[0][predicted_index]
#grabs a confidence score between 0 and 1 



#displaying the prediction
print(f"Predicted Landmark: {predicted_class} (Confidence: {confidence:.2f})")
