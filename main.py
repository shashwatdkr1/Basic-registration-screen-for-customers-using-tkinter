from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Registration Form")
root.geometry("400x400")
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
custIdLabel = ttk.Label(frame, text="Customer ID")
custIdLabel.grid(column=0, row=0, sticky=W)
custId = ttk.Entry(frame)
custId.grid(column=1, row=0, sticky=(W, E))
nameLabel = ttk.Label(frame, text="Customer Name")
nameLabel.grid(column=0, row=1, sticky=W)
name = ttk.Entry(frame)
name.grid(column=1, row=1, sticky=(W, E))
branchLabel = ttk.Label(frame, text="Branch")
branchLabel.grid(column=0, row=2, sticky=W)
branch = ttk.Entry(frame)
branch.grid(column=1, row=2, sticky=(W, E))
branch.insert(0, "adyar")
accountTypeLabel = ttk.Label(frame, text="Account Type")
accountTypeLabel.grid(column = 0,row = 3, sticky=W)
savingsRadioButton = ttk.Radiobutton(frame,text = "Savings",value=0)
savingsRadioButton.grid(column=1, row=3, sticky=(W, E))
currentRadioButton = ttk.Radiobutton(frame,text = "Current",value=1)
currentRadioButton.grid(column=2, row=3, sticky=(W, E))
amountLabel = ttk.Label(frame,text = "Amount")
amountLabel.grid(column = 0, row = 4, sticky = W)
amountSpinbox = ttk.Scale(frame,from_=0,to=20000)
amountSpinbox.grid(column=1, row=4, sticky=(W, E))
amountSpinbox.set("1000")
insertButton = ttk.Button(frame, text="Insert")
insertButton.grid(column=0, row=5, sticky=(W, E))
updateButton = ttk.Button(frame, text="Update")
updateButton.grid(column=1, row=5, sticky=(W, E))
deleteButton = ttk.Button(frame, text="Delete")
deleteButton.grid(column=0, row=6, sticky=(W, E))
selectButton = ttk.Button(frame, text="Select")
selectButton.grid(column=1, row=6, sticky=(W, E))
root.mainloop()