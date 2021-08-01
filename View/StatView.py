class StatViews():

    def Menu(self):
        return input("1) Find player info\n"
        + "2) Display best career stats\n"
        + "3) Display most played hero\n"
        + "4) Compare win rate")


    def GetPlayerName(self):
        return input("\nInput account name *XXXX-1111*: ")

    
    def ConfirmUpdate(self):
        return input("\nPlayer found, update stats?(y/n): ")
