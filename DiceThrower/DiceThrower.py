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
window.title("Dice Thrower")
mainframe = ttk.Frame(window, padding='3 3 12 12')
mainframe.grid(
window.columnconfigure(0, 1)
window.rowconfigure(0, 1)
window.mainloop()