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
