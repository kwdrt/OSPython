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

# TODO: to refator into a PDF class in new file
"""
printed_report = reportService.get_report_data("-MXrGrD-KriOFQsiUMf3")
print(printed_report)

font_dir = os.getcwd() + '\\font\\'

def single_data(pdf_file, text1, text2):
    pdf.set_font('Roboto', 'BI', 12)
    pdf_file.cell(40, 10, text1)
    pdf_file.cell(40)
    pdf_file.set_font('Roboto', "", 8)
    pdf_file.cell(0, 10, text2)
    pdf_file.ln(10)

def long_data(pdf_file, text1, text2):
    pdf.set_font('Roboto', 'BI', 12)
    pdf_file.cell(40, 10, text1)
    pdf_file.set_font('Roboto', "", 8)
    pdf_file.ln(10)
    pdf_file.multi_cell(0,5,text2)
    pdf_file.ln()

def id_to_text(ps, id):
    person = ps.get_person_by_id(id)
    person_data = person.get("FirstName") + " " + person.get("LastName")
    return person_data

def section_to_string(ps, section_table):
    section_string = ""
    for id in section_table:
        section_string += id_to_text(ps, id) + "\n"
    return section_string

pdf = fpdf.FPDF()
pdf.add_page()

#pdf.multi_cell()

pdf.add_font("Roboto", style="", fname= font_dir + "Roboto-Regular.ttf", uni=True)
pdf.add_font("Roboto", style="B", fname= font_dir + "Roboto-Bold.ttf", uni=True)
pdf.add_font("Roboto", style="I", fname= font_dir + "Roboto-Italic.ttf", uni=True)
pdf.add_font("Roboto", style="BI", fname= font_dir + "Roboto-BoldItalic.ttf", uni=True)

pdf.set_font('Roboto', 'BI', 8)
pdf.cell(0, 10, 'Raport z dnia ' + printed_report.get("out_date"), 1, 0, 'C')
pdf.ln(20)

single_data(pdf, "Data wyjazdu", printed_report.get("out_date"))
single_data(pdf, "Godzina wyjazdu", printed_report.get("out_hour"))
single_data(pdf, "Godzina na miejscu", printed_report.get("at_place_hour"))
single_data(pdf, "Rodzaj zdarzenia", printed_report.get("accident_type"))
single_data(pdf, "Miejsce zdarzenia", printed_report.get("place_name"))

# Sekcja inaczej
long_data(pdf, "Skład sekcji", section_to_string(personService, printed_report.get("section_current")))

single_data(pdf, "Dowódca sekcji", id_to_text(personService, printed_report.get("section_leader_id")))
single_data(pdf, "Dowódca akcji", id_to_text(personService, printed_report.get("action_leader_id")))
single_data(pdf, "Kierowca", id_to_text(personService, printed_report.get("driver_id")))

single_data(pdf, "Sprawca", printed_report.get("perpetrator"))
single_data(pdf, "Poszkodowany", printed_report.get("injured"))
long_data(pdf, "Szczegóły zdarzenia", printed_report.get("details"))
single_data(pdf, "Data powrotu", printed_report.get("return_date"))
single_data(pdf, "Godzina zakończenia", printed_report.get("return_hour"))
single_data(pdf, "Godzina w remizie", printed_report.get("depot_hour"))
single_data(pdf, "Stan licznika", printed_report.get("counter_state"))
single_data(pdf, "KM do miejsca zdarzenia", str(printed_report.get("KM_to_place")))


pdf.output("testraport.pdf")

"""

print(reportService.get_report_id_by_fields("01-01-2000,00:00,Niebieska 1"))
