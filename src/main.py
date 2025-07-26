#lets start working on the main file 
#we are using tensorflow here, i am using tensorflow's keras API
#TensorFlow keras API is high level ,easy to write and fast .
#Keras also handles memory management and I don't have to deal with complicated wiring as a beginner

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
#using imagedataGenerator which is a part of the tensorflow.keras API.
#It generates batches during training of the model and saves memory.
