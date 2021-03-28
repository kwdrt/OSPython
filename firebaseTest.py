import firebaseUtils as fU

dataService = fU.FireService()
print(dataService.get_all_people())
print("\n")
print(dataService.get_all_reports())
