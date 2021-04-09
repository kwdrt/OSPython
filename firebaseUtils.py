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
        person_id = None

        for key, i in all_people.items():
            if i is not None:
                if i.get('FirstName') == first_name and i.get('LastName') == last_name and i.get('PhoneNumber') == phone_number:
                    person_id = key
                    break
        return person_id

    def remove_person_from_active(self, id):
        self.db.child("OSP").child("People").child(id).update({"IsActive": 0})

    def change_person_data(self, id, first_name, last_name, phone_number, is_active, is_driver, is_action_leader, is_section_leader):
        if id is not None:
            self.db.child("OSP").child("People").child(id).update({
                "FirstName": first_name,
                "LastName": last_name,
                "IsActionLeader": is_action_leader,
                "IsActive": is_active,
                "IsDriver": is_driver,
                "IsSectionLeader": is_section_leader,
                "PhoneNumber": phone_number
            })


class ReportService:
    def __init__(self):
        self.firebase = Firebase(config)
        self.db = self.firebase.database()

    def get_all_reports(self):
        var = self.db.child("OSP").child("Reports").get()
        return var.val()

    def get_report_data(self, report_id):
        report = self.db.child("OSP").child("Reports").child(report_id).get()
        return report.val()

    def add_report(self, km_to_place, accident_type, at_place_date, at_place_hour, counter_state, depot_hour,
                   injured, out_date, out_hour, perpetrator, place_name, return_date, return_hour, section_current,
                   section_leader_id, editable, action_leader_id, driver_id):
        report_data = {
            "KM_to_place": km_to_place,
            "accident_type": accident_type,
            "action_leader_id": action_leader_id,
            "at_place_date": at_place_date,
            "at_place_hour": at_place_hour,
            "counter_state": counter_state,
            "depot_hour": depot_hour,
            "driver_id": driver_id,
            "editable": editable,
            "injured": injured,
            "out_date": out_date,
            "out_hour": out_hour,
            "perpetrator": perpetrator,
            "place_name": place_name,
            "return_date": return_date,
            "return_hour": return_hour,
            "section_current": section_current,
            "section_leader_id": section_leader_id
        }
        self.db.child("OSP").child("Reports").push(report_data)

    def change_report_data(self, report_id, km_to_place, accident_type, at_place_date, at_place_hour, counter_state,
                           depot_hour, injured, out_date, out_hour, perpetrator, place_name, return_date, return_hour,
                           section_current, section_leader_id, editable, action_leader_id, driver_id):
        if report_id is not None:
            self.db.child("OSP").child("Reports").child(report_id).update({
                "KM_to_place": km_to_place,
                "accident_type": accident_type,
                "action_leader_id": action_leader_id,
                "at_place_date": at_place_date,
                "at_place_hour": at_place_hour,
                "counter_state": counter_state,
                "depot_hour": depot_hour,
                "driver_id": driver_id,
                "editable": editable,
                "injured": injured,
                "out_date": out_date,
                "out_hour": out_hour,
                "perpetrator": perpetrator,
                "place_name": place_name,
                "return_date": return_date,
                "return_hour": return_hour,
                "section_current": section_current,
                "section_leader_id": section_leader_id
            })
