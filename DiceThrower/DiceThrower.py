import random
import Tkinter
import ttk

def DiceThrow(times, sides):
    result = 0
    try:
        for x in times:
            result += random.randint(1, sides)
    except ValueError:
        pass
    return result

window = Tkinter.Tk()
mainframe = 
