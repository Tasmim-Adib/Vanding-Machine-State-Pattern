import State19
import VendingMachine19

class CheckValidity(State19.State):

    
    givenAmount = 0
    givenChoice = 0
    remainingAmount = 0
    exit = False

    def __init__(self, amount, choice):
        self.givenAmount = amount
        self.givenChoice = choice

    def performTask(self, vendingMachine):
        if(self.givenChoice == 1):
            if(self.givenAmount >= 120):
                self.remainingAmount = self.givenAmount - 120
            else:
                print("---You have given less amount to buy Coffee!!!---")
                print("------------------------------")

                self.exit = True
        else:
            if(self.givenAmount >= 150):
                self.remainingAmount = self.givenAmount - 150
            else:
                print("---You have given less amount to buy Cappuccino!!!---")
                print("------------------------------")
                self.exit = True

        vendingMachine.setState(self)
    
    def getRemainingAmount(self):
        return self.remainingAmount
    
    def isExit(self):
        return self.exit