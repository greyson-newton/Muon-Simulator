from tkinter import *
from multpleScattering import * 
import math
import datetime
import os

window = Tk()
window.title("GUI")
filename = "log_" + str(datetime.date.today()) + "_.txt"

try:
	log = open(filename, "w+")
except:
	print("log cant open")


program = multpleScattering()
X, Y, Phi = 0,0,0
Dx, Dy, dPhi = 0,0,0
count = 0

designPosLabel = Label(window, text="Enter Design Pos:").grid(row=3, column=0)
actualPosLabel =Label(window, text="Enter Actual Pos:").grid(row=5, column=0)
blank1 = Label(window,text="").grid(row=6,column=3)

xLabel = Label(window,text="X").grid(row=2,column=1)
yLabel = Label(window,text="Y").grid(row=2,column=2)
phiLabel = Label(window,text="Phi").grid(row=2,column=3)

DXLabel = Label(window,text="DX").grid(row=4,column=1)
DYLabel = Label(window,text="DY").grid(row=4,column=2)
DPhiLabel = Label(window,text="DPhi").grid(row=4,column=3)

accuracyLabel = Label(window, text="Accuray").grid(row = 0, column = 1)
lengthLabel = Label(window, text="Length").grid(row=0, column=3)
blank = Label(window,text="").grid(row=8,column=3)
timeLabel = Label(window, text="Time Elapsed:").grid(row = 7, column = 1)

accuracyEntry = Entry(window)
accuracyEntry.grid(row=1, column=1)
accuracyEntry.insert(0, "0.0001")
lengthEntry = Entry(window)
lengthEntry.grid(row=1, column = 3)
lengthEntry.insert(0, "100")
timeResult = Entry(window)
timeResult.grid(row = 7, column = 2)


xEntry = Entry(window)
xEntry.grid(row=3,column=1)
xEntry.insert(0, "50")
yEntry = Entry(window)
yEntry.grid(row=3,column=2)
yEntry.insert(0, "0")
phiEntry = Entry(window)
phiEntry.grid(row=3,column=3)
phiEntry.insert(0, "90")

dxEntry = Entry(window)
dxEntry.grid(row=5,column=1)
dxEntry.insert(0, "5")
dyEntry = Entry(window)
dyEntry.grid(row=5,column=2)
dyEntry.insert(0, "0")
dPhiEntry = Entry(window)
dPhiEntry.grid(row=5,column=3)
dPhiEntry.insert(0, "0")
StartBtn = Button(window,text="Start", command=lambda: StartIsPressed()).grid(row=9, column=1)
EndBtn = Button(window, text="Reset", command=lambda: ResetIsPressed()).grid(row=9, column=3)
ShowBtn = Button(window, text="Log", command=lambda:ShowIsPushed()).grid(row = 9, column=2)

def StartIsPressed():
	global count
	count+=1
	print(count, "\n", file=log)
	print(str(xEntry.get()) , ",", str(yEntry.get()), "," , str(float(phiEntry.get())*(math.pi/180)) , ",", str(dxEntry.get()) , "," , str(dyEntry.get()) , ",", str(float(dPhiEntry.get())*(math.pi/180)), ",", str(accuracyEntry.get()), "\n", file=log)
	program.start(float(xEntry.get()), float(yEntry.get()), float(phiEntry.get())*(math.pi/180),  float(dxEntry.get()),  float(dyEntry.get()), float(dPhiEntry.get())*(math.pi/180), int(lengthEntry.get()), float(accuracyEntry.get()))
	if program.chamber1.isDone():
		timeResult.insert(0, str(program.returnTime()))

def ResetIsPressed():
	print(timeResult.get(), "\n", file=log)
	timeResult.delete(0, END)
	program.reset()
def ShowIsPushed():
	global filename
	log.close()
	os.startfile(filename)
window.mainloop()