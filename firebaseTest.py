import firebaseUtils as fU

personService = fU.PersonService()
reportService = fU.ReportService()

#
print(personService.get_all_people())
print("\n")
print(reportService.get_all_reports())

#person existence check
print(personService.check_person_existence("Jan", "Kowalski", 123456789))
print(personService.check_person_existence("Jan", "Kowalski", 123256789))

#person data change check
id_changed = personService.check_person_existence("Jan", "Kowalski", 123456789)
personService.change_person_data(id_changed, "Jan", "Kowalski2", 666666666, 1, 1, 1, 1)