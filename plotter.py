#!/usr/bin/env python3
import matplotlib.pyplot as plt , json, sys, logging, time


class plotter():
	def __init__(self, dumpToLoad):
		with open(dumpToLoad, 'r') as df: self.dump = json.loads(df.read())

	def plot(self, procName, attrName):
		plt.plot([self.dump[procName][attrName][0] for i in self.dump[procName][attrName]],  [self.dump[procName][attrName][1] for i in self.dump[procName][attrName]])
		plt.show()


if __name__ == '__main__':
	logging.basicConfig(format= '%(asctime)s %(levelname)s - %(name)s:\t%(message)s', level=logging.INFO)
	ld, li = logging.debug, logging.info
	if sys.argv[1:]:
		pl = plotter(sys.argv[1])
		ld("%r" %(pl.dump))
		#pl.plot('osafckptnd','memory_info')
		
		plt.plot(list(range(1,10)), list(range(1,10)))
		plt.axis([0,10,0,20])
		plt.show()
		#time.sleep(5)
		