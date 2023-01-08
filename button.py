import time
import tkinter as tk
import random
from _datetime import datetime

count = 0
temp = 0
after_id = ''


def press_button():
    print('button is pressed')


# def click_counter():                      # функция подсчета нажатий на кнопку
#     global count
#     count += 1
#     label_3.configure(text=count)


def change_label():                            # функция изменения надписи и цвета label
    bg_list = ['red', 'green', 'blue', 'orange']
    txt_list = ['yahoo! Done!', 'Already done', 'Done! do not annoy me!', 'Done! You are cool!']
    label_1.configure(text=random.choice(txt_list), bg=random.choice(bg_list))


def color_bg():                              # функция изменения цвета окна
    color_name = ['#B2FF66', '#CC99FF', '#E0E0E0', '#FF9999', '#3399FF']
    win.config(bg=random.choice(color_name))
#     time.sleep(2)


def tick():
    global temp, after_id
    after_id = win.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
    label_5.configure(text=str(f_temp))
    temp += 1


def start_tick():
    btn_1.pack_forget()
    btn_2.pack()
    tick()


def stop_tick():
    btn_2.pack_forget()
    btn_3.pack()
    btn_4.pack()
    win.after_cancel(after_id)


def continue_tick():
    btn_3.pack_forget()
    btn_4.pack_forget()
    btn_2.pack()
    tick()


def reset_tick():
    global temp
    temp = 0
    label_5.configure(text='00:00')
    btn_3.pack_forget()
    btn_4.pack_forget()
    btn_1.pack()


#def random_color():
#    colors = ['white', 'red', 'orange', 'yellow', 'lime', 'green', 'violet', 'pink']
#    btn_1['bg'] = random.choice(colors)       # случайный цвет фона кнопки
#    btn_1['fg'] = random.choice(colors)       # случайный цвет текста кнопки


win = tk.Tk()
photo = tk.PhotoImage(file='fun.png')
win.iconphoto(False, photo)
win.config(bg='#CCFFFF')
win.title("Observing window")
win.geometry('300x300+50+50')
win.resizable(False, False)


label_1 = tk.Label(win,
                   text='Hello!\n Press the button',
                   bg='white',
                   fg='black',
                   )
label_1.pack()


# entry = tk.Entry(win)
# entry.pack()


btn_1 = tk.Button(win,
                  text='START',
                  bg='white',
                  activebackground='grey',
                  command=lambda:[change_label(), color_bg(), start_tick()]
                  )
btn_1.pack()


btn_2 = tk.Button(win,
                  text='STOP',
                  bg='white',
                  activebackground='grey',
                  command=lambda:[stop_tick(), color_bg()]
                  )


btn_3 = tk.Button(win,
                  text='continue',
                  bg='white',
                  command=lambda:[continue_tick(), color_bg()]
                  )


btn_4 = tk.Button(win,
                  text='RESET',
                  bg='white',
                  command=lambda:[reset_tick(), color_bg()]
                  )


# label_2 = tk.Label(win,
#                    text='total number of clicks on the button',
#                    font='Arial 10 bold'
#                    )
# label_2.pack()


# label_3 = tk.Label(win,
#                    text='0',
#                    font='Arial 20 bold'
#                    )
# label_3.pack()


label_4 = tk.Label(win,
                   text='Time counter',
                   font='Arial 10 bold'
                   )
label_4.pack()


label_5 = tk.Label(win,
                   text='00:00',
                   font='Arial 20 bold'
                   )
label_5.pack()


win.mainloop()
