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

    def add_person(self,
                   first_name,
                   last_name,
                   is_action_leader,
                   is_active,
                   is_driver,
                   is_section_leader,
                   phone_number):

        person_data = {
            "FirstName": first_name,
            "LastName": last_name,
            "IsActionLeader": is_action_leader,
            "IsActive": is_active,
            "IsDriver": is_driver,
            "IsSectionLeader": is_section_leader,
            "PhoneNumber": phone_number
        }

        self.db.child("OSP").child("People").push(person_data)

    def check_person_existence(self, first_name, last_name, phone_number):
        all_people = self.db.child("OSP").child("People").get().val()
        is_there = 0

        for _, i in all_people.items():
            if i is not None:
                if i.get('FirstName') == first_name and i.get('LastName') == last_name and i.get('PhoneNumber') == phone_number:
                    is_there = 1
                    break
        return is_there

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
