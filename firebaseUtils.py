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


class PersonService:
    def __init__(self):
        self.firebase = Firebase(config)
        self.db = self.firebase.database()

    def get_all_people(self):
        var = self.db.child("OSP").child("People").get()
        return var.val()

    def add_person(self, first_name, last_name, is_action_leader, is_active, is_driver, is_section_leader, phone_number):
        FirstName = "John"
        LastName = "Smith"
        IsActionLeader = 1
        IsActive = 1
        IsDriver = 1
        IsSectionLeader = 1
        PhoneNumber = 123412345

        person_data = {
            "FirstName": FirstName,
            "LastName": LastName,
            "IsActionLeader": IsActionLeader,
            "IsActive": IsActive,
            "IsDriver": IsDriver,
            "IsSectionLeader": IsSectionLeader,
            "PhoneNumber": PhoneNumber
        }

        self.db.child("OSP").child("People").push(person_data)

    def remove_person_from_active(self, id):
        self.db.child("OSP").child("People").child(id).update({"IsActive": 0})
        pass

    def change_person_data(self):
        pass


class ReportService:
    def __init__(self):
        self.firebase = Firebase(config)
        self.db = self.firebase.database()

    def get_all_reports(self):
        var = self.db.child("OSP").child("Reports").get()
        return var.val()

    def get_report_data(self):
        pass
