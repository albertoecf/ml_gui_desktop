#%%
# %%
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import matplotlib.pyplot as plt
print('d')


def upload_file():
    global uploaded_image
    file_path = filedialog.askopenfilename()
    uploaded_image = ImageTk.PhotoImage(file=file_path)
    image_label = Label(input_window)
    image_label.image = uploaded_image
    image_label['image'] = uploaded_image
    image_label.pack()

#%%
input_window = Tk()
input_window.title('Classify Image')
l1 = Label(input_window,text='Upload your image').pack()


b1 = Button(input_window, text='Upload File', 
   width=20,command = lambda:upload_file()).pack()

Button(input_window, text="Quit",
       command=input_window.quit).pack()
input_window.mainloop()
# %%
