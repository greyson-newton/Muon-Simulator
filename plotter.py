import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from math import exp
from scipy.stats import norm

class plotter:
	def __init__(self, xInit, xFinal, momentum, nIterations):
		self.nIterations = nIterations
		self.momentum = momentum
		plt.style.use('seaborn')
		self.x = range(xInit, xFinal)
		self.Y = [self.momentum*exp(-0.5*_) for _ in self.x]
		self.size = len(self.x)
		self.error = norm.rvs(0, scale=0.0001, size=self.size)
		self.simulated_data = [max(0, y+e) for (y,e) in zip(self.Y[:self.size],self.error)]		

		#print(self.simulated_data)

		self.fig = plt.figure(figsize = (14,10))

		self.sub1 = self.fig.add_subplot(2,1,2)
		self.sub1.set_title('Visual of Alignment')
		self.sub1.margins(0.05)           # Default margin is 0.05, value 0 means fit
		self.sub1.set_xlim([0, 75])
		self.sub1.set_ylim([-150, 150])

		self.sub2 = self.fig.add_subplot(2,2,1)
		self.sub2.set_title('Alignment Step')

		self.sub3 = self.fig.add_subplot(2,2,2)
		self.sub3.set_title('Residual')
		self.fig.suptitle('Fastest Job')
		sub1legend = self.sub1.legend(loc='lower left', bbox_to_anchor=(0.5, -0.05), shadow=True)
		sub2legend = self.sub2.legend(loc='lower left', bbox_to_anchor=(0.5, -0.05), shadow=True)
	def returnStepSize(self, index):
		return self.Y[index]
	def returnStepSizes(self):
		return self.Y
	def show(self):
		plt.show()
	def updateEndpoints(self, actualEndpoints, designEndpoints):
		self.sub1.margins(0.05)           # Default margin is 0.05, value 0 means fit
		self.sub1.set_xlim([0, 75])
		self.sub1.set_ylim([-150, 150])
		self.sub1.set_ylabel('local y')
		self.sub1.set_xlabel('local x')
		self.actualEndpoints = actualEndpoints
		self.designEndpoints = designEndpoints
		self.designPlot = self.sub1.plot(self.designEndpoints[0],self.designEndpoints[1], color='blue', label="design Chamber Postition")
		self.actualPlot = self.sub1.plot(self.actualEndpoints[0],self.actualEndpoints[1], color='green', label="actual Chamber Postition")
		
	def updateMuonPath(self, muonTrackOne, muonPathOne):
		self.muonTrack = muonTrackOne
		self.muonPath = muonPathOne
		self.trackPlot = self.sub1.plot(self.muonTrack[0], self.muonTrack[1], color='orange', label="track")
		self.muonPlot = self.sub1.plot(self.muonPath[0],self.muonPath[1], marker = 'o', color='red', label="actual path")

		plt.pause(0.0001)
	def updateLinePlots(self, xCount, yCount, zCount):
		self.sub2.set_ylim([0,(self.momentum)])
		self.sub2.set_xlim([0,15])
		self.sub2.set_xlabel('alignment step #')
		self.sub2.set_ylabel('alignment step magnitude')
		self.xPt, self.yPt, self.zPt = [xCount, xCount], [yCount, yCount], [zCount, zCount]
		self.xLine  = [0, 0.25]
		self.yLine=[0, 0.25]
		self.zLine = [0, 0.25]
						#axs = plt.subplots(nrows=3, ncols=2, sharex=True, sharey=True, figsize = (10,6), gridspec_kw={'hspace': 0})
		self.sub2.plot(self.x, self.Y, color = 'black')
		self.datapointPlot = self.sub2.plot(self.x[:self.size], self.simulated_data, 'r.')
		self.xPlot = self.sub2.plot(self.xPt, self.xLine, color='blue', lw=2, label = 'x iteration')
		self.yPlot = self.sub2.plot(self.yPt, self.yLine, color='red', lw=2, label = 'y iteration')
		self.zPlot = self.sub2.plot(self.zPt, self.zLine, color='green', lw=2, label = 'phi iteration')


	def updateResidualPlot(self, yResidual):
		#viridisBig = cm.get_cmap('viridis', 512)
		#newcmp = ListedColormap(viridisBig(np.linspace(0.25, 0.75, 256)))
       # psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
        #fig.colorbar(psm, ax=ax)
		self.residualPlot = self.sub3.hist(yResidual)

	def resetMuonPaths(self):
		self.sub1.legend()
		for x in self.muonPlot:
			x.remove()
		for x in self.trackPlot:
			x.remove()
	def resetEndpoints(self):
		self.sub1.legend()
		for x in self.designPlot:
			x.remove()
		for x in self.actualPlot:
			x.remove()
	def resetLinePlot(self):
		self.sub2.legend()
		for x in self.xPlot:
			x.remove()
		for x in self.yPlot:
			x.remove()
		for x in self.zPlot:
			x.remove()


		#self.sub2.clear()
		#self.sub2.legend()