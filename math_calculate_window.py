#%%
# %%
from tkinter import *
print('d')
#%%
def math_function():
    first_operand = int(input_one.get())
    second_operand = int(input_two.get())
    result_val = first_operand * second_operand
    result_text_widget.config(
        text= "Result : {}".format(result_val))

#%%
input_window = Tk()
input_window.title('Calculate')
Label(input_window,text='input two numbers').pack()

input_one = Entry(input_window )
input_two = Entry(input_window)

submit_button = Button(input_window, text ='Calculate', command=math_function)
result_text_widget = Label(input_window, text = "")

input_one.pack()
input_two.pack()
submit_button.pack()
result_text_widget.pack()
Button(input_window, text="Quit",
       command=input_window.quit).pack()
input_window.mainloop()
# %%
