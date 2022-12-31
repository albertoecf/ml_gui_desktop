#%%
# %%
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import numpy as np
from keras.models import load_model 

print('d')


def upload_file():
    global uploaded_image
    file_path = filedialog.askopenfilename()
    uploaded_image = ImageTk.PhotoImage(file=file_path)
    image_label = Label(input_window)
    image_label.image = uploaded_image
    image_label['image'] = uploaded_image
    image_label.pack()

def predict_image():
    global uploaded_image
    
    file_path = filedialog.askopenfilename()
    uploaded_image = ImageTk.PhotoImage(file=file_path)
    image_label = Label(input_window)
    image_label.image = uploaded_image
    image_label['image'] = uploaded_image
    image_label.pack()
    
    loaded_model = load_model('burger_vs_boxex_CNN.h5')
    img_loaded = Image.open(file_path)
    img_resized = Image.Image.resize(img_loaded, (100,100))
    img = (np.array(img_resized)-127.5)/127.5
    img = img.reshape(1,100,100,3)
    
    prediction = loaded_model.predict(img) 
    classes_x=np.argmax(prediction,axis=1)
    
    if classes_x == 0:
        l2.config(
        text= "Product Prediction : Burger",fg="white", bg="green")
    elif classes_x == 1 :
        l2.config(
        text= "Product Prediction : Box",fg="white" ,bg="green")
    else : 
        l2.config(
        text= "Couldn't predict. Please try again or other image")




#%%
input_window = Tk()
input_window.title('Classify Image')
l1 = Label(input_window,text='Upload your image').pack()
l2 = Label(input_window, text= "Waiting user input", bg='grey')
l2.pack()
b0 = Button(input_window, text='Show File', 
   width=20,command = lambda:upload_file()).pack()
b1 = Button(input_window, text='Predict Class', 
   width=20,command = lambda:predict_image()).pack()

Button(input_window, text="Quit",
       command=input_window.quit).pack()
input_window.mainloop()

# %%
