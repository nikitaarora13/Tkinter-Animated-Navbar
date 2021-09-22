from tkinter import *
from tkinter import PhotoImage


# setting root window:
root = Tk()
root.title('Animated Navbar')
root.geometry('350x500')

# setting button state
btn_state = False

# get icon image
nav_icon = PhotoImage(file = 'bar.png')
close_icon = PhotoImage(file = 'close.png')

def switch():
    global btn_state
    if btn_state is True:
        # close navbar
        for x in range(251):
            NavBar.place(x=-x, y=0)
            frame.update()
        frame.config(bg='black')

        # set button state off
        btn_state = False

    else:
        # open NavBar
        for x in range(-250, 0):
            NavBar.place(x=x, y=0)
            frame.update()
        frame.config(bg='SystemButtonFace')

        # set button state ON
        btn_state = True

# frame for NavBar icon
frame = Frame(root, bg='black')
frame.pack(side='top', fill=X)

# NavBar button
navbar_btn = Button(frame, image=nav_icon, bg='black', bd=0, command=switch)
navbar_btn.grid(row=1,column=1)

# label to display selected menu option
label = Label(root, font='ariel 18 bold')
label.place(x=60, y=250)

# frame for NavBar
NavBar = Frame(root, bg='black', height=1000, width=250)
NavBar.place(x=-250, y=0)

def option_selected(msg):
    switch()
    label.config(text=msg)


# NavBar options
option1 = Button(NavBar, text='C++', font='ariel 18 bold', bg='black', fg='white', activebackground='gray',
                activeforeground='white', bd=0, command=lambda msg=' you have selected C++':
                option_selected(msg)).place(x=25, y=60)

option2 = Button(NavBar, text='Java', font='ariel 18 bold', bg='black', fg='white', activebackground='grey',
                activeforeground='white', bd=0, command=lambda msg=' you have selected Java':
                option_selected(msg)).place(x=25, y=120)

option3 = Button(NavBar, text='Python', font='ariel 18 bold', bg='black', fg='white', activebackground='grey',
                activeforeground='white', bd=0, command=lambda msg=' you have selected Python':
                option_selected(msg)).place(x=25, y=180)


# NavBar close Button
close_btn = Button(NavBar, image=close_icon, bg='black', bd=0, command=switch)
close_btn.place(x=200, y= 5)

root.mainloop()
