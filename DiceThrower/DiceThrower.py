import random
import Tkinter
import ttk

def DiceThrow(*args):
    try:
        times = int(NumberOfDice.get())
        sides = int(NumberOfSides.get())
        result = 0
        for x in range(times):
            result += random.randint(1, sides)
        ThrowResult.set(result)
    except ValueError:
        pass

window = Tkinter.Tk()
window.title("Dice Thrower")

mainframe = ttk.Frame(window, padding='3 3 12 12')
mainframe.grid(column=0, row=0)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

NumberOfDice = Tkinter.IntVar()
NumberOfSides = Tkinter.IntVar()
ThrowResult = Tkinter.IntVar()

DiceInput = ttk.Entry(window, width=4, textvariable=NumberOfDice)
DiceInput.grid(column=1, row=1)

ttk.Label(window, textvariable='d').grid(column=2, row=2)

SideInput = ttk.Entry(window, width=4, textvariable=NumberOfSides)
SideInput.grid(column=3, row=1)

ttk.Button(window, text="Throw!", command=DiceThrow).grid(column=4, row=1)
ttk.Label(window, textvariable="The result of the throw is").grid(column=1, row=2)
ttk.Label(window, textvariable=ThrowResult).grid(column=3, row=2)

window.mainloop()