import State19
import VendingMachine19

class CollectCoin(State19.State):

    totalAmount = 0
    choice = 0

    def performTask(self, vendingMachine):
        print("------------------------------")
        print("------------------------------")
        print("You are allowed to give only 10, 20 and 50 cents")
        tenCent = int(input("How many 10 cent coin do you want to give : "))
        twentyCent = int(input("How many 20 cent coin do you want to give : "))
        fiftyCent = int(input("How many 50 cent coin do you want to give : "))
        print("------------------------------")
        print("------------------------------")

        self.totalAmount = tenCent * 10 + twentyCent * 20 + fiftyCent * 50
        vendingMachine.setState(self)
        print("---------------------------------------------")
        print("Total amount you have given : " + str(self.totalAmount))
        print("1. Proceed")
        print("2. Cancel")
        self.choice = int(input("Enter your choice : "))
        print("------------------------------")
    
    def getAmount(self):
        return self.totalAmount

    def isExit(self):
        if(self.choice == 1):
            return False
        else:
            return True