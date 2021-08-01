import pyrebase
import requests

config = {
    "apiKey" : "AIzaSyDg_XVDSQJ5q3_V3F5pWvqLNHlDKwZXDZY",
    "authDomain" : "cst8276project-af898.firebaseapp.com",
    "databaseURL" : "https://cst8276project-af898-default-rtdb.firebaseio.com/",
    "projectId" : "cst8276project-af898",
    "storageBucket" : "cst8276project-af898.appspot.com",
    "messagingSenderId" : "532154756835",
    "appId" : "1:532154756835:web:ab7d4eceb3554c14795fd6"
    }

firebase = pyrebase.initialize_app(config)

db = firebase.database()

# data = {'Name' : 'Monkeh'}
# db.child('Heroes').push(data)

heroes = db.child("Heroes").get()

for hero in heroes:
    print(hero.key())
    print(hero.val())

#URL = "https://best-overwatch-api.herokuapp.com/player/pc/us/Jeh0vah-1531"
URL = "https://ow-api.com/v1/stats/pc/us/Azulon-1178/complete"

r = requests.get(url = URL)

data = r.json()
db.child("Players").push(data)

# heroes = db.child("Heroes").shallow().get()
# print(heroes.val())
# print(type(heroes))
# for a in heroes:
#     h = db.child(a).get()
#     print(h.val())

# print("Database returned:")
# print(printList)
# print("Done")