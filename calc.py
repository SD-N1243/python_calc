import time
from tkinter import *
import tkinter as tk

def test(a, d):
    # check if a and d are numbers
    if isinstance(a, (int, float)) and isinstance(d, (int, float)):
        # add a and d together and return the result
        return (a + d)
    else:
        # raise an exception if a or d is not a number
        raise TypeError("a and d must be numbers")


# Get user input and validate it
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    num1 = float(num1)
    num2 = float(num2)

    # Calculate the result
    result = test(num1, num2)

    num1 = int(num1)
    num2 = int(num2)

except ValueError:
    print(f"Error: {num1} and {num2} are most likely not valid numbers")
    print("Script will exit in 10 seconds")
    time.sleep(10)
    exit()

# Create the GUI window
window = Tk()
window.title("Result")
window.iconbitmap("calc.ico")

label2 = tk.Label(window, text="that is " + str(result), height="9", font=("comic sans MS", "20"))
label2.pack()

window.geometry("459x300")
window.mainloop()