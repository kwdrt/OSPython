# PDFgen(id_szukanego)
import os
import fpdf
import firebaseUtils as fU

class PDFgen:

    def __init__(self, printed_report_id, ps, rs):
        self.ps = ps
        self.rs = rs
        self.font_dir = os.getcwd() + '\\font\\'
        self.pdf = fpdf.FPDF()
        self.printed_report = self.rs.get_report_data(printed_report_id)
        self.generate_report()

    #printed_report = reportService.get_report_data("-MXrGrD-KriOFQsiUMf3")






    def single_data(self, pdf_file, text1, text2):
        self.pdf.set_font('Roboto', 'BI', 12)
        pdf_file.cell(40, 10, text1)
        pdf_file.cell(40)
        pdf_file.set_font('Roboto', "", 8)
        pdf_file.cell(0, 10, text2)
        pdf_file.ln(10)

    def long_data(self, pdf_file, text1, text2):
        self.pdf.set_font('Roboto', 'BI', 12)
        pdf_file.cell(40, 10, text1)
        pdf_file.set_font('Roboto', "", 8)
        pdf_file.ln(10)
        pdf_file.multi_cell(0,5,text2)
        pdf_file.ln()

    def id_to_text(self, id):
        person = self.ps.get_person_by_id(id)
        person_data = person.get("FirstName") + " " + person.get("LastName")
        return person_data

    def section_to_string(self, section_table):
        section_string = ""
        for id in section_table:
            section_string += self.id_to_text(id) + "\n"
        return section_string

    def generate_report(self):

        self.pdf.add_page()

        self.pdf.add_font("Roboto", style="", fname= self.font_dir + "Roboto-Regular.ttf", uni=True)
        self.pdf.add_font("Roboto", style="B", fname= self.font_dir + "Roboto-Bold.ttf", uni=True)
        self.pdf.add_font("Roboto", style="I", fname= self.font_dir + "Roboto-Italic.ttf", uni=True)
        self.pdf.add_font("Roboto", style="BI", fname= self.font_dir + "Roboto-BoldItalic.ttf", uni=True)

        self.pdf.set_font('Roboto', 'BI', 8)
        self.pdf.cell(0, 10, 'Raport z dnia ' + self.printed_report.get("out_date"), 1, 0, 'C')
        self.pdf.ln(20)

        self.single_data(self.pdf, "Data wyjazdu", self.printed_report.get("out_date"))
        self.single_data(self.pdf, "Godzina wyjazdu", self.printed_report.get("out_hour"))
        self.single_data(self.pdf, "Godzina na miejscu", self.printed_report.get("at_place_hour"))
        self.single_data(self.pdf, "Rodzaj zdarzenia", self.printed_report.get("accident_type"))
        self.single_data(self.pdf, "Miejsce zdarzenia", self.printed_report.get("place_name"))

        # Sekcja inaczej
        self.long_data(self.pdf, "Skład sekcji", self.section_to_string(self.printed_report.get("section_current")))

        self.single_data(self.pdf, "Dowódca sekcji", self.id_to_text(self.printed_report.get("section_leader_id")))
        self.single_data(self.pdf, "Dowódca akcji", self.id_to_text(self.printed_report.get("action_leader_id")))
        self.single_data(self.pdf, "Kierowca", self.id_to_text(self.printed_report.get("driver_id")))

        self.single_data(self.pdf, "Sprawca", self.printed_report.get("perpetrator"))
        self.single_data(self.pdf, "Poszkodowany", self.printed_report.get("injured"))
        self.long_data(self.pdf, "Szczegóły zdarzenia", self.printed_report.get("details"))
        self.single_data(self.pdf, "Data powrotu", self.printed_report.get("return_date"))
        self.single_data(self.pdf, "Godzina zakończenia", self.printed_report.get("return_hour"))
        self.single_data(self.pdf, "Godzina w remizie", self.printed_report.get("depot_hour"))
        self.single_data(self.pdf, "Stan licznika", self.printed_report.get("counter_state"))
        self.single_data(self.pdf, "KM do miejsca zdarzenia", str(self.printed_report.get("KM_to_place")))

        parsed_hour = self.printed_report.get("out_hour")
        parsed_hour = parsed_hour.replace(":", "-")

        report_name = "Raport" + "-" + self.printed_report.get("out_date") + "--" + parsed_hour + ".pdf"

        self.pdf.output(report_name)


#test block of code with example call
ps = fU.PersonService()
rs = fU.ReportService()
PDFgen("-MXrGrD-KriOFQsiUMf3", ps, rs)