from firebase import Firebase

config = {
    "apiKey": "AIzaSyCSMzDr9ohvgy4tTk6-5b8eC4A7CG4FgYM",
    "authDomain": "ospython-c68c0.firebaseapp.com",
    "databaseURL": "https://ospython-c68c0-default-rtdb.firebaseio.com",
    "projectId": "ospython-c68c0",
    "storageBucket": "ospython-c68c0.appspot.com",
    "messagingSenderId": "169713426191",
    "appId": "1:169713426191:web:2987a97f43ee1db2ab287a"
}


class FireService:
    def __init__(self):
        self.firebase = Firebase(config)
        self.db = self.firebase.database()

    def get_all_people(self):
        var = self.db.child("OSP").child("People").get()
        return var.val()

    def get_all_reports(self):
        var = self.db.child("OSP").child("Reports").get()
        return var.val()