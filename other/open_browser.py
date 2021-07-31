import webbrowser
from tkinter import *

root = Tk()

root.title("Open Browser")
root.geometry('300x200')


def google():
    webbrowser.open("http://google.com")


google_button = Button(root, text="Google", command=google).pack(pady=20)

root.mainloop()
