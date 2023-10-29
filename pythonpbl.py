from tkinter import *
root = Tk()

# Title for the Quadratic Equation Solver
root.title("Quadratic Equation Solver...")

stva = StringVar()

#Variable to store roots
vtsr = 0

# Taking the coefficients of the Quadratic Equation
st1 = Label(root, text="Enter the values of the Coefficients of the Quadratic Equation")
st1.grid(row=0, column=0, columnspan=2)
coa = Label(root, text="a = ")
coa.grid(row=1, column=0)
cob = Label(root, text="b = ")
cob.grid(row=2, column=0)
coc = Label(root, text="c = ")
coc.grid(row=3, column=0)

mainloop()
