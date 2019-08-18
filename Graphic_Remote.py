from tkinter import *
import matplotlib.pyplot as plt
from AI_Remote import *
import easygui as e
import datetime, os, math


fig, axs = plt.subplots(3, sharex=True, sharey=True, figsize = (10,6), gridspec_kw={'hspace': 0})
fig.suptitle('Sharing both axes')
fig.figsize=10,6

axs[0].margins(0.05)
axs[0].set_xlim([0,100])
axs[0].set_ylim([-200, 200])

axs[1].margins(0.05)
axs[1].set_xlim([0,100])
axs[1].set_ylim([-200, 200])

axs[2].margins(0.05)
axs[2].set_xlim([0,100])
axs[2].set_ylim([-200, 200])
for ax in axs:
	ax.label_outer()
window = Tk()
window.title("GUI")


AI_remote = AI_Remote(fig, axs[0], axs[1], axs[2])
X, Y, Phi = 0,0,0
Dx, Dy, dPhi = 0,0,0
count = 0

designPosLabel = Label(window, text="Enter Design Pos:").grid(row=3, column=0)
actualPosLabel =Label(window, text="Enter Actual Range:").grid(row=5, column=0)
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
phiEntry.config(state='readonly')

dxEntry = Entry(window)
dxEntry.grid(row=5,column=1)
dxEntry.insert(0, "0,5,5")
dyEntry = Entry(window)
dyEntry.grid(row=5,column=2)
dyEntry.insert(0, "0,0,0")
dPhiEntry = Entry(window)
dPhiEntry.grid(row=5,column=3)
dPhiEntry.insert(0, "0,0,0")
StartBtn = Button(window,text="Start", command=lambda: start()).grid(row=9, column=1)
ShowBtn = Button(window, text="Show", command=lambda: showPlots()).grid(row=9, column=3)
LogBtn = Button(window, text="Log", command=lambda: showLog()).grid(row = 9, column=2)

def start():
	#progressWindow = Tk()
	#progressWindow.title = "Progress"
	print("start")
	#nJobs = 0
	#xI, xF, xB, yI, yF, yB, pI, pF, pB = 0,0,0,0,0,0,0,0,0
	#getRanges(xI, xF, xB, yI, yF, yB, pI, pF, pB, nJobs)
	dxValues = str(dxEntry.get()).split(',')
	dyValues = str(dyEntry.get()).split(',')
	dpValues = str(dPhiEntry.get()).split(',')
	xI, xF, xB = float(dxValues[0]), float(dxValues[1]), float(dxValues[2])
	yI, yF, yB = float(dyValues[0]), float(dyValues[1]), float(dyValues[2])
	pI, pF, pB = float(dpValues[0]), float(dpValues[1]), float(dpValues[2])
	print(xI, xF, xB, yI, yF, yB, pI, pF, pB)
	AI_remote.start(float(xEntry.get()), float(yEntry.get()), float(phiEntry.get())*(math.pi/180), xI, xF, xB, yI, yF, yB, pI, pF, pB, int(lengthEntry.get()), float(accuracyEntry.get()))
def showLog():
	try:
		AI_remote.showLog()
	except:
		e.msgbox('Cannot open Log', 'wait until program is finished')
def showPlots():
	AI_remote.showPlots()
	e.msgbox('Cannot show Plots', 'wait until program is finished')
window.mainloop()