import datetime
import tkinter

counter = -1
running = False
price = 0
def counter_label(label):
    def count():
        if running:
            global counter
            global price
            price_sec = 0.0066667   #cena za sekundu

            if counter==-1:
                display="Spúšťam..."
                display2=" "
            else:
                display = str(datetime.timedelta(seconds=counter))
                display2 = str(round(counter*price_sec,2)) + " €"
            label['text']=display
            price_label['text'] = display2
            label.after(1000, count)
            counter += 1

    count()

def Start(label):
    global running
    running = True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'

def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False

def Reset(label):
    global counter
    counter=-1
    if running==False: # If reset is pressed after pressing stop.
        reset['state']='disabled'
        label['text']='-'
    else: # If reset is pressed while the stopwatch is running.
        label['text']='reštart'

root = tkinter.Tk()
root.title("Stopky")
root.minsize(width=250, height=140)
label = tkinter.Label(root, text="Čas", fg="black", font="Arial 20 bold")
label.pack()
price_label = tkinter.Label(root, text="Cena", fg="black", font="Arial 20 bold")
price_label.pack()
start = tkinter.Button(root, text='Start', width=15, command = lambda:Start(label))
stop = tkinter.Button(root, text='Stop', width = 15, state ='disabled', command = Stop)
reset = tkinter.Button(root, text ='Reset', width = 15, state = 'disabled', command = lambda:Reset(label))

start.pack()
stop.pack()
reset.pack()
root.mainloop()
