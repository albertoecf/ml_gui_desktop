from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from keras.models import load_model 

loaded_model = load_model('burger_vs_boxex_CNN.h5')

image_path = "new_image.jpg"

def prediction_new_image(image_to_predict_path):
    img_loaded = Image.open(image_to_predict_path)
    img_resized = Image.Image.resize(img_loaded, (100,100))
    img = (np.array(img_resized)-127.5)/127.5
    img = img.reshape(1,100,100,3)
    prediction = loaded_model.predict(img) 
    classes_x=np.argmax(prediction,axis=1)
    if classes_x == 0:
        print("Prediction : burger")
    elif classes_x == 1 :
        print('Prediction : Box')
    else : 
        print('could not decide')
    plt.imshow(img_resized)
    plt.show()


image_path = "cajaunicornio.jpeg"
prediction_new_image(image_path)

