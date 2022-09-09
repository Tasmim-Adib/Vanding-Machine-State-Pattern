import VendingMachine19
import ShowMenu19
import CollectCoin19
import Welcome19
import CheckValidity19
import Dispense19

vendingMachine = VendingMachine19.VendingMachine()
showMenu = ShowMenu19.ShowMenu()
collectCoin = CollectCoin19.CollectCoin()

exit = False
remainCoffee = 5
remainCappuccino = 5
while(exit == False):
    
    welcome = Welcome19.Welcome(remainCoffee, remainCappuccino)
    welcome.performTask(vendingMachine)
    exit = welcome.isExit()
    if(exit == True):
        break

    collectCoin.performTask(vendingMachine)
    total = vendingMachine.getState().getAmount()
    exit = collectCoin.isExit()
    if(exit == True):
        break

    showMenu.performTask(vendingMachine)
    exit = showMenu.isExit()
    if(exit == True):
        break
    choice = vendingMachine.getState().getChoice()
    remainCoffee = vendingMachine.getState().getRemainingCoffee()
    remainCappuccino = vendingMachine.getState().getRemainingCappuccino()

    checkValidity = CheckValidity19.CheckValidity(total, choice)
    checkValidity.performTask(vendingMachine)
    remaining = vendingMachine.getState().getRemainingAmount()

    exit = checkValidity.isExit()
    if(exit == True):
        break

    dispense = Dispense19.Dispense(remaining)
    dispense.performTask(vendingMachine)


