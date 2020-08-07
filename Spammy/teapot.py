from pynput.keyboard import Key, Controller
from tkinter import *
import time

keyboard = Controller()

class mainBody:
    def biscut():
        root = Tk()
        root.title('Spam Bot')
        root.geometry("500x500")
        root.resizable(False,False)

        # functions :
        def start_timer():
            flag = 0
            time.sleep(0.5)
            start_spam(count, message)
            timer_msg.config(text="Spam Completed \n GG!")


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

        def count_accpt(    ):
            global count
            count = 0
            count = get_count.get()
            try:
                count = int(count)
            except ValueError:
                msg_conf.config(text="Enter a number -_-").pack()

            msg_conf.config(text='Count... Ahah! Got it!!')
            msg_conf.config(text="All set..\nClick the button to start a 7 sec timer")
            timer_msg.config(text="Your Spamming will start soon..\n Press the confirm button and \nPlace the cursor where you want to spam")
            confirm_button = Button(text="Confirm", command=start_timer)
            confirm_button.pack(pady=10)


        def msg_accpt():
            global message
            message = get_message.get()
            msg_conf.config(text='Got the message!')



        # window settings
        #root.title('Spam Bot')
        #root.geometry("500x500")
        #root.resizable(False,False)

        # Label
        main_label = Label(root,text="SPAMMY").pack()
        bottom_label = Label(root,text="NYX-Tech").pack(side=BOTTOM)

        #Entry box and other :p :

        l1 = Label(root,text="Enter your message").pack(pady=10)
        get_message = Entry(root, width='50')
        get_message.pack(pady=10)
        accept_message = Button(root, text="Give message",command=msg_accpt)
        accept_message.pack(pady=10)
        l2 = Label(root,text="Enter your count").pack(pady=10)
        get_count = Entry(root, width='50')
        get_count.pack(pady=10)
        accept_count = Button(root, text="Give count",command=count_accpt)
        accept_count.pack(pady=10)


        # Additional Labels :

        msg_conf = Label(root, text='')
        msg_conf.pack()
        timer_msg = Label(root, text='')
        timer_msg.pack()
        root.mainloop()
