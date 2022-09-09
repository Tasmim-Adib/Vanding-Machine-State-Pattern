import State19
import VendingMachine19

class Welcome(State19.State):

    choice = 0
    remainCoffee = 0
    remainCappuccino = 0
    def __init__(self, coffee, cappuccino):
        self.remainCoffee = coffee
        self.remainCappuccino = cappuccino

    def performTask(self, vendingMachine):
        print("Welcome !!! Please Give me some cents and enjoy your drinks")
        print("You will get only coffe and cappuccino from me")
        print("Coffee Remaining : " + str(self.remainCoffee))
        print("Cappuccino Remaining : " + str(self.remainCappuccino))
        print("------------------------------")
        vendingMachine.setState(self)
        print("1. Proceed")
        print("2. Cancel")
        self.choice = int(input("Enter your choice : "))
        print("------------------------------")

    def isExit(self):
        if(self.choice == 1):
            return False
        else:
            return True
