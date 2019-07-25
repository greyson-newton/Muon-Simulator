from tkinter import *
from multpleScattering import * 

class GUI:
	program = multpleScattering()
	X, Y, Phi = 0,0,0
	Dx, Dy, dPhi = 0,0,0

	window = Tk()
	window.title("GUI")
	window.geometry("800x200")

	vcmdX = window.register(validateX)
	vcmdY = window.register(validateY)
	vcmdPhi = window.register(validatePhi)
	vcmdDx = window.register(validateDx)
	vcmdDy = window.register(validateDy)
	vcmdDphi = window.register(validateDp)

	designPosLabel = Label(window, text="Enter Design Pos:").grid(row=1, column=0)
	actualPosLabel =Label(window, text="Enter Actual Pos:").grid(row=3, column=0)

	xLabel = Label(window,text="X").grid(row=0,column=1)
	yLabel = Label(window,text="Y").grid(row=0,column=2)
	phiLabel = Label(window,text="Phi").grid(row=0,column=3)

	dxLabel = Label(window,text="DX").grid(row=2,column=1)
	dyLabel = Label(window,text="DY").grid(row=2,column=2)
	dPhiLabel = Label(window,text="DPhi").grid(row=2,column=3)

	xEntry = Entry(window, validate="key", validatecommand=(vcmdX, '%P')).grid(row=1,column=1)
	yEntry = Entry(window, validate="key", validatecommand=(vcmdY, '%P')).grid(row=1,column=3)
	phiEntry = Entry(window, validate="key", validatecommand=(vcmdPhi, '%P')).grid(row=1,column=5)

	dxEntry = Entry(window, validate="key", validatecommand=(vcmdDx, '%P')).grid(row=2,column=1)
	dyEntry = Entry(window, validate="key", validatecommand=(vcmdDy, '%P')).grid(row=2,column=3)
	dPhiEntry = Entry(window, validate="key", validatecommand=(vcmdDphi, '%P')).grid(row=2,column=5)

	StartBtn = Button(window,text="Start", command=lambda: StartIsPressed()).grid(row=4,column=0)
	EndBtn = Button(window, text="End", command=lambda: EndIsPressed()).grid(row=4, column=2)

	def StartIsPressed():
		print("Pressed")
		program.start(X, Y, Phi, Dx, Dy, Dp)

	def validateX(var):
		new_value = var.get()
		if not(new_value is None):
			try:
				X = float(new_value)
			except NameError:
				raise ValueError("Detected Input But Could Not Append to Variable")
	def validateY( var):
		new_value = var.get()
		if not(new_value is None):
			try:
				Y = float(new_value)
			except NameError:
				raise ValueError("Detected Input But Could Not Append to Variable")
	def validatePhi( var):
		new_value = var.get()
		if not(new_value is None):
			try:
				Phi = float(new_value)
			except NameError:
				raise ValueError("Detected Input But Could Not Append to Variable")
	def validateDx( var):
		new_value = var.get()
		if not(new_value is None):
			try:
				Dx = float(new_value)
			except NameError:
				raise ValueError("Detected Input But Could Not Append to Variable")
	def validateDy( var):
		new_value = var.get()
		if not(new_value is None):
			try:
				Dy = float(new_value)
			except NameError:
				raise ValueError("Detected Input But Could Not Append to Variable")
	def validateDphi( var):
		new_value = var.get()
		if not(new_value is None):
			try:
				Dphi = float(new_value)
			except NameError:
				raise ValueError("Detected Input But Could Not Append to Variable")


	#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


	

	

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

