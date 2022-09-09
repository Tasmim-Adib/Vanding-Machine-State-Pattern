import State19
import VendingMachine19

class Dispense(State19.State):

    remainingAmount = 0

    exit = False
    def __init__(self, amount):
        self.remainingAmount = amount

    def performTask(self, vendingMachine):
        print("------------------------------")
        print("----Please Have your Drinks-----")
        print("----Please Have the Changed " + str(self.remainingAmount) + "cent-----")
        print("----Thank you for being with us-----")
        print("----Have A Nice Day-----")
        print("------------------------------")
    
    def isExit(self):
        return self.exit