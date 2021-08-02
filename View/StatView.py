import PySimpleGUI as psg

class StatViews():

    def __init__(self):
        #PySimpleGUI.Window(title="Stat Tracker", layout=[[]], margins=(500, 350)).read()
        layout = [
            [psg.Text("Menu")], 
            [psg.Button("Find player info")], 
            [psg.Button("Display best career stats")], 
            [psg.Button("Compare win rate")], 
            [psg.Button("Exit")]
            ]

        self.findPlayerLayout = [
            [psg.Text("Find a player")],
            [psg.T("Enter an account *XXXX-1111*"), psg.In(default_text='',size=(60,1), key='account', do_not_clear=True)],
            [psg.Button("Back")],
            [psg.Button("Find")]
        ]

        self.window = psg.Window("Stat Tracker", layout, finalize=True)
        #self.findPlayerWindow = psg.Window("Find Player", findPlayerLayout)


    def CreateWindow(self):
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == psg.WIN_CLOSED:
                break
        
        self.window.close()


    def Menu(self):
        return input("\n1) Find player info\n"
        + "2) Display best career stats\n"
        + "3) Compare win rate\n"
        + "x) Exit\n")


    def GetPlayerName(self):
        return input("\nInput account name *XXXX-1111*: ")

    
    def ConfirmUpdate(self):
        return input("\nPlayer found, update stats?(y/n): ")


    def PrintPlayerName(self, listNum, name):
        print(str(listNum) + ": " + name + "\n")

    
    def SelectPlayer(self):
        return input("\nSelect a user from the list: ")

    
    def PrintBestCareerStats(self, stats):
        statList = list(stats)

        print("\n")
        for item in statList:
            print(item + " " + str(stats[item]))


    def PrintWinRates(self, winRates):
        for key, value in winRates.items():
            print("\n" + key + " -- Win " + "%.2f" %value + "%")
