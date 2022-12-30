#%%
print('im working')

#%%
from tkinter import * 
# %%
window = Tk()
window.title('Testing Window')

# Add text into a window :
# 1 create text : 
welcome_message = Label(window, text= "Welcome to our first window")
# 2 add text into window
welcome_message.pack()
# Configure window size : 
window.geometry("500x50")

#Add a button to quit execution
Button(window, text="Quit", command=window.quit).pack()
window.mainloop()
# %%


