from tkinter import *
from fns import *


class main_window:

    def __init__(self):
        root = Tk()
        root.title('')
        root.geometry('500x550')
        root.resizable(False,False)

        #--Labels --#
        heading = Label(root,text="S P A M M Y")
        heading.config(font=("Courier", 33))
        heading.pack()
        footer = Label(root,text="github.com/Jay-2512").pack(side=BOTTOM)

        #--underline--#
        underlineLabel = Label(root,text="-------------------------------------")
        underlineLabel.config(font=("Courier", 44))
        underlineLabel.pack()

        #--get message label--#
        get_messageLabel = Label(root, text="Enter the message : ")
        get_messageLabel.config(font=("Arial",15))
        get_messageLabel.pack(pady=10)



        #--get message entry--#

        get_messageEntry = Entry(root, width="50")
        get_messageEntry.pack(pady=10)


        #--get message button--#

        get_messageButton = Button(root,text="Give Message",command= lambda : main_functions.get_message(get_messageEntry, get_requirementsConfirm))
        get_messageButton.pack()

        #--get count label--#
        get_countLabel = Label(root, text="Enter the count : ")
        get_countLabel.config(font=("Arial",15))
        get_countLabel.pack(pady=10)

        #--get count entry--#

        get_countEntry = Entry(root, width="50")
        get_countEntry.pack(pady=10)

        #--get count button--#

        get_countButton = Button(root,text="Give Count", command=lambda : main_functions.get_count(get_countEntry, get_requirementsConfirm, final_message))
        get_countButton.pack()

        #--confirmation labels--#

        get_requirementsConfirm = Label(root, text="")
        get_requirementsConfirm.pack(pady=10)

        final_message = Label(root,text="")
        final_message.pack(pady=10)

        #-- start timer button--#

        start_timerButton = Button(root, text="Start!", command=lambda : main_functions.start_timer(get_messageEntry, get_countEntry, get_requirementsConfirm))
        start_timerButton.pack(pady=20)

        #--reset button--#
        value_resetButton = Button(root,text="Reset!",command=lambda : main_functions.value_reset(get_countEntry, get_messageEntry, get_requirementsConfirm, final_message))
        value_resetButton.pack(padx=10, side=LEFT)

        #--exit button--#
        exit_button = Button(root,text="Exit",command = exit)
        exit_button.pack(padx=10,side=RIGHT)
        print("HEYY!!\nVisit our blog : https://nyx-tech@blogspot.com")



        root.mainloop()