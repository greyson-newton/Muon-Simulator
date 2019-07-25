#https://www.cs.uct.ac.za/mit_notes/python/Introduction_to_GUI_Programming.html
from numba import jit
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import math
import random
from geometry import *
from constants import *
from iterateMuon import iterateMuon
from circleIntersectLine import circleIntersectLine
from propagateMuon import propagateMuon
from chamber import chamber
import numpy as np
from tkinter import *
random.seed(1.0)

class multpleScattering:
	def __init__(self):
		self.Length = 10
		self.X, self.Y, self.Phi = 0,0,0
		self.dX, self.dY, self.dPhi = 0,0,0

	def start(self, X, Y, Phi, Dx, Dy, Dphi):

		self.sub1 = plt.subplot(212)
		self.sub1.margins(0.05)           # Default margin is 0.05, value 0 means fit
		self.sub1.set_xlim([0, 100])
		self.sub1.set_ylim([-200, 200])

		self.sub2 = plt.subplot(221)
		self.sub2.set_title('Fitness')
		self.sub2.set_xlim([0, 40])

		self.sub3 = plt.subplot(222)
		self.sub3.set_title('y Residual')

		residualLeavingBounds = []

		self.X, self.Y, self.Phi =  X, Y, Phi
		self.Dx, self.Dy, self.dPhi = Dx, Dy, Dphi

		self.accuracy = 0.00001

		chamber1 = chamber(1, self.Length, self.X, self.Y, self.Phi, self.X+self.Dx, self.Y+self.Dy, self.Phi+self.dPhi, self.accuracy)
		chamber1.plotChamber(self.sub1,self.sub2,self.sub3)

		learningRates = [50,10,1.5]
		stepSizes = [.01,.01,.01]
		for i in range(400):
			if chamber1.isDone():
				#throw results
				break
			shootMuons(chamber1, self.sub1)
			chamber1.align()
			chamber1.resetData()
			chamber1.cleanChamberPlot()
			chamber1.plotChamber(self.sub1,self.sub2,self.sub3)



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


