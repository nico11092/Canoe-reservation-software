import Class.ModelClass.Model_export as model 
from fpdf import FPDF

class PDFExport():
    def __init__(self, _date):
        self.model = model.ExportModel()
        self.date = _date

    def get_data(self):
        return self.model.get_export(self.date)

    def create_PDF(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)
        pdf.set_fill_color(230, 230, 230)

        #titre 
        pdf.cell(200, 10, txt="Fiche navette du + date", ln=1, align="C")

        #recuperation des données 
        data = self.get_data()

        currentLine = 3
        currentCity = ""
        line = ""
        for i in range(len(data)):
            if currentCity != data[i][0]:
                currentCity = data[i][0]
                pdf.cell(200, 10, txt=str(data[i][0]), ln=currentLine, align="C")
                currentLine+=2

                # create the table headers
                pdf.cell(35, 10, "Client", 1, 0, "C", 1)
                pdf.cell(35, 10, "Téléphone", 1, 0, "C", 1)
                pdf.cell(35, 10, "Date / Heure", 1, 0, "C", 1)
                pdf.cell(15, 10, "Nb Pers.", 1, 0, "C", 1)
                pdf.cell(75, 10, "Bateaux", 1, 0, "C", 1)
                pdf.ln()

             
            pdf.cell(35,10,str(data[i][1] + " " + data[i][2]),1,0,"C")
            pdf.cell(35,10,str(data[i][3]),1,0,"C")
            pdf.cell(35,10,str(data[i][4] + " / " + data[i][5]),1,0,"C")
            pdf.cell(15,10,str(data[i][6]),1,0,"C")
            pdf.cell(75,10,f"C "+str(data[i][7])+" | CC "+str(data[i][8])+" | K "+str(data[i][9])+" | GC "+str(data[i][10])+" | PAD "+str(data[i][11])+" | BSU "+str(data[i][12]),1,1,"L")

        pdf.output("..//..//Assets//Export//Fiche_navette.pdf").encode('latin1')
        

    
#rajout : 
#mettre la date dans le titre 
#mettre la date dans le nom du fichier
