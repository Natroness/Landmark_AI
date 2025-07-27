#lets start working on the main file 
#we are using tensorflow here, i am using tensorflow's keras API
#TensorFlow keras API is high level ,easy to write and fast .
#Keras also handles memory management and I don't have to deal with complicated wiring as a beginner

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
#using imagedataGenerator which is a part of the tensorflow.keras API.
#It generates batches during training of the model and saves memory.

'''
MobileNetV2 is a CNN (Convolutional Neural Network) meaning a type of artificial
neural network primarily used for analysing visual imagery.
It was trained on millions of images (ImageNet), 
so it already knows how to see things like edges, shapes, patterns, curves, etc.
'''
from tensorflow.keras.applications import MobileNetV2
#It helps to stack the layers in order. As our program is linear.
from tensorflow.keras.models import Sequential
#GlobalAveragePooling2D shrinks the 2D feature maps into a 1D vector
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D



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
    rescale = 1./255, #changes pixel 0-255 to 0-1
    rotation_range = 30,#rotates randomly upto 30 degree
    zoom_range = 0.2,#zooms in/out
    brightness_range = (0.5,1.5), #makes photo darker/brighter
    horizontal_flip = True, #flips images left/right
    validation_split=0.2  #splits image by 20%
)

#training images from the train_datagen setting
train_generator = train_datagen.flow_from_directory(
    'src/images',
    target_size =IMAGE_SIZE,
    batch_size = BATCH_SIZE,
    class_mode = 'categorical',
    subset='training'

)

#to check if my model is actually learning or just memorizing
val_generator = train_datagen.flow_from_directory(
    'src/images',
    target_size = IMAGE_SIZE,
    batch_size = BATCH_SIZE,
    class_mode = 'categorical',
    subset = 'validation'
)

#lets load the base model without the fully connected layers
base_model = MobileNetv2(
    input_shape = IMAGE_SIZE + (3,),
    include_top = False, #no need for the top which is used to classify 1000 categories from imagenet dataset
    weights = 'imagenet' #asking pre-trained weights learned from imagenet
)

#Freezing the base model because we don't want to train it 
base_model.trainable = False

#stack our model using the sequential
model = Sequential(
    base_model,#extracts features like shapes/edges
    GlobalAveragePooling2D(),#reduces 2d vector to 1d vector
    Dense(128,actiavtion = 'relu'), #A fully connected layer 
    #leanrs patterns specific to landmark class(dense(18))
    Dense(train_generator.num_classes,activation= 'softmax')#output layer 
    #this outputs probability for each class 


)

