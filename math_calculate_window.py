#%%
# %%
from tkinter import *
print('d')
#%%

input_window = Tk()
input_window.title('Calculate')
Label(input_window,text='input two numbers').pack()

input_one = Entry(input_window )
input_two = Entry(input_window)

input_one.pack()
input_two.pack()

submit_button = Button(input_window, text ='Calculate')
submit_button.pack()


Button(input_window, text="Quit",
       command=input_window.quit).pack()
input_window.mainloop()
# %%
