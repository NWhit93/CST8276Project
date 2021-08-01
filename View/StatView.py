class StatViews():

    def Menu(self):
        return input("\n1) Find player info\n"
        + "2) Display best career stats\n"
        + "3) Display most played hero\n"
        + "4) Compare win rate\n"
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
