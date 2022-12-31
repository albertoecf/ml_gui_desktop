# %%
from tkinter import *
print('d')
# %%


def show_date():
    '''Get date and show as text in label widget'''
    from datetime import date
    today = date.today()
    today_text = str(today.strftime("%b-%d-%Y"))
    today_text = "Today's date: {date_text} ".format(date_text=today_text)
    welcome_message.config(text=today_text)
    print(today_text)
# %%
window = Tk()
window.title('Morning App')

welcome_message = Label(
    window,
    text="Today is going to be awesome",
    padx=200,
    pady=100,
    fg='white'  # similar to font
    , bg='blue'  # background color
)
welcome_message.pack()  # we could pack in the same line

# window.geometry("500x100")

# (optional) Add a button to quit execution
Button(window, text="Quit",
       command=window.quit,
       fg='red',
       bg="#FF8C00").pack()
show_date_button = Button(window, text="Date", command=show_date)
show_date_button.pack()

# run our window
window.mainloop()

# %%

