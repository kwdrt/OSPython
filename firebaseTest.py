import os

import firebaseUtils as fU
import fpdf

print()

personService = fU.PersonService()
reportService = fU.ReportService()

#
#print(personService.get_all_people())
#print("\n")
#print(reportService.get_all_reports())

# person existence check
#print(personService.check_person_existence("Jan", "Kowalski2", 666666666))
#print(personService.check_person_existence("Jan", "Kowalski", 123256789))

# person data change check
#id_changed = personService.check_person_existence("Jan", "Kowalski2", 666666666)
#personService.change_person_data(id_changed, "Jan", "KowalskiZmiana", 666666666, 1, 1, 1, 1)

# add new report
#reportService.add_report(30, "kot na drzewie", "10-10-2010", "22:12", "2000001",
#                         "01:41", "Maria Nowak", "10-10-2010", "22:00",
#                         "Kot Filemon", "Ogrodowa 12", "11-10-2010", "01:55",
#                         ["key2", "key4", "key12"], 5, 0, 11, 2, "szczegoly zdarzenia")


# -MXrGrD-KriOFQsiUMf3 to print

# data wyjazdu
# godzina wyjazdu
# godzina na miejscu
# rodzaj zdarzenia
# miejsce zdarzenia
# sekcja
# dowódca sekcji
# dwd akcji
# kierowca
# sprawca
# poszkodowany
# szczegóły zdarzenia
# data powrotu
# godzina zakończenia
# godzina w remizie
# stan licznika
# KM do miejsca zdarzenia



print(reportService.get_report_id_by_fields("01-01-2000,00:00,Niebieska 1"))
