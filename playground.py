#%%
print('im working')

#%%
from tkinter import * 
#%%
#defining functions : 

def print_date():
    from datetime import date
    today = date.today()
    print("Today's date:", today)

# %%
window = Tk()
window.title('Morning Window')

# Add text into a window :
# 1 create text : 
welcome_message = Label(window, text= "Let's have a great day")
# 2 add text into window
welcome_message.pack()
#(optional) Configure window size : 
window.geometry("500x100")

#(optional) Add a button to quit execution
Button(window, text="Quit", command=window.quit).pack()
Button(window, text="Date", command=print_date).pack()

# run our window
window.mainloop()
# %%


