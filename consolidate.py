#!/usr/bin/env python3
import sys, json

class consolidate():
	def __init__(self, dump):
		self.dump = dump
		self.result = dict( (k,type(v)()) for k,v in self.dump.items())

	def consolidate(self, aProc):
		self.result[aProc]['memory_MB'] = sum([aTup[1] for aTup in self.dump[aProc]['memory_info']])/len(self.dump[aProc]['memory_info'])
		self.result[aProc]['cpu_percent'] = sum([aTup[1] for aTup in self.dump[aProc]['cpu_info']])/len(self.dump[aProc]['cpu_info'])
		self.result[aProc]['net_load'] = {'up':None, 'down':None}
		if len(self.dump[aProc]['net_load']['up'])>0:
			self.result[aProc]['net_load']['up'] = sum( [aTup[1] for aTup in self.dump[aProc]['net_load']['up']] )/len(self.dump[aProc]['net_load']['up'])
			self.result[aProc]['net_load']['down'] = sum( [aTup[1] for aTup in self.dump[aProc]['net_load']['down']] )/len(self.dump[aProc]['net_load']['down'])

	def summary(self):
		for aProc in self.dump:	self.consolidate(aProc)
		return self.result

	def summary_all(self):
		res_all = {'memory_info':0, 'cpu_info':0, 'net_load':{'up':0, 'down':0}}
		self.summary()
		for aProc in self.result:
			res_all['memory_info'] += self.result[aProc]['memory_MB'] if self.result[aProc]['memory_MB'] is not None else 0
			res_all['cpu_info'] += self.result[aProc]['cpu_percent'] if self.result[aProc]['cpu_percent'] is not None else 0
			res_all['net_load']['up'] += self.result[aProc]['net_load']['up'] if self.result[aProc]['net_load']['up'] is not None else 0
			res_all['net_load']['down'] += self.result[aProc]['net_load']['down'] if self.result[aProc]['net_load']['down'] is not None else 0
		procLen = len(self.result.keys())
		res_all['memory_info'] = res_all['memory_info']/procLen
		res_all['cpu_info'] = res_all['cpu_info']/procLen
		res_all['net_load']['up'] = res_all['net_load']['up']/procLen
		res_all['net_load']['down'] = res_all['net_load']['down']/procLen
		return res_all


if __name__ == '__main__':
	if sys.argv[1:]:
		with open(sys.argv[1],'r') as f: dump = json.loads(f.read())
		c = consolidate(dump)
		#print(c.summary())
		if sys.argv[2:]:
			if sys.argv[2]=='-a':
				with open(sys.argv[1] + '_consolidated_all.json', 'w') as fw:
					jd = json.dumps(c.summary_all(), indent=4)
					fw.write(jd)
					print(jd) 
		with open(sys.argv[1] + '_consolidated.json', 'w') as fw: 
			jd = json.dumps(c.summary(), indent=4)
			fw.write(jd)
			print(jd)

		
