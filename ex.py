from tkinter import *
from datetime import datetime

temp = 0
after_id = ''


def tick():
    global temp, after_id
    after_id = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label1.configure(text=str(f_temp))
    temp += 1


def start_tick():
    btnStart.pack_forget()
    btnStop.pack()
    tick()


root = Tk()
root.title('секундомер')
root.resizable(width=False, height=False)
root.geometry('300x200')


label1 = Label(root, width=10, font='Arial 30', text='00:00')
label1.pack()


btnStart = Button(root, width=15, font=20, text='START', command=start_tick)
btnStop = Button(root, width=15, font=20, text='STOP')
btnContinue = Button(root, width=15, font=20, text='CONTINUE')
btnReset = Button(root, width=15, font=20, text='RESET')
btnStart.pack()


root.mainloop()

