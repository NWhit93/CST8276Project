from pyasn1.type.univ import Integer
import FirebaseConnector
import PySimpleGUI as psg
from View import StatView

class StatController():
    def __init__(self):
        self.Connector = FirebaseConnector.DBConnector()
        self.View = StatView.StatViews()
        

    def ProgramStart(self):
        self.Connector.ConnectToDatabase()
        self.isRunning = True

        self.StartWindow()
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

    
    def CompareWinRate(self):
        allPlayers = self.Connector.FindAllPlayers()
        currentPlayers = {}

        for player in allPlayers.each():
            playerKey = player.key()
            games = self.Connector.GetWins(playerKey)
            gameWins = games.val()['won']
            gameTotal = games.val()['played']

            winRate = (int(gameWins)/int(gameTotal)) * 100

            currentPlayers[player.val()['name']] = winRate

        self.View.PrintWinRates(currentPlayers)   


    def Confirm(self, option):
        if option.lower() == "y":
            return True
        if option.lower() == "n":
            return False


    # GUI Menu
    def StartWindow(self):
        menuWindow = self.View.window
        findPlayerWindow = None

        while True:
            #event, values = self.View.window.read()
            window, event, values = psg.read_all_windows()
            if event == "Exit" or event == psg.WIN_CLOSED:
                break
            elif event == "Find player info" and not findPlayerWindow:
                menuWindow.hide()
                findPlayerWindow = self.MakeFindPlayerWindow().read()
                # Switch to new window with textbox input
            elif event == "Find":
                userName = values['account']
                print(userName)

        
        self.View.window.close()


    def MakeFindPlayerWindow(self):
        return psg.Window("Find Player", self.View.findPlayerLayout)


    # Console Menu
    def EvaluateUserOption(self, choice):
        if choice == "1":
            self.GetPlayerStats()
        elif choice == "2":
            self.GetBestCareerStats()
        elif choice == "3":
            self.CompareWinRate()
        elif choice.lower() == "x":
            self.isRunning = False
        else:
            print("Please enter a valid option")
            return
