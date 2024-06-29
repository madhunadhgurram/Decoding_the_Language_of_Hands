
import sys
import cv2

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import numpy as np
import cv2

from PIL import ImageTk, Image
from tkinter import filedialog, messagebox

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
from backend import image_pred

import os.path

from googletrans import Translator

# Create Translator objects for Hindi and Kannada
translatorHI = Translator()
translatorKN = Translator()

import pyttsx3
engine = pyttsx3.init()

# Function to voice out the result text
def voice_out_result(result_text):
    engine.say(result_text)
    engine.runAndWait()
    
    
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = ImageModule(root)
    root.mainloop()


w = None


def create_ImageModule(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel(root)
    top = ImageModule(w)
    return (w, top)


def destroy_ImageModule():
    global w
    w.destroy()
    w = None


class ImageModule:
    def __init__(self, top=None):
        self.directory = "model/"

        def flip_predict(event):
            if self.ImageFileName == None:
                messagebox.showerror('Error', 'Please Select a image')
            else:
                img = cv2.imread(self.ImageFileName)
                img = cv2.flip(img, 1)
                img = cv2.resize(img, None, fx=0.4, fy=0.4)
                frame, result = image_pred(img)
                # print(result)
                b, g, r = cv2.split(frame)
                rbgImg = cv2.merge((r, g, b))
                image = Image.fromarray(rbgImg)
                image = image.resize((800, 600), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                self.lblImage.configure(image=photo)
                self.lblImage.image = photo
                messagebox.showinfo("Prediction", result)

        def predict(event):
            if self.ImageFileName == None:
                messagebox.showerror('Error', 'Please Select a image')
            else:
                img = cv2.imread(self.ImageFileName)
                img = cv2.resize(img, None, fx=0.4, fy=0.4)
                frame, result = image_pred(img)
                # hi = translatorHI.translate(result)
                # kn = translatorKN.translate(result)
                hi = translatorHI.translate(result, src="en", dest="hi").text
                kn = translatorKN.translate(result, src="en", dest="te").text
                

                b, g, r = cv2.split(frame)
                rbgImg = cv2.merge((r, g, b))
                image = Image.fromarray(rbgImg)
                image = image.resize((800, 600), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                self.lblImage.configure(image=photo)
                self.lblImage.image = photo

                self.lblResultText.configure(text=result)
                self.lblHiText.configure(text=hi)
                self.lblKnText.configure(text=kn)
                voice_out_result(result)  # Voice out the result text


        self.ImageFileName = None

        def chooseImage(event):
            ##Get File directory from user
            self.ImageFileName = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                             filetypes=(("all files", "*.*"),
                                                                        ("jpeg files", "*.jpg"),
                                                                        ("png files", "*.png")))
            ###Identify the name of file
            image = Image.open(self.ImageFileName)
            image = image.resize((800, 600), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.lblImage.configure(image=photo)
            self.lblImage.image = photo

        def btnExit(event):
            top.destroy()
            import mainGUI
            mainGUI.vp_start_gui()

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        font10 = "-family {Segoe UI} -size 24 -weight bold -slant " \
                "roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 18 -weight bold -slant " \
                "roman -underline 0 -overstrike 0"

        top.geometry("1324x817+310+102")
        top.title("New Toplevel")
        top.state('zoomed')
        top.configure(background="#ffffff")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.385, rely=0.037, height=60, width=715)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Sign Language Detection System''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.083, rely=0.049, height=154, width=250)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "images/icon.png")
        self._img0 = tk.PhotoImage(file=photo_location)
        self.Label2.configure(image=self._img0)
        self.Label2.configure(text='''Label''')

        self.lblImage = tk.Label(top)
        self.lblImage.place(relx=0.317, rely=0.196, height=606, width=852)
        self.lblImage.configure(background="#ffffff")
        self.lblImage.configure(disabledforeground="#a3a3a3")
        self.lblImage.configure(foreground="#000000")
        self.lblImage.configure(relief="ridge")
        self.lblImage.configure(text='''Image''')
        self.lblImage.configure(width=852)

        self.btnChooseImage = tk.Button(top)
        self.btnChooseImage.place(relx=0.068, rely=0.33, height=70, width=225)
        self.btnChooseImage.configure(activebackground="#ececec")
        self.btnChooseImage.configure(activeforeground="#000000")
        self.btnChooseImage.configure(background="#ff1212")
        self.btnChooseImage.configure(disabledforeground="#a3a3a3")
        self.btnChooseImage.configure(font=font11)
        self.btnChooseImage.configure(foreground="#ffffff")
        self.btnChooseImage.configure(highlightbackground="#d9d9d9")
        self.btnChooseImage.configure(highlightcolor="black")
        self.btnChooseImage.configure(pady="0")
        self.btnChooseImage.configure(text='''Choose Image''')
        self.btnChooseImage.bind('<Button-1>', chooseImage)

        self.btnAlgorithm1 = tk.Button(top)
        self.btnAlgorithm1.place(relx=0.068, rely=0.59, height=70, width=225)
        self.btnAlgorithm1.configure(activebackground="#ececec")
        self.btnAlgorithm1.configure(activeforeground="#000000")
        self.btnAlgorithm1.configure(background="#f7ff0f")
        self.btnAlgorithm1.configure(disabledforeground="#a3a3a3")
        self.btnAlgorithm1.configure(font=font11)
        self.btnAlgorithm1.configure(foreground="#0a0a0a")
        self.btnAlgorithm1.configure(highlightbackground="#d9d9d9")
        self.btnAlgorithm1.configure(highlightcolor="black")
        self.btnAlgorithm1.configure(pady="0")
        self.btnAlgorithm1.configure(text='''Predict''')
        self.btnAlgorithm1.bind('<Button-1>', predict)

        self.btnExit = tk.Button(top)
        self.btnExit.place(relx=0.068, rely=0.808, height=70, width=225)
        self.btnExit.configure(activebackground="#ececec")
        self.btnExit.configure(activeforeground="#000000")
        self.btnExit.configure(background="#287a0a")
        self.btnExit.configure(disabledforeground="#a3a3a3")
        self.btnExit.configure(font=font11)
        self.btnExit.configure(foreground="#ffffff")
        self.btnExit.configure(highlightbackground="#d9d9d9")
        self.btnExit.configure(highlightcolor="black")
        self.btnExit.configure(pady="0")
        self.btnExit.configure(text='''EXIT''')
        self.btnExit.bind('<Button-1>', btnExit)
        
        self.lblResult = tk.Label(top)
        self.lblResult.place(relx=0.8, rely=0.2, height=100, width=300)
        self.lblResult.configure(background="#ffffff")
        self.lblResult.configure(disabledforeground="#a3a3a3")
        self.lblResult.configure(foreground="#000000")
        self.lblResult.configure(font=("Helvetica", 16))
        self.lblResult.configure(text='''Result:''')

        self.lblResultText = tk.Label(top)
        self.lblResultText.place(relx=0.8, rely=0.3, height=100, width=300)
        self.lblResultText.configure(background="#ffffff")
        self.lblResultText.configure(disabledforeground="#a3a3a3")
        self.lblResultText.configure(foreground="#000000")
        self.lblResultText.configure(font=("Helvetica", 16))

        self.lblHi = tk.Label(top)
        self.lblHi.place(relx=0.8, rely=0.4, height=100, width=300)
        self.lblHi.configure(background="#ffffff")
        self.lblHi.configure(disabledforeground="#a3a3a3")
        self.lblHi.configure(foreground="#000000")
        self.lblHi.configure(font=("Helvetica", 16))
        self.lblHi.configure(text='''Hindi Translation:''')

        self.lblHiText = tk.Label(top)
        self.lblHiText.place(relx=0.8, rely=0.5, height=100, width=300)
        self.lblHiText.configure(background="#ffffff")
        self.lblHiText.configure(disabledforeground="#a3a3a3")
        self.lblHiText.configure(foreground="#000000")
        self.lblHiText.configure(font=("Helvetica", 16))

        self.lblKn = tk.Label(top)
        self.lblKn.place(relx=0.8, rely=0.6, height=100, width=300)
        self.lblKn.configure(background="#ffffff")
        self.lblKn.configure(disabledforeground="#a3a3a3")
        self.lblKn.configure(foreground="#000000")
        self.lblKn.configure(font=("Helvetica", 16))
        self.lblKn.configure(text='''Telugu Translation:''')

        self.lblKnText = tk.Label(top)
        self.lblKnText.place(relx=0.8, rely=0.7, height=100, width=300)
        self.lblKnText.configure(background="#ffffff")
        self.lblKnText.configure(disabledforeground="#a3a3a3")
        self.lblKnText.configure(foreground="#000000")
        self.lblKnText.configure(font=("Helvetica", 16))
