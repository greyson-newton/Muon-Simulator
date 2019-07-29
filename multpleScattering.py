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
from chamber import chamber
import numpy as np
random.seed(1.0)

class multpleScattering:
	def __init__(self, figure, sub1, sub2, sub3):
		self.Length = 10
		self.X, self.Y, self.Phi = 0,0,0
		self.dX, self.dY, self.dPhi = 0,0,0
		self.figure = figure
		self.sub1, self.sub2, self.sub3 = sub1, sub2, sub3

	def start(self, X, Y, Phi, Dx, Dy, Dphi, Length, Accuracy):

		self.time = 0

		residualLeavingBounds = []

		self.X, self.Y, self.Phi =  X, Y, Phi
		self.Dx, self.Dy, self.dPhi = Dx, Dy, Dphi

		self.Length, self.Accuracy = Length, Accuracy

		self.chamber1 = chamber(1, self.Length, self.X, self.Y, self.Phi, self.X+self.Dx, self.Y+self.Dy, self.Phi+self.dPhi, self.Accuracy)
		self.chamber1.plotChamber(self.sub1,self.sub2,self.sub3)

		learningRates = [50,10,1.5]
		stepSizes = [.01,.01,.01]
		startTime = time.time()
		for i in range(400):
			if self.chamber1.isDone():
				endTime = time.time()
				break
			shootMuons(self.chamber1, self.sub1)
			self.chamber1.align()
			self.chamber1.resetData()
			self.chamber1.cleanChamberPlot()
			self.chamber1.plotChamber(self.sub1,self.sub2,self.sub3)
		self.time = endTime-startTime
	def reset(self):
		self.chamber1.cleanChamberPlot()

	def returnTime(self):
		return self.time

def shootMuons(chamber1, sub1):
	for i in range(nEvents):

		if i%1000==0: print(i*1.0/nEvents)

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
		muonTrack, muonPath = propagateMuon(angleInitial, speedInitial, charge, xInitial, yInitial)

		chamber1.getResiduals(muonTrack, muonPath)

		# note the y and x axis are not to scale, meaning things are stretched. A tilted chamber will look shorter
		if i%10000==0:
			#plt.clf()
			trackPaths = sub1.plot(muonTrack[0],muonTrack[1], color='orange', label="track")
			muonPaths = sub1.plot(muonPath[0],muonPath[1], marker = 'o', color='red', label="actual path")
			legend = sub1.legend()
			plt.pause(0.01)
			for muonPath in muonPaths:
				muonPath.remove()
			for trackPath in trackPaths:
				trackPath.remove()
			   #plt.show()
				#plt.draw()
				#plt.clf()


