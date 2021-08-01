from pyasn1.type.univ import Integer
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
                self.Connector.DeleteRecord(user)
                self.Connector.PrepareURLGetAll(user)
            else:
                return

    
    def GetBestCareerStats(self):
        allPlayers = self.Connector.FindAllPlayers()
        currentPlayers = []
        i = 1
        for player in allPlayers.each():
            self.View.PrintPlayerName(i, player.val()['name'])
            i += 1
            currentPlayers.append(player)
        choice = int(self.View.SelectPlayer())

        choice -= 1
        j = 0
        for p in currentPlayers:
            if (j == choice):
                playerKey = p.key()
                break
            else:
                j += 1
        
        p = self.Connector.GetBestCareerStats(playerKey)
        self.View.PrintBestCareerStats(p.val())

        
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
        if choice == "2":
            self.GetBestCareerStats()
        if choice.lower() == "x":
            self.isRunning = False
        else:
            print("Please enter a valid option")
            return
