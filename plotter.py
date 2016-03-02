#!/usr/bin/env python3

import json, sys, logging, time, plotly, plotly.graph_objs as go
#import numpy as np, matplotlib.pyplot as plt

class plotter():
	def __init__(self, dumpToLoad):
		#with open(dumpToLoad, 'r') as df: self.dump = json.loads(df.read())
		self.dump = dumpToLoad
		self.layout = go.Layout(autosize=False, width=800, height=500)
		self.fig = plotly.tools.make_subplots(rows=2, cols=1, vertical_spacing=0.1, subplot_titles=('Memory Usage', 'Network Usage',))

	def plot(self, tupleList, traceName):
		ld("%r" %([tupleList[i][0] for i in range(len(tupleList))]))
		memTrace = go.Scatter( x=[tupleList[i][0] for i in range(len(tupleList))],\
							 y=[tupleList[i][1] for i in range(len(tupleList))],\
							 name='memory usage of '+traceName)
		self.fig.append_trace(memTrace, 1, 1)

	def plot_net(self, tupleList, traceName):
		upTrace = go.Scatter( x=[tupleList['up'][i][0] for i in range(len(tupleList['up']))], \
							y=[tupleList['up'][i][1] for i in range(len(tupleList['up']))],\
							name='upload rate of '+traceName )
		downTrace = go.Scatter( x=[tupleList['down'][i][0] for i in range(len(tupleList['down']))], \
							y=[tupleList['down'][i][1] for i in range(len(tupleList['down']))],\
							name='download rate of '+traceName )
		self.fig.append_trace(upTrace,2,1)
		self.fig.append_trace(downTrace,2,1)
		


if __name__ == '__main__':
	logging.basicConfig(format= '%(asctime)s %(levelname)s - %(name)s:\t%(message)s', level=logging.INFO)
	ld, li = logging.debug, logging.info
	#totalMem, totalNet = dict(), {'up':dict(), 'down':dict()}
	#memAggArr = [dump[key]['memory_info'][i][1] for i in dump[kefor key in dump]
	if sys.argv[1:]:
		with open(sys.argv[1], 'r') as df: dump = json.loads(df.read())
		memAggArr = []
		pl = plotter(dump)
		for aProc in dump:
			pl.plot(dump[aProc]['memory_info'], aProc)
			if len(dump[aProc]['net_load']['up']) + len(dump[aProc]['net_load']['down'])>0:
				pl.plot_net(dump[aProc]['net_load'], aProc)
		plotly.offline.plot(pl.fig, filename=sys.argv[1]+'_plots.html')