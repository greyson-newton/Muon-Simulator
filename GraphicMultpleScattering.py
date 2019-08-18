#https://www.cs.uct.ac.za/mit_notes/python/Introduction_to_GUI_Programming.html
from numba import jit
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import math, random, time
from geometry import *
from constants import *
from iterateMuon import iterateMuon
from circleIntersectLine import circleIntersectLine
from propagateMuon import propagateMuon
from GraphicChamber import *
import numpy as np
random.seed(1.0)

class GraphicMultpleScattering:
	def __init__(self, figure, sub1, sub2, sub3):

		self.figure = figure
		self.sub1, self.sub2, self.sub3 = sub1, sub2, sub3


	def start(self, chamberInfoOne, chamberInfoTwo, chamberInfoThree, Length, Accuracy):

		residualLeavingBounds = []
		self.OneX, self.OneY, self.OnePhi, self.OneDX, self.OneDY, self.OneDPhi = float(chamberInfoOne[0]), float(chamberInfoOne[1]), float(chamberInfoOne[2]), float(chamberInfoOne[3]), float(chamberInfoOne[4]), float(chamberInfoOne[5])
		self.TwoX, self.TwoY, self.TwoPhi, self.TwoDX, self.TwoDY, self.TwoDPhi = float(chamberInfoTwo[0]), float(chamberInfoTwo[1]), float(chamberInfoTwo[2]), float(chamberInfoTwo[3]), float(chamberInfoTwo[4]), float(chamberInfoTwo[5])
		self.ThreeX, self.ThreeY, self.ThreePhi, self.ThreeDX, self.ThreeDY, self.ThreeDPhi = float(chamberInfoThree[0]), float(chamberInfoThree[1]), float(chamberInfoThree[2]), float(chamberInfoThree[3]), float(chamberInfoThree[4]), float(chamberInfoThree[5])
		
		self.chamber1 = chamber(1, Length, self.OneX, self.OneY, self.OnePhi, self.OneX+self.OneDX, self.OneY+self.OneDY, self.OnePhi+self.OneDPhi, Accuracy)
		self.chamber2 = chamber(1, Length, self.TwoX, self.TwoY, self.TwoPhi, self.TwoX+self.TwoDX, self.TwoY+self.TwoDY, self.TwoPhi+self.TwoDPhi, Accuracy)
		self.chamber3 = chamber(1, Length, self.ThreeX, self.ThreeY, self.ThreePhi, self.ThreeX+self.ThreeDX, self.ThreeY+self.ThreeDY, self.ThreePhi+self.ThreeDPhi, Accuracy)
		#self.chamber1.plotChamber(self.sub1,self.sub2,self.sub3)
		learningRates = [50,10,1.5]
		stepSizes = [.01,.01,.01]
		for i in range(400):
			self.actualEndpointsOne = self.chamber1.actualEndpoints
			self.designEndpointsOne = self.chamber1.designEndpoints
			self.designPlotOne = self.sub1.plot(self.designEndpointsOne[0],self.designEndpointsOne[1], color='blue', label="design Chamber Postition")
			self.actualPlotOne = self.sub1.plot(self.actualEndpointsOne[0],self.actualEndpointsOne[1], color='green', label="actual Chamber Postition")
			    
			self.actualEndpointsTwo = self.chamber2.actualEndpoints
			self.designEndpointsTwo = self.chamber2.designEndpoints
			self.designPlotTwo = self.sub2.plot(self.designEndpointsTwo[0],self.designEndpointsTwo[1], color='blue', label="design Chamber Postition")
			self.actualPlotTwo = self.sub2.plot(self.actualEndpointsTwo[0],self.actualEndpointsTwo[1], color='green', label="actual Chamber Postition")
				
			self.actualEndpointsThree = self.chamber3.actualEndpoints
			self.designEndpointsThree = self.chamber3.designEndpoints
			self.designPlotThree = self.sub3.plot(self.designEndpointsThree[0],self.designEndpointsThree[1], color='blue', label="design Chamber Postition")
			self.actualPlotThree = self.sub3.plot(self.actualEndpointsThree[0],self.actualEndpointsThree[1], color='green', label="actual Chamber Postition")
			shootMuons(self.chamber1, self.chamber2, self.chamber3, self.sub1, self.sub2, self.sub3)
			self.chamber1.align()
			self.chamber1.resetData()

			for plot in self.designPlotOne:
			    plot.remove()
			for plot in self.actualPlotOne:
			    plot.remove()

			self.chamber2.align()
			self.chamber2.resetData()

			for plot in self.designPlotTwo:
			    plot.remove()
			for plot in self.actualPlotTwo:
			    plot.remove()

			self.chamber3.align()
			self.chamber3.resetData()

			for plot in self.designPlotThree:
			    plot.remove()
			for plot in self.actualPlotThree:
			    plot.remove()



	def reset(self):
		self.chamber1.cleanChamberPlot()

	def returnTime(self):
		return self.time

def shootMuons(chamber1, chamber2, chamber3, sub1, sub2, sub3):
	for i in range(nEvents):

		if i%1000==0: i*1.0/nEvents

		#set up inital state of muon
		angleInitial = 1
		speedInitial = 1000

		angleInitial = random.random()-.5

		charge = random.random()
		if charge > .5: charge = 1
		else: charge = -1


		xInitial = 0
		yInitial = 0

		#create muon track
		if verbose > 5: print("start  angle {} speed {} charge {} x {} y {}".format( angleInitial, speedInitial, charge, xInitial, yInitial))
		muonTrackOne, muonPathOne = propagateMuon(angleInitial, speedInitial, charge, xInitial, yInitial)
		muonTrackTwo, muonPathTwo = propagateMuon(angleInitial, speedInitial, charge, xInitial, yInitial)
		muonTrackThree, muonPathThree = propagateMuon(angleInitial, speedInitial, charge, xInitial, yInitial)
		
		chamber1.getResiduals(muonTrackOne, muonPathOne)
		chamber2.getResiduals(muonTrackTwo, muonPathTwo)
		chamber3.getResiduals(muonTrackThree, muonPathThree)

		# note the y and x axis are not to scale, meaning things are stretched. A tilted chamber will look shorter
		if i%10000==0:
			#plt.clf()
			trackPathsOne = sub1.plot(muonTrackOne[0],muonTrackOne[1], color='orange', label="track")
			muonPathsOne = sub1.plot(muonPathOne[0],muonPathOne[1], marker = 'o', color='red', label="actual path")

			trackPathsTwo = sub2.plot(muonTrackTwo[0],muonTrackTwo[1], color='orange', label="track")
			muonPathsTwo = sub2.plot(muonPathTwo[0],muonPathTwo[1], marker = 'o', color='red', label="actual path")

			trackPathsThree = sub3.plot(muonTrackThree[0],muonTrackThree[1], color='orange', label="track")
			muonPathsThree = sub3.plot(muonPathThree[0],muonPathThree[1], marker = 'o', color='red', label="actual path")
			legend = sub1.legend()
			plt.pause(0.01)
			for muonPath in muonPathsOne:
				muonPath.remove()
			for trackPath in trackPathsOne:
				trackPath.remove()
			for muonPath in muonPathsTwo:
				muonPath.remove()
			for trackPath in trackPathsTwo:
				trackPath.remove()
			for muonPath in muonPathsThree:
				muonPath.remove()
			for trackPath in trackPathsThree:
				trackPath.remove()

