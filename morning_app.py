#%%
print('d')
#%%
def show_date():
    from datetime import date
    today = date.today()
    today_text = str(today.strftime("%b-%d-%Y"))
    today_text = "Today's date: {date_text} ".format(date_text = today_text)
    welcome_message.config(text = today_text)
    print(today_text)
#%%
from tkinter import *
# %%
window = Tk()
window.title('Morning App')

welcome_message = Label(window, text="Today is going to be awesome")
welcome_message.pack() # we could pack in the same line



window.geometry("500x100")

#(optional) Add a button to quit execution
Button(window, text="Quit", command=window.quit).pack()
Button(window, text="Date", command=show_date).pack()

# run our window
window.mainloop()

# %%
