import tkinter as tk

toor = tk.Tk()
    
def func(event):
    print("You hit return.")
    entrytext=entry.get()
    while entrytext=="":
        super() #random piece of code that does not work but gets the job done
    open('participant.txt','w').write(entry.get())
    toor.destroy()
toor.bind('<Return>', func)

def onclick():
    print("You clicked the button")
    entrytext=entry.get()
    while entrytext=="":
        super() #random piece of code that does not work but gets the job done
    open('participant.txt','w').write(entry.get())
    toor.destroy()

label = tk.Label(toor, text="Enter participant number:", font=("Verdana", 25))
label.pack(pady=10,padx=10)

entry = tk.Entry(toor)
entry.pack()
button = tk.Button(toor,text='submit',command=onclick)
button.pack()

windowWidth = toor.winfo_reqwidth()
windowHeight = toor.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(toor.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(toor.winfo_screenheight()/2 - windowHeight/2)

toor.title("Enter Participant Number")
toor.geometry("+{}+{}".format(positionRight, positionDown))
toor.mainloop()
