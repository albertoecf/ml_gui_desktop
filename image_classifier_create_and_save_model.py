from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import to_categorical
import os
import cv2

from keras.models import Sequential
from keras.layers import Activation, Conv2D, Dense, Flatten, MaxPool2D
from sklearn.model_selection import train_test_split

def images_to_array(folder,name):
    for imgage in os.listdir(folder):
        loaded_image = Image.open(os.path.join(folder, imgage))
        resize_image = Image.Image.resize(loaded_image, [100,100])
        image_array = np.array(resize_image)
        x.append(image_array) #images
        y.append(name_encoded[name]) #categories

        image_flipped = cv2.flip(image_array,1) #feature argument data
        x.append(image_flipped)
        y.append(name_encoded[name])


        image_blurred = cv2.blur(image_array, (2,2)) #feature argument data
        x.append(image_blurred)
        y.append(name_encoded[name])

        image_flipped_blurred = cv2.blur(image_flipped, (2,2))
        x.append(image_flipped)
        y.append(name_encoded[name])




def show_image(index):
    plt.imshow(x[index])
    plt.show()
    print(y[index])

x = [] # images
y = [] # categories 

folder_burger = 'burger_pictures'
folder_box = 'boxes_pictures'

name_encoded = {"burger":0, "box":1 }

images_to_array(folder_box, "box")
images_to_array(folder_burger, "burger")

y = to_categorical(y, num_classes=2) #one hot encoding
x = np.array(x) # convert to numpy array 
show_image(0)
#Normalize data-> Now data is 0-255 , we need between -1 , 1 
x = ((x - 127.5)/127.5) 

show_image(90)

# Create the Architecture for the CNN
model = Sequential()

model.add(Conv2D(32, (5,5), padding='same',activation='relu', input_shape=(100,100,3))) # we resize imagenes -> (100,100). rbg = 3
model.add(MaxPool2D(pool_size=(2,2))) # MaxPool -> max value pooling. we could use : min, average..

model.add(Conv2D(100, (5,5), padding='same',activation='relu')) 
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Conv2D(100, (5,5), padding='same',activation='relu')) 
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Conv2D(100, (5,5), padding='same',activation='relu')) 
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Conv2D(100, (5,5), padding='same',activation='relu')) 
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(124))
model.add(Activation('relu'))
model.add(Dense(2))
model.add(Activation('sigmoid'))

model.summary()
# %%
# Prepare to run
x_train, x_test , y_train, y_test = train_test_split(x,y, test_size=0.1) # split train and test
# %%
from keras.optimizers import Adam
optimizer_adam = Adam(lr=0.001) #learning rate
model.compile(optimizer=optimizer_adam, loss='binary_crossentropy',metrics=['accuracy'])
h = model.fit(x_train, y_train, batch_size=10, epochs=20, validation_data=(x_test,y_test))
model.save('burger_vs_boxex_CNN.h5')

plt.plot(h.history['accuracy'], label='train')
plt.plot(h.history['val_accuracy'], label='test')
plt.title('Model accuracy')
plt.xlabel('Epoch Number')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()

model_score = model.evaluate(x_test, y_test, verbose=0)
print('Test accuracy : {}'.format(model_score[1]))