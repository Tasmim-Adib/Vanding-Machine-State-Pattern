import State19

class VendingMachine():

	state : State19.State

	def __init__(self):
		self.state = ""
	
	def setState(self, state):
		self.state = state
	
	def getState(self):
		return self.state