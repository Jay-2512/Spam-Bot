
from tkinter import *
from pynput.keyboard import Key,Controller
import time


class mainBody():
    def biscuit():
        #--variables--#
        keyboard = Controller()
        




        #-- tkinter main window--#
        
        root = Tk()
        root.title('')
        root.geometry('500x550')
        root.resizable(False,False)



        def start_timer():
            time.sleep(0.5)
            start_spam(count,message)


        #--main function--#

        def start_spam(count, message):
            time.sleep(7)
            lim = 0
            while(count > lim):
                for letter in message:
                    keyboard.press(letter)
                    keyboard.release(letter)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                lim = lim + 1

        #--get message--function--#
        def get_message():
            global message
            message = get_messageEntry.get()
            get_requirementsConfirm.config(text="Got the message!")
            print("[+] Got the message !")

        #--get count--function--#
        def get_count():
            global message
            global count
            right = False
            count = get_countEntry.get()
            try:
                count = int(count)
                right = True
            except ValueError:
                print("[!] YO!! Thats not a number.. such a weirdo..")
                get_requirementsConfirm.config(text="TBH, That's not a number... Try again")
            if right == True:
                get_requirementsConfirm.config(text="Count Accepted!!")
                time.sleep(1)
                #print(message)
                #print(count)
                print('[+] Got the count!')
                final_message.config(text="Press the start button and place your cursor at the target location\nSpamming will start soon!")
                return count

        #--value reset--#
        def value_reset():
            global count,message
            get_countEntry.delete(first=0,last=100)
            get_messageEntry.delete(first=0, last=100)
            count = 1
            message = NONE
            print("[!!] Erasing all stuffs from the memory! ")

        #--Labels --#
        heading = Label(root,text="S P A M M Y")
        heading.config(font=("Courier", 33))
        heading.pack()
        footer = Label(root,text="NYX-Tech").pack(side=BOTTOM)

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

        get_messageButton = Button(root,text="Give Message",command=get_message)
        get_messageButton.pack()

        #--get count label--#
        get_countLabel = Label(root, text="Enter the count : ")
        get_countLabel.config(font=("Arial",15))
        get_countLabel.pack(pady=10)

        #--get count entry--#

        get_countEntry = Entry(root, width="50")
        get_countEntry.pack(pady=10)

        #--get count button--#

        get_countButton = Button(root,text="Give Count", command=get_count)
        get_countButton.pack()

        #--confirmation labels--#

        get_requirementsConfirm = Label(root, text="")
        get_requirementsConfirm.pack(pady=10)

        final_message = Label(root,text="")
        final_message.pack(pady=10)

        #-- start timer button--#

        start_timerButton = Button(root, text="Start!", command=start_timer)
        start_timerButton.pack(pady=20)

        #--reset button--#
        value_resetButton = Button(root,text="Reset!",command=value_reset)
        value_resetButton.pack(padx=10, side=LEFT)

        #--exit button--#
        exit_button = Button(root,text="Exit",command=exit)
        exit_button.pack(padx=10,side=RIGHT)
        print("HEYY!!\nVisit our blog : https://nyx-tech@blogspot.com")



        root.mainloop()
