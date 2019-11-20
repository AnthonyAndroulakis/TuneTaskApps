# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	

import tkinter as tk
import os
from PIL import ImageTk, Image
import time
import multiprocessing
import glob
import linecache

practiceFiles=[]
tunesFiles=[]
for i in glob.glob("practice\\*.wav"):
    practiceFiles.append('..\\'+i)
for j in glob.glob("tunes\\*.wav"):
    tunesFiles.append('..\\'+j)
    

LARGE_FONT= ("Verdana", 40)
MEDIUM_FONT= ("Verdana", 40)
SMALL_FONT= ("Verdana", 30)

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.destroy()

class MelodyRepetitionTask(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame): #start page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Melody Repetition Task", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        global photo
        photo = tk.PhotoImage(file='welcome page.PPM')
        button1 = tk.Button(self, image=photo)
        button1.pack(pady=6)

        button3 = tk.Button(self, text="Enter participant number",
                            command=getInput, font=SMALL_FONT, highlightbackground='yellow')
        button3.pack(expand=True,fill='both')

        button = tk.Button(self, text="Practice",
                            command=lambda: controller.show_frame(PageOne), font=SMALL_FONT)
        button.pack(expand=True,fill='both')

        button2 = tk.Button(self, text="Melody Repetition Task",
                            command=lambda: controller.show_frame(PageTwo), font=SMALL_FONT)
        button2.pack(expand=True,fill='both')


class PageOne(tk.Frame): #practice page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button2 = tk.Button(self, text="Start Practice",
                            command= mtPractice, font=MEDIUM_FONT, highlightbackground='#00FF00')
        button2.pack(side='top',pady=150)

        button1 = tk.Button(self, text="← Back to Start",
                            command=lambda: controller.show_frame(StartPage), font=SMALL_FONT)
        button1.pack(side="left",pady=50,fill='both', expand=True)

        button3 = tk.Button(self, text="Go To Melody Repetition Task →",
                            command=lambda: controller.show_frame(PageTwo), font=SMALL_FONT)
        button3.pack(side="right",pady=50,fill='both', expand=True)


class PageTwo(tk.Frame): #melody repetition task page

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button2 = tk.Button(self, text="Start Melody Repetition Task",
                            command= mtTunes, font=MEDIUM_FONT, highlightbackground='#00FF00')
        button2.pack(side='top',pady=200)

        button1 = tk.Button(self, text="← Back to Start",
                            command=lambda: controller.show_frame(StartPage), font=SMALL_FONT)
        button1.pack(side="top",pady=50,fill='both', expand=True)

def mtPractice():
    print("cd ImgAudRec & py gui_test.py "+' '.join(practiceFiles))
    os.system("cd ImgAudRec & py gui_test.py "+' '.join(practiceFiles))

def mtTunes():
    print("cd ImgAudRec & py gui_test.py "+' '.join(tunesFiles))
    os.system("cd ImgAudRec & py gui_test.py "+' '.join(tunesFiles))
    
def getInput():
    os.system('py getinput.py')

app = MelodyRepetitionTask()
app.config(background = "white") 

app.title("Melody Repetition Task")
app.geometry("{}x{}".format(width, height))
app.mainloop()
