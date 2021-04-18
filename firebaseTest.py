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

printed_report = reportService.get_report_data("-MXrGrD-KriOFQsiUMf3")
print(printed_report)

font_dir = os.getcwd() + '\\font\\'

def single_data(pdf_file, text1, text2):
    pdf.set_font('Roboto', 'BI', 14)
    pdf_file.cell(40, 10, text1)
    pdf_file.ln(15)
    pdf_file.set_font('Roboto', "", 10)
    pdf_file.cell(40, 10, text2)
    pdf_file.ln(20)


pdf = fpdf.FPDF()
pdf.add_page()

pdf.add_font("Roboto", style="", fname= font_dir + "Roboto-Regular.ttf", uni=True)
pdf.add_font("Roboto", style="B", fname= font_dir + "Roboto-Bold.ttf", uni=True)
pdf.add_font("Roboto", style="I", fname= font_dir + "Roboto-Italic.ttf", uni=True)
pdf.add_font("Roboto", style="BI", fname= font_dir + "Roboto-BoldItalic.ttf", uni=True)

pdf.set_font('Roboto', 'BI', 14)
pdf.cell(80)
pdf.cell(30, 10, 'Raport', 1, 0, 'C')
pdf.ln(20)

single_data(pdf, "Nagłówek sekcji", "dane nizej pod naglowkiem")
single_data(pdf, u"""Nagłówek sekcji""", "dane nizej pod naglowkiem")
single_data(pdf, u"""Nagłówek sekcji""", "dane nizej pod naglowkiem")

pdf.output("testraport.pdf")

