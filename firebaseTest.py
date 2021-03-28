import firebaseUtils as fU

personService = fU.PersonService()
reportService = fU.ReportService()

print(personService.get_all_people())
print("\n")
print(reportService.get_all_reports())

personService.add_person()

print(personService.get_all_people())
