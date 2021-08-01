import FirebaseConnector
from View import StatView

class StatController():
    def __init__(self):
        self.Connector = FirebaseConnector.DBConnector()
        self.View = StatView.StatViews()
        

    def ProgramStart(self):
        self.Connector.ConnectToDatabase()
        self.isRunning = True
        while(self.isRunning):
            userOption = self.View.Menu()
            self.EvaluateUserOption(userOption)
    

    def GetPlayerStats(self):
        user = self.View.GetPlayerName()
        if (self.Connector.PrepareURLGetAll(user)):
            if (self.Confirm(self.View.ConfirmUpdate())):
                # Delete object with current username and store it again from a fresh api pull
                None
            else:
                return


    def GetMostPlayedHero(self):
        None

    
    def CompareWinRate(self):
        None


    def Confirm(self, option):
        if option.lower() == "y":
            return True
        if option.lower() == "n":
            return False


    def EvaluateUserOption(self, choice):
        if choice == "1":
            self.GetPlayerStats()
        else:
            print("Please enter a valid option")
            return
