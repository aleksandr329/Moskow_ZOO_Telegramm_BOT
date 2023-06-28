from parametrs import COMMANDS

#A program for checking the text, in case the user enters some incomprehensible text!
def text_check01(mess):
    if mess in COMMANDS:
        return False
    else:
        return True