from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image 
from single_image_haze_removal import removeHazeUtility
import cv2

def reset():
    imageLabel.configure(image = None)
    imageLabel.image = None

    imageLabel2.configure(image = None)
    imageLabel2.image = None

def save_file():
    files = [ ('JPEG image', '*.jpg'),
             ('PNG image', '*.png')]
    filename = filedialog.asksaveasfilename(filetypes = files, defaultextension = files)
    dehazed_img = cv2.imread('result.jpg')
    cv2.imwrite(filename, dehazed_img)

def convert_file():
    global filename
    dehazed_img = removeHazeUtility(filename)
    img = ImageTk.PhotoImage(Image.open('result.jpg'))
    imageLabel2.configure(image = img)
    imageLabel2.image = img

def open_file():
    global filename
    filename = filedialog.askopenfilename()
    img = ImageTk.PhotoImage(Image.open(filename))
    imageLabel.configure(image = img)
    imageLabel.image = img

filename = ''
root = Tk()
root.title('Satellite Image Dehazer')
root.geometry('1124x637')

open_btn = Button(root, text = "OPEN", command=open_file)
open_btn.place(x=25, y=20)
convert_btn = Button(root, text = "CONVERT", command=convert_file)
convert_btn.place(x=275, y=20)
save_btn = Button(root, text = "SAVE", command=save_file)
save_btn.place(x=525, y=20)
reset_btn = Button(root, text = "RESET", command=reset)
reset_btn.place(x=775, y=20)

imageLabel = Label(root)
imageLabel.place(x=25, y=100)

imageLabel2 = Label(root)
imageLabel2.place(x=587, y=100)

root.mainloop()