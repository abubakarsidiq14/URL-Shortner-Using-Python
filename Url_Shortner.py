from tkinter import *
import pyshorteners

def Shorturl():
    U = url.get()
    Url = U

    def short(Url):
        Short = pyshorteners.Shortener()
        print(Short.tinyurl.short(Url))
    short(Url)
    
root =Tk()
root.geometry('800x300')
root.title("URL Shortner")

url=StringVar()

Label(root,text="URL Shortner",font="Times 24 bold").place(x=300,y=40)
Label(root,text="Enter URL Here : ",font="Times 18 bold").place(x=30,y=100)
Entry(root,textvariable=url,width=90).place(x=240,y=108)
Label(root,text="Press Generate Button to Generate Shortner.",font="Times 14").place(x=30,y=150)
Button(root,text="Generate",font="Times 16 bold",command=Shorturl).place(x=350,y=200)

root.mainloop()