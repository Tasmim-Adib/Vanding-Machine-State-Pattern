import State19
import VendingMachine19

class ShowMenu(State19.State):

    choice = 0
    coffeRemaining = 5
    cappuccinoRemaining = 5
    ex = False
    def performTask(self, vendingMachine):
        print("-----Choose your drinks-----")
        print("1. Coffee")
        print("2. Cappuccino")
        self.choice = int(input("Give your choice : ")) 
        print("------------------------------")
        if(self.choice == 1):
            if(self.coffeRemaining > 0):
                self.coffeRemaining = self.coffeRemaining - 1
            else:
                print("----No more Coffee is available-----")
                print("------------------------------")
                self.ex = True
        else:
            if(self.cappuccinoRemaining > 0):
                self.cappuccinoRemaining = self.cappuccinoRemaining - 1
            else:
                print("----No more Cappuccino is available-----")
                print("------------------------------")
                self.ex = True

        vendingMachine.setState(self)
    
    def getRemainingCoffee(self):
        return self.coffeRemaining
    
    def getRemainingCappuccino(self):
        return self.cappuccinoRemaining
    
    def getChoice(self):
        return self.choice

    def isExit(self):
        return self.ex
    
