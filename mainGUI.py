import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import ImageModule
try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True
import mainGUI_support
import os.path
from backend import webcam_pred


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    root = tk.Tk()
    top = Toplevel1(root)
    mainGUI_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    mainGUI_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        def ImageModuleGUI(event):
            top.destroy()
            ImageModule.vp_start_gui()

        def WebCamModule(event):
            import threading
            threading.Thread(target=webcam_pred).start()
            # top.destroy()
            # WebCam.vp_start_gui()


        def btnExit(event):
            import os
            os._exit(0)

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font16 = "-family Constantia -size 40 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font18 = "-family {Sitka Small} -size 15 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"

        w = 1000
        h = 650
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        top.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # top.geometry("1016x635")
        top.title("Sign Language Recognition System")
        top.configure(background="#ffffff")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.3, rely=0.01, height=250, width=350)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "Images/icon.png")
        self._img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=self._img0)
        self.Label1.configure(text='''Label''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.0, rely=0.4, height=88, width=1000)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font16)
        self.Label2.configure(foreground="#2365e8")
        self.Label2.configure(text='''Language Recognition System''')
        self.Label2.configure(width=659)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.03, rely=0.535, relheight=0.402, relwidth=0.94)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="7")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#ffffff")
        self.Frame1.configure(width=955)





        self.btnImage1 = tk.Label(self.Frame1)
        self.btnImage1.place(relx=0.1, rely=0.110, height=176, width=172)
        self.btnImage1.configure(activebackground="#f9f9f9")
        self.btnImage1.configure(activeforeground="black")
        self.btnImage1.configure(background="#ffffff")
        self.btnImage1.configure(disabledforeground="#a3a3a3")
        self.btnImage1.configure(foreground="#000000")
        self.btnImage1.configure(highlightbackground="#d9d9d9")
        self.btnImage1.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location, "Images/images icon.png")
        self._img3 = tk.PhotoImage(file=photo_location)
        self.btnImage1.configure(image=self._img3)
        self.btnImage1.configure(text='''Label''')
        self.btnImage1.configure(width=172)
        self.btnImage1.bind('<Button-1>', ImageModuleGUI)


        self.Label3_61 = tk.Label(self.Frame1)
        self.Label3_61.place(relx=0.12, rely=0.784, height=36, width=142)
        self.Label3_61.configure(activebackground="#f9f9f9")
        self.Label3_61.configure(activeforeground="black")
        self.Label3_61.configure(background="#ffffff")
        self.Label3_61.configure(disabledforeground="#a3a3a3")
        self.Label3_61.configure(font=font18)
        self.Label3_61.configure(foreground="#061104")
        self.Label3_61.configure(highlightbackground="#d9d9d9")
        self.Label3_61.configure(highlightcolor="#000000")
        self.Label3_61.configure(text='''Image''')
        self.Label3_61.configure(width=142)



        self.Label3_5 = tk.Label(self.Frame1)
        self.Label3_5.place(relx=0.460, rely=0.784, height=26, width=142)
        self.Label3_5.configure(activebackground="#f9f9f9")
        self.Label3_5.configure(activeforeground="black")
        self.Label3_5.configure(background="#ffffff")
        self.Label3_5.configure(disabledforeground="#a3a3a3")
        self.Label3_5.configure(font=font18)
        self.Label3_5.configure(foreground="#061104")
        self.Label3_5.configure(highlightbackground="#d9d9d9")
        self.Label3_5.configure(highlightcolor="#000000")
        self.Label3_5.configure(text='''WebCam''')
        self.Label3_5.configure(width=142)


        self.btnWebcam = tk.Label(self.Frame1)
        self.btnWebcam.place(relx=0.45, rely=0.157, height=154, width=154)
        self.btnWebcam.configure(background="#ffffff")
        self.btnWebcam.configure(disabledforeground="#a3a3a3")
        self.btnWebcam.configure(foreground="#000000")
        photo_location = os.path.join(prog_location, "Images/webcam icon.png")
        self._img1 = tk.PhotoImage(file=photo_location)
        self.btnWebcam.configure(image=self._img1)
        self.btnWebcam.configure(text='''Label''')
        self.btnWebcam.bind('<Button-1>', WebCamModule)


        self.btnExit = tk.Label(self.Frame1)
        self.btnExit.place(relx=0.822, rely=0.100, height=186, width=150)
        self.btnExit.configure(activebackground="#f9f9f9")
        self.btnExit.configure(activeforeground="black")
        self.btnExit.configure(background="#ffffff")
        self.btnExit.configure(disabledforeground="#a3a3a3")
        self.btnExit.configure(foreground="#000000")
        self.btnExit.configure(highlightbackground="#d9d9d9")
        self.btnExit.configure(highlightcolor="black")
        photo_location = os.path.join(prog_location, "Images/ExitIcon.png")
        self._img4 = tk.PhotoImage(file=photo_location)
        self.btnExit.configure(image=self._img4)
        self.btnExit.configure(text='''Label''')
        self.btnExit.configure(width=162)
        self.btnExit.bind('<Button-1>', btnExit)

        self.Label3_6 = tk.Label(self.Frame1)
        self.Label3_6.place(relx=0.832, rely=0.784, height=26, width=130)
        self.Label3_6.configure(activebackground="#f9f9f9")
        self.Label3_6.configure(activeforeground="black")
        self.Label3_6.configure(background="#ffffff")
        self.Label3_6.configure(disabledforeground="#a3a3a3")
        self.Label3_6.configure(font=font18)
        self.Label3_6.configure(foreground="#061104")
        self.Label3_6.configure(highlightbackground="#d9d9d9")
        self.Label3_6.configure(highlightcolor="#000000")
        self.Label3_6.configure(text='''Exit''')
        self.Label3_6.configure(width=142)



