#lets start working on the main file 
#we are using tensorflow here, i am using tensorflow's keras API
#TensorFlow keras API is high level ,easy to write and fast .
#Keras also handles memory management and I don't have to deal with complicated wiring as a beginner

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
#using imagedataGenerator which is a part of the tensorflow.keras API.
#It generates batches during training of the model and saves memory.

#Lets Create our Data generator to Load and Augment Images

#lets keep constant ImageSize and BatchSize
IMAGE_SIZE = (224,224)
#this is the size Mobilenet will expect
BATCH_SIZE = 32
#its the number of images to process at once


'''
So, Here we are going to train the model via ImageDataGenerator,
We will train the model with same images but we want it to tweak a little bit so that it can be trained on the 
small dataset.
So, we will ask the tool to rescale itself,rotate,zoom in and out so that it can figure
out and train itself.
'''


train_datagen = ImageDataGenerator(
    rescale = 1./225, #changes pixel 0-255 to 0-1
    rotation_range = 30,#rotates randomly upto 30 degree
    zoom_range = 0.2,#zooms in/out
    brightness_range = (0.5,1.5), #makes photo darker/brighter
    horizontal_flip = True, #flips images left/right
    validation_split=0.2  #splits image by 20%
)

train_generator = train_datagen.flow_from_directory(
    'src/images',
    target_size =IMAGE_SIZE,
    batch_size = BATCH_SIZE,
    class_mode = 'categorical',
    subset='training'

)

val_generator = train_datagen.flow_from_directory(
    'src/images',
    target_size = IMAGE_SIZE,
    batch_size = BATCH_SIZE,
    class_mode = 'categorical',
    subset = 'validation'
)