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

    def get_drivers(self):
        peoples = self.get_all_people()
        drivers = []
        for key, i in peoples.items():
            if i is not None:
                if i.get("IsDriver") and i.get("IsActive"):
                    drivers.append({"FirstName": i.get("FirstName"), "LastName": i.get("LastName"), "PhoneNumber": i.get("PhoneNumber")})
        return drivers

    def get_action_leaders(self):
        peoples = self.get_all_people()
        action_leaders = []
        for key, i in peoples.items():
            if i is not None:
                if i.get("IsActionLeader") and i.get("IsActive"):
                    action_leaders.append({"FirstName": i.get("FirstName"), "LastName": i.get("LastName"), "PhoneNumber": i.get("PhoneNumber")})
        return action_leaders

    def get_section_leaders(self):
        peoples = self.get_all_people()
        section_leaders = []
        for key, i in peoples.items():
            if i is not None:
                if i.get("IsSectionLeader") and i.get("IsActive"):
                    section_leaders.append({"FirstName": i.get("FirstName"), "LastName": i.get("LastName"), "PhoneNumber": i.get("PhoneNumber")})
        return section_leaders

    def check_person_existence(self, first_name, last_name, phone_number):
        all_people = self.get_all_people()
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

    def get_person_by_id(self, id):
        return self.db.child("OSP").child("People").child(id).get().val()

    def id_to_text(self, id):
        person = self.get_person_by_id(id)
        person_data = person.get("FirstName") + " " + person.get("LastName")
        return person_data

    def id_to_box(self, id):
        person = self.get_person_by_id(id)
        person_data = person.get("FirstName") + "," + person.get("LastName") + "," + str(person.get("PhoneNumber"))
        return person_data

    def section_to_string(self, section_table):
        section_string = ""
        for id in section_table:
            section_string += self.id_to_text(id) + "\n"
        if section_string == "":
            print("Empty section")
        return section_string

    # gets id of chosen person from data in UI element, should return None if not found (should not happen in usage)
    def translate_to_id(self, text):
        person_details = text.split(",")
        p_len = len(person_details)
        p_num = person_details[p_len - 1]
        p_last = person_details[p_len - 2]
        p_first = ""
        for i in range(0, p_len - 2):
            p_first += person_details[i]
        return self.check_person_existence(p_first, p_last, int(p_num))

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

    # 0 means not closed
    def is_report_closed(self, report_id):
        return self.get_report_data(report_id)["editable"]

    def get_report_id_by_fields(self, report_string):
        report_details = report_string.split(",")
        all_reports = self.get_all_reports()
        report_id = None

        for key, i in all_reports.items():
            if i is not None:
                if i.get('at_place_date') == report_details[0] \
                        and i.get('at_place_hour') == report_details[1] \
                        and i.get('place_name') == report_details[2]:
                    report_id = key
                    break
        return report_id

    def add_report(self, km_to_place, accident_type, at_place_date, at_place_hour, counter_state, depot_hour,
                   injured, out_date, out_hour, perpetrator, place_name, return_date, return_hour, section_current,
                   section_leader_id, editable, action_leader_id, driver_id, details):
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
            "section_leader_id": section_leader_id,
            "details": details
        }
        self.db.child("OSP").child("Reports").push(report_data)

    def change_report_data(self, report_id, km_to_place, accident_type, at_place_date, at_place_hour, counter_state,
                           depot_hour, injured, out_date, out_hour, perpetrator, place_name, return_date, return_hour,
                           section_current, section_leader_id, editable, action_leader_id, driver_id, details):
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
                "section_leader_id": section_leader_id,
                "details": details
            })
