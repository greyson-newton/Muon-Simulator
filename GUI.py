from tkinter import *


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class GUI:
	def __init__(self, length, initX, initY, initPhi, delX, delY, delPhi, initSimSpeed, isProgramOn):
	
		self.length, self.initX, self.initX, self.initY = length, initX, initY, initPhi
		self.delX, self.delY, self.delPhi = delX, delY, delPhi
		self.initSimSpeed = initSimSpeed
		self.isProgramOn = isProgramOn

	
	def setUpGUI(self):
		
				
		tb1 = DoubleVar()
		tb2 = IntVar()
		tb3 = IntVar()
		tb4 = IntVar()
		tb5 = DoubleVar()
		tb6 = IntVar()
		tb7 = IntVar()
		tb8 = DoubleVar()
		
		window = Tk()
		window.title("GUI")
		window.geometry("800x200")
		
		# Simulation Speed
		Label(window,text="Simulation Speed").grid(row=0,column=0)
		Entry(window, textvariable = tb1).grid(row=0,column=1)

		# Length
		Label(window,text="Length").grid(row=0,column=3)
		Entry(window, textvariable = tb2).grid(row=0,column=4)


		# Init Pos
		Label(window,text="InitX").grid(row=1,column=0)
		Entry(window, textvariable=tb3).grid(row=1,column=1)

		Label(window,text="InitY").grid(row=1,column=2)
		Entry(window, textvariable=tb4).grid(row=1,column=3)

		Label(window,text="InitPhi").grid(row=1,column=4)
		Entry(window, textvariable=tb5).grid(row=1,column=5)


		# Del Pos
		Label(window,text="delX").grid(row=2,column=0)
		Entry(window, textvariable=tb6).grid(row=2,column=1)

		Label(window,text="delY").grid(row=2,column=2)
		Entry(window, textvariable=tb7).grid(row=2,column=3)

		Label(window,text="delPhi").grid(row=2,column=4)
		Entry(window, textvariable=tb8).grid(row=2,column=5)

		# Parameters for alignment


		# Start SIM Button
		StartBtn = Button(window,text="Start SIM", command=lambda: StartIsPressed()).grid(row=3,column=0)

	
	def StartIsPressed(self):
		print("Pressed")
		self.initSimSpeed = tb1.get()
		self.length = tb2.get()
		self.initX = int(tb3.get())
		self.initY = int(tb4.get())
		self.initPhi = int(tb5.get())
		self.delX = int(tb6.get())
		self.delY = int(tb7.get())
		self.delPhi = int(tb7.get())
		print(self.initSimSpeed)
		print(self.initX)
		self.isProgramOn = True
	

	
	



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


	

	

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

