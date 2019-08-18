import numpy as np
import os, math
from GraphicMultpleScattering import *
from multpleScattering import *
import matplotlib.pyplot as plt
from tqdm import tqdm_gui
import datetime

class AI_Remote:
	def __init__(self, figure1, sub1, sub2, sub3):
		self.sub1, self.sub2, self.sub3 = sub1, sub2, sub3
		self.figure1 = figure1
		self.filename = "log_" + str(datetime.date.today()) + "_.txt"

		try:
			self.log = open(self.filename, "w+")
		except:
			print("log cant open")

	def start(self, x, y, phi, xI, xF, xB, yI, yF, yB, pI, pF, pB, Length, Accuracy):

		print("Remote Working")
		self.x, self.y, self.phi = x, y, phi

		self.xI, self.xF, self.xB, self.yI, self.yF, self.yB, self.pI, self.pF, self.pB = int(xI), int(xF), int(xB), int(yI), int(yF), int(yB), int(pI), int(pF), int(pB)

		self.DxRange = np.linspace(self.xI,self.xF,self.xB, endpoint = True)
		self.DyRange = np.linspace(self.yI,self.yF,self.yB, endpoint = True)
		self.DpRange = np.linspace(self.pI,self.pF,self.pB, endpoint = True)
		print(self.DxRange)
		print(self.DyRange)
		print(self.DpRange)

		self.Length, self.Accuracy = Length, Accuracy

		self.times, self.xPos, self.yPos, self.phiPos =[], [], [], []
		self.DxPos, self.DyPos, self.DphiPos = [], [], []
		self.charges, self.angles = [], []
		self.count = 0
		if self.xB == 0 and not(self.yB==0 and self.pB==0):
			print("x = 0")
			for dy in range(len(self.DyRange)):
				for dp in range(len(self.DpRange)):
					DxValue = int(self.xF)
					DyValue = int(self.DyRange[dy])
					DpValue = int(self.DpRange[dp])
					program = multpleScattering(x,y,phi,DxValue, DyValue, DpValue, Length, self.Accuracy)
					self.count+=1
					print(self.count)
					self.times.append(program.returnTime())
					self.DxPos.append(DxValue) 
					self.DyPos.append(DyValue) 
					self.DphiPos.append(DpValue)
					self.xPos.append(self.x)
					self.yPos.append(self.y)
					self.phiPos.append(self.phi)
					self.charges.append(program.charge)
					self.angles.append(program.angleInitial)

		if self.yB == 0 and not(self.xB==0 or self.pB==0):
			print("y = 0")
			for dx in range(len(self.DxRange)):
				for dp in range(len(self.DpRange)):
					#print(dx, dy, dp)
					DxValue = int(self.DxRange[dx])
					DyValue = int(self.yF)
					DpValue = int(self.DpRange[dp])
					#print(DxValue)
					program = multpleScattering(x,y,phi,DxValue, DyValue, DpValue, Length, self.Accuracy)
					self.count+=1
					print(self.count)
					self.times.append(program.returnTime())
					self.DxPos.append(DxValue) 
					self.DyPos.append(DyValue) 
					self.DphiPos.append(DpValue)
					self.xPos.append(self.x)
					self.yPos.append(self.y)
					self.phiPos.append(self.phi)
					self.charges.append(program.charge)
					self.angles.append(program.angleInitial)

		if self.pB == 0 and not(self.xB==0 or self.yB==0):
			print("p = 0")
			for dx in range(len(self.DxRange)):
				for dy in range(len(self.DyRange)):
					DxValue = int(self.DxRange[dx])
					DyValue = int(self.DyRange[dy])
					DpValue = int(pF)
					program = multpleScattering(x,y,phi,DxValue, DyValue, DpValue, Length, self.Accuracy)
					self.count+=1
					print(self.count)
					self.times.append(program.returnTime())
					self.DxPos.append(DxValue) 
					self.DyPos.append(DyValue) 
					self.DphiPos.append(DpValue)
					self.xPos.append(self.x)
					self.yPos.append(self.y)
					self.phiPos.append(self.phi)
					self.charges.append(program.charge)
					self.angles.append(program.angleInitial)

		if self.xB==0 and self.yB == 0 and not(self.pB==0):
			print("x & y = 0")
			for dp in range(len(self.DpRange)):
				DxValue = int(self.xF)
				DyValue = int(self.yF)
				DpValue = int(self.DpRange[dp])
				program = multpleScattering(x,y,phi,DxValue, DyValue, DpValue, Length, self.Accuracy)
				self.count+=1
				print(self.count)
				self.times.append(program.returnTime())
				self.DxPos.append(DxValue) 
				self.DyPos.append(DyValue) 
				self.DphiPos.append(DpValue)
				self.xPos.append(self.x)
				self.yPos.append(self.y)
				self.phiPos.append(self.phi)

		if self.yB==0 and self.pB == 0 and not(self.xB==0):
			print("y & p = 0")
			for dx in range(len(self.DxRange)):
				DxValue = int(self.DxRange[dx])
				DyValue = int(self.yF)
				DpValue = int(self.pF)
				program = multpleScattering(x,y,phi,DxValue, DyValue, DpValue, Length, self.Accuracy)
				self.count+=1
				print(self.count)
				self.times.append(program.returnTime())
				self.DxPos.append(DxValue) 
				self.DyPos.append(DyValue) 
				self.DphiPos.append(DpValue)
				self.xPos.append(self.x)
				self.yPos.append(self.y)
				self.phiPos.append(self.phi)

		if self.xB==0 and self.pB == 0 and not(self.yB==0):
			print("x & p = 0")
			for dy in range(len(self.DyRange)):
				DxValue = int(self.xF)
				DyValue = int(self.DyRange[dy])
				DpValue = int(self.pF)
				program = multpleScattering(x,y,phi,DxValue, DyValue, DpValue, Length, self.Accuracy)
				self.count+=1
				print(self.count)
				self.times.append(program.returnTime())
				self.DxPos.append(DxValue) 
				self.DyPos.append(DyValue) 
				self.DphiPos.append(DpValue)
				self.xPos.append(self.x)
				self.yPos.append(self.y)
				self.phiPos.append(self.phi)

		minTimeOne = 100
		minTimeTwo = 100
		minTimeThree = 100

		minCoordinatesOne = []
		minCoordinatesTwo = []
		minCoordinatesThree = []

		self.minTimeOneIndex = 0
		self.minTimeTwoIndex = 0
		self.minTimeThreeIndex = 0

		nJobs = xB + yB + pB

		print("Down Here")
		print(self.xPos)
		print(self.yPos)
		print(self.phiPos)
		print(self.times)
		print(self.charges)
		print(self.angles)

		if nJobs > 3 or nJobs == 3:
			minTimeOne = min(self.times)
			self.minTimeOneIndex = self.times.index(minTimeOne)
			minTimeTwo = sorted(self.times)[-2]
			self.minTimeTwoIndex = self.times.index(minTimeTwo)
			minTimeThree = sorted(self.times)[-3]
			self.minTimeThreeIndex = self.times.index(minTimeThree)
			
			minCoordinatesOne.append(self.xPos[self.minTimeOneIndex])
			minCoordinatesOne.append(self.yPos[self.minTimeOneIndex])
			minCoordinatesOne.append(self.phiPos[self.minTimeOneIndex])

			minCoordinatesTwo.append(self.xPos[self.minTimeTwoIndex])
			minCoordinatesTwo.append(self.yPos[self.minTimeTwoIndex])
			minCoordinatesTwo.append(self.phiPos[self.minTimeTwoIndex])

			minCoordinatesThree.append(self.xPos[self.minTimeThreeIndex])
			minCoordinatesThree.append(self.yPos[self.minTimeThreeIndex])
			minCoordinatesThree.append(self.phiPos[self.minTimeThreeIndex])
			#print(self.minTimeOneIndex, self.minTimeTwoIndex, self.minTimeThreeIndex)
			print("# 1: \n", self.minTimeOneIndex, "st Job",  file = self.log)
			print("Design Position: " ,str(self.xPos[self.minTimeOneIndex]) , ",", str(self.yPos[self.minTimeOneIndex]), "," , str(self.yPos[self.minTimeOneIndex]) , "\nActual Position: ", str(self.DxPos[self.minTimeOneIndex]) , "," , str(self.DyPos[self.minTimeOneIndex]) , ",", str(float(self.DphiPos[self.minTimeOneIndex])*(math.pi/180)), "\n", file=self.log)
			print("Accuracy: ", str(self.Accuracy), "Length: ", str(self.Length), file=self.log)

			print("# 2: \n", self.minTimeTwoIndex, "st Job",  file = self.log)
			print("Design Position: " ,str(self.xPos[self.minTimeTwoIndex]) , ",", str(self.yPos[self.minTimeTwoIndex]), "," , str(self.yPos[self.minTimeTwoIndex]) , "\nActual Position: ", str(self.DxPos[self.minTimeTwoIndex]) , "," , str(self.DyPos[self.minTimeTwoIndex]) , ",", str(float(self.DphiPos[self.minTimeTwoIndex])*(math.pi/180)), "\n", file=self.log)
			print("Accuracy: ", str(self.Accuracy), "Length: ", str(self.Length), file=self.log)

			print("# 3: \n", self.minTimeThreeIndex, "st Job",  file = self.log)
			print("Design Position: " ,str(self.xPos[self.minTimeThreeIndex]) , ",", str(self.yPos[self.minTimeThreeIndex]), "," , str(self.yPos[self.minTimeThreeIndex]) , "\nActual Position: ", str(self.DxPos[self.minTimeThreeIndex]) , "," , str(self.DyPos[self.minTimeThreeIndex]) , ",", str(float(self.DphiPos[self.minTimeThreeIndex])*(math.pi/180)), "\n", file=self.log)
			print("Accuracy: ", str(self.Accuracy), "Length: ", str(self.Length), "\n" , file=self.log)

		if nJobs == 2:
			minTimeOne = min(self.times)
			self.minTimeOneIndex = self.times.index(minTimeOne)
			minTimeTwo = sorted(self.times)[-2]
			self.minTimeTwoIndex =self.times.index(minTimeTwo)
			
			minCoordinatesOne.append(self.xPos[self.minTimeOneIndex])
			minCoordinatesOne.append(self.yPos[self.minTimeOneIndex])
			minCoordinatesOne.append(self.phiPos[self.minTimeOneIndex])

			minCoordinatesTwo.append(self.xPos[self.minTimeTwoIndex])
			minCoordinatesTwo.append(self.yPos[self.minTimeTwoIndex])
			minCoordinatesTwo.append(self.phiPos[self.minTimeTwoIndex])

			#print(self.minTimeOneIndex, self.minTimeTwoIndex, self.minTimeThreeIndex)
			print("# 1: \n", self.minTimeOneIndex, "st Job",  file = self.log)
			print("Design Position: " ,str(self.xPos[self.minTimeOneIndex]) , ",", str(self.yPos[self.minTimeOneIndex]), "," , str(self.yPos[self.minTimeOneIndex]) , "\nActual Position: ", str(self.DxPos[self.minTimeOneIndex]) , "," , str(self.DyPos[self.minTimeOneIndex]) , ",", str(float(self.DphiPos[self.minTimeOneIndex])*(math.pi/180)), "\n", file=self.log)
			print("Accuracy: ", str(self.Accuracy), "Length: ", str(self.Length), file=self.log)

			print("# 2: \n", self.minTimeTwoIndex, "st Job",  file = self.log)
			print("Design Position: " ,str(self.xPos[self.minTimeTwoIndex]) , ",", str(self.yPos[self.minTimeTwoIndex]), "," , str(self.yPos[self.minTimeTwoIndex]) , "\nActual Position: ", str(self.DxPos[self.minTimeTwoIndex]) , "," , str(self.DyPos[self.minTimeTwoIndex]) , ",", str(float(self.DphiPos[self.minTimeTwoIndex])*(math.pi/180)), "\n", file=self.log)
			print("Accuracy: ", str(self.Accuracy), "Length: ", str(self.Length), file=self.log)

		if nJobs == 1:
			minTimeOne = min(self.times)
			self.minTimeOneIndex = self.times.index(minTimeOne)
			
			minCoordinatesOne.append(self.xPos[self.minTimeOneIndex])
			minCoordinatesOne.append(self.yPos[self.minTimeOneIndex])
			minCoordinatesOne.append(self.phiPos[self.minTimeOneIndex])

			print(self.minTimeOneIndex, self.minTimeTwoIndex, self.minTimeThreeIndex)
			print("# 1: \n", self.minTimeOneIndex, "st Job",  file = self.log)
			print("Design Position: " ,str(self.xPos[self.minTimeOneIndex]) , ",", str(self.yPos[self.minTimeOneIndex]), "," , str(self.yPos[self.minTimeOneIndex]) , "\nActual Position: ", str(self.DxPos[self.minTimeOneIndex]) , "," , str(self.DyPos[self.minTimeOneIndex]) , ",", str(float(self.DphiPos[self.minTimeOneIndex])*(math.pi/180)), "\n", file=self.log)
			print("Accuracy: ", str(self.Accuracy), "Length: ", str(self.Length), file=self.log)


	def showPlots(self):

		chamberOneInfo = [self.xPos[self.minTimeOneIndex], self.yPos[self.minTimeOneIndex], self.phiPos[self.minTimeOneIndex], self.DxPos[self.minTimeOneIndex], self.DyPos[self.minTimeOneIndex], self.DphiPos[self.minTimeOneIndex]]
		chamberTwoInfo = [self.xPos[self.minTimeTwoIndex], self.yPos[self.minTimeTwoIndex], self.phiPos[self.minTimeTwoIndex], self.DxPos[self.minTimeTwoIndex], self.DyPos[self.minTimeTwoIndex], self.DphiPos[self.minTimeTwoIndex]]
		chamberThreeInfo = [self.xPos[self.minTimeThreeIndex], self.yPos[self.minTimeThreeIndex], self.phiPos[self.minTimeThreeIndex], self.DxPos[self.minTimeThreeIndex], self.DyPos[self.minTimeThreeIndex], self.DphiPos[self.minTimeThreeIndex]]
		plot = GraphicMultpleScattering(self.figure1, self.sub1, self.sub2, self.sub3)
		plot.start(chamberOneInfo, chamberTwoInfo, chamberThreeInfo, self.Length, self.Accuracy)

	def showLog(self):
		self.log.close()
		os.startfile(self.filename)

	def returnJobNumber(self):
		return count


#print("2 --- time: ", minTimeOne, "x: ", minCoordinatesOne[0], "y: ", minCoordinatesOne[2], "phi: ", minCoordinatesOne[2], "\n", file = log)
#print("2 --- time: ", minTimeTwo, "x: ", minCoordinatesTwo[0], "y: ", minCoordinatesTwo[1], "phi: ", minCoordinatesTwo[2], "\n", file = log)
#rint("1 --- time: ", minTimeThree, "x: ", minCoordinatesThree[0], "y: ", minCoordinatesThree[1], "phi: ", minCoordinatesThree[2], "\n", file = log)