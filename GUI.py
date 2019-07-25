from tkinter import *
from multpleScattering import * 
import math
window = Tk()
frame = Frame()
window.title("GUI")


program = multpleScattering()
X, Y, Phi = 0,0,0
Dx, Dy, dPhi = 0,0,0


designPosLabel = Label(window, text="Enter Design Pos:").grid(row=1, column=0)
actualPosLabel =Label(window, text="Enter Actual Pos:").grid(row=3, column=0)

xLabel = Label(window,text="X").grid(row=0,column=1)
yLabel = Label(window,text="Y").grid(row=0,column=2)
phiLabel = Label(window,text="Phi").grid(row=0,column=3)
blank = Label(window,text="").grid(row=5,column=3)

DXLabel = Label(window,text="DX").grid(row=2,column=1)
DYLabel = Label(window,text="DY").grid(row=2,column=2)
DPhiLabel = Label(window,text="DPhi").grid(row=2,column=3)

xEntry = Entry(window)
xEntry.grid(row=1,column=1)
xEntry.insert(0, "50")
yEntry = Entry(window)
yEntry.grid(row=1,column=2)
yEntry.insert(0, "25")
phiEntry = Entry(window)
phiEntry.grid(row=1,column=3)
phiEntry.insert(0, "90")

dxEntry = Entry(window)
dxEntry.grid(row=3,column=1)
dxEntry.insert(0, "0")
dyEntry = Entry(window)
dyEntry.grid(row=3,column=2)
dyEntry.insert(0, "0")
dPhiEntry = Entry(window)
dPhiEntry.grid(row=3,column=3)
dPhiEntry.insert(0, "0")
StartBtn = Button(window,text="Start", command=lambda: StartIsPressed()).grid(row=6,column=1)
EndBtn = Button(window, text="End", command=lambda: EndIsPressed()).grid(row=6, column=3)

def StartIsPressed():
	print("Pressed")
	submit_data()
	program.start(X, Y, Phi, Dx, Dy, dPhi)
#def EndIsPressed():

def submit_data():
	X = xEntry.get()
	Y = yEntry.get()
	Phi = float(phiEntry.get())*(math.pi/180)
	DX = dxEntry.get()
	DY = dyEntry.get()
	dPhi = float(dPhiEntry.get())*(math.pi/180)

window.mainloop()