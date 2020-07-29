import os

class system:
    def __init__(self):
        os.system('clear')

        text = open("shhh.txt","r",encoding="utf8")

        lines = text.readlines()

        for line in lines:
            print(line)
