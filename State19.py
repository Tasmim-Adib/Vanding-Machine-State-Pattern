from abc import ABC, abstractmethod
import VendingMachine19

class State(ABC):

	@abstractmethod
	def performTask(self, vendingMachine):
		pass

	@abstractmethod
	def isExit(self):
		pass

