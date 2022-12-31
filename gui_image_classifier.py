from tkinter import *
from image_class_predictor import image_predictor


def image_prediction_output():
    '''run imported function and inject text in text widget'''
    prediction_text_widget.config(text=image_predictor())


window = Tk()
window.title("Let's check your image")

title_msg_widget = Label(window, text="Upload your image")
predict_button = Button(window, text='Make Prediction',
                        command=image_prediction_output)
prediction_text_widget = Label(
    window, text='Prediction : (waiting user input)')

prediction_text_widget.pack()
predict_button.pack()
title_msg_widget.pack()
window.mainloop()
