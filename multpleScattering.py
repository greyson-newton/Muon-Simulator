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
	def __init__(self, X, Y, Phi, Dx, Dy, Dphi, Length, Accuracy):

		self.X, self.Y, self.Phi =  X, Y, Phi
		self.Dx, self.Dy, self.dPhi = Dx, Dy, Dphi

		self.Length, self.Accuracy = Length, Accuracy

		self.chamber1 = chamber(1, self.Length, self.X, self.Y, self.Phi, self.X+self.Dx, self.Y+self.Dy, self.Phi+self.dPhi, self.Accuracy)

		learningRates = [50,10,1.5]
		stepSizes = [.01,.01,.01]
		startTime = time.time()
		for i in range(400):
			if self.chamber1.isDone():
				endTime = time.time()
				break
			shootMuons(self.chamber1)
			self.chamber1.align()
			self.chamber1.resetData()
		self.time = endTime-startTime

	def returnTime(self):
		return self.time

def shootMuons(chamber1):
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
		if verbose > 5: print("")
		muonTrack, muonPath = propagateMuon(angleInitial, speedInitial, charge, xInitial, yInitial)

		chamber1.getResiduals(muonTrack, muonPath)

