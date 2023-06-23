from parametrs import COMMANDS

#A program for checking the text, in case the user enters some incomprehensible text!
def text_check01(mess):
    counter = 0
    for i in COMMANDS:
        if mess == i:
            counter += 1
    if counter == 0:
        return True
    else:
        return False