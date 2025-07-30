import tensorflow as tf
import numpy as np
import json
import sys
import os
from tensorflow.keras.preprocessing import image

#constant from last main file
IMAGE_SIZE= (224,224)

model = tf.keras.models.load_model("Landmark_AI.h5")

#loading class indices 
with open("class_indices.json" as "r") as f:
    class_indices = json.load(f)
#Invert class_indices to get index -> name mapping
index_to_class = {v:k for k,v in class_indices.items()}

#Image path from command line
if len(sys.argv)<2:
    print("Usage: python predict_landmark.py path_to_image.jpg")
    sys.exit()

img_path = sys.argv[1]

if not os.path.exists(img_path):
    print(f"Error: File '{img_path}' not found.")
    sys.exit()

#Load and Preprocess the image
img = image.load_img(img_path,target_size = IMAGE_SIZE)
img_array = image.img_to_array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array , axis = 0)

#predict
prediction = model.predict(img_array)
predicted_index = np.argmax(predictions)
predicted_class = index_to_class[predicted_index]
confidence = predictions[0][predicted_index]

#displaying the prediction
print(f"Predicted Landmark: {predicted_class }((Confidence: {confidence:.2f})")
