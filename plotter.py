#!/usr/bin/env python3

import json, sys, logging, time, plotly, plotly.graph_objs as go
#import numpy as np, matplotlib.pyplot as plt

class plotter():
	def __init__(self, dumpToLoad):
		with open(dumpToLoad, 'r') as df: self.dump = json.loads(df.read())
		self.fig = None

	def plot(self, tupleList):
		#plt.plot([self.dump[procName][attrName][0] for i in self.dump[procName][attrName]],  [self.dump[procName][attrName][1] for i in self.dump[procName][attrName]])
		#plt.show()
		ld("%r" %([tupleList[i][0] for i in range(len(tupleList))]))
		plotly.offline.plot({\
			"data": [go.Scatter(x=[tupleList[i][0] for i in range(len(tupleList))],\
							y=[tupleList[i][1] for i in range(len(tupleList))]),\
					]
			})

	def plot_net(self, tupleList, fileName):
		upTrace = go.Scatter( x=[tupleList['up'][i][0] for i in range(len(tupleList['up']))], \
							y=[tupleList['up'][i][1] for i in range(len(tupleList['up']))],\
							name='up-stream' )
		downTrace = go.Scatter( x=[tupleList['down'][i][0] for i in range(len(tupleList['down']))], \
							y=[tupleList['down'][i][1] for i in range(len(tupleList['down']))],\
							name='down-stream' )
		self.fig = plotly.tools.make_subplots(rows=1, cols=1, specs=[[{}]], shared_xaxes=True, shared_yaxes=True, vertical_spacing=0.001)
		self.fig.append_trace(upTrace,1,1)
		self.fig.append_trace(downTrace,1,1)
		plotly.offline.plot(self.fig, filename=fileName)


if __name__ == '__main__':
	logging.basicConfig(format= '%(asctime)s %(levelname)s - %(name)s:\t%(message)s', level=logging.DEBUG)
	ld, li = logging.debug, logging.info
	if sys.argv[1:]:
		pl = plotter(sys.argv[1])
		pl.plot(pl.dump['osafdtmd']['memory_info'])
		pl.plot_net(pl.dump['osafdtmd']['net_load'], 'dtmd_net.html')		
		#time.sleep(5)
		