import pyrebase
import requests


class DBConnector():

    def ConnectToDatabase(self):
        self.config = {
            "apiKey" : "AIzaSyDg_XVDSQJ5q3_V3F5pWvqLNHlDKwZXDZY",
            "authDomain" : "cst8276project-af898.firebaseapp.com",
            "databaseURL" : "https://cst8276project-af898-default-rtdb.firebaseio.com/",
            "projectId" : "cst8276project-af898",
            "storageBucket" : "cst8276project-af898.appspot.com",
            "messagingSenderId" : "532154756835",
            "appId" : "1:532154756835:web:ab7d4eceb3554c14795fd6"
            }

        self.firebase = pyrebase.initialize_app(self.config)

        self.db = self.firebase.database()

    
    def PrepareURLGetAll(self, userName):
        if (self.AccountStatExists(userName)):
            return True
        else:
            URL = "https://ow-api.com/v1/stats/pc/us/" + userName + "/complete"
            self.GetAll(URL)
            return False

    
    def GetAll(self, URL):
        r = requests.get(url = URL)
        data = r.json()
        self.db.child("Players").push(data)


    def FindAllPlayers(self):
        return self.db.child("Players").order_by_child("name").get()


    def AccountStatExists(self, userName):
        try:
            players = self.db.child("Players").get()
            userName = userName.replace("-", "#")
            for player in players.each():
                if player.val()['name'] == userName:
                    return True
            return False
        except:
            return False
    

    def DeleteRecord(self, userName):
        players = self.db.child("Players").get()
        userName = userName.replace("-", "#")
        for player in players.each():
                if player.val()['name'] == userName:
                    key = player.key()

        self.db.child("Players").child(key).remove()


    def GetBestCareerStats(self, playerKey):
        return self.db.child("Players").child(playerKey).child("quickPlayStats").child("careerStats").child("allHeroes").child("best").get()


    def GetWins(self, playerKey):
        return self.db.child("Players").child(playerKey).child("quickPlayStats").child("games").get()        
