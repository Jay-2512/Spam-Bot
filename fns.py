from pynput.keyboard import Key, Controller
import time


class main_functions:

    def start_spam(message, count):

        keyboard = Controller()

        time.sleep(5)
        lim = 0
        while(count > lim):
            for letter in message:
                keyboard.press(letter)
                keyboard.release(letter)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            lim = lim + 1

    def start_timer(get_messageEntry, get_countEntry, get_requirementsConfirm):
        time.sleep(0.5)
        message = get_messageEntry.get()
        print(message)
        
        count = int(get_countEntry.get())
        print(type(count))

        print(count)

        if message != "" and count > 0:
            main_functions.start_spam(message, count)
        elif message == "":
            print("[!] Message field looks like its empty!")
            get_requirementsConfirm(text='Message Field is Empty please fill it!!')
        elif count == 1:
            print("[!] Count value not entered! Will be using the default value : 1")

    
    def get_message(get_messageEntry, get_requirementsConfirm):

            message = None
            message = get_messageEntry.get()
            if message == "":
                get_requirementsConfirm.config(text="Whoops! That will be treated as a space...\n Re-Enter")
            else:
                get_requirementsConfirm.config(text="Gotcha!")
                print("[+] Got the message !")

    def get_count(get_countEntry, get_requirementsConfirm, final_message):

            right = False
            count = 1 #default
            count = get_countEntry.get()
            count = int(count)
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

    def value_reset(get_countEntry, get_messageEntry, get_requirementsConfirm, final_message):

            get_countEntry.delete(first=0,last=100)
            get_messageEntry.delete(first=0, last=100)
            count = 1
            message = None
            get_requirementsConfirm.config(text="")
            final_message.config(text="")
            print("[!!] Erasing all stuffs from the memory! ")
 