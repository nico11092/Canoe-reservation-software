import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import Components.Main_window as myWindow
import Components.Client_window as myClientWindow
import Components.Bus_window as myBusWindow
import Components.Resa_window as myResaWindow

import Class.ViewClass.View_stock as stockView
import Class.ViewClass.View_bus as busView
import Class.ViewClass.View_reservation as reservationView
import Class.ViewClass.View_resume as resumeView
import Class.ViewClass.View_client as clientView

import Class.ExportClass.Export_PDF as PDFExport

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        self.ui = myWindow.Ui_MainWindow()

        #init view 
        self.mySotckView = stockView.FrameStock()
        self.myBusView = busView.FrameBus()
        self.myReservationView = reservationView.FrameReservation()
        self.myResumeView = resumeView.FrameResume()

        self.ui.setupUi(self)

        #date actuelle 
        self.actual_date = str(self.ui.obj_dateEdit.date().toPyDate())

        #attribut recherche actuelle 
        self.actual_search_tel = ""
        self.actual_search_client = ""
        self.actual_search_desti = ""

        #evenement sur le changement de date 
        self.ui.obj_dateEdit.dateChanged.connect(self.search)

        #evenement sur la recherche d'une personne 
        self.ui.obj_search_tel.textChanged.connect(self.search)
        self.ui.obj_search_client.textChanged.connect(self.search)
        self.ui.obj_search_desti.activated.connect(self.search)

        #init les vues avec la date actuelle 
        self.mySotckView.setdate(self.actual_date)
        self.myBusView.setdate(self.actual_date)
        self.myReservationView.setdate(self.actual_date)
        self.myResumeView.setdate(self.actual_date)

        #init les vues avec les données 
        self.init_frame_stock()
        self.init_frame_bus()
        self.init_frame_reservation()
        self.init_frame_resume()

        #init la fenetre dialog d'ajout client 
        self.Dialog_client = QDialog()
        self.ui_client = myClientWindow.Ui_Dialog()
        self.ui_client.setupUi(self.Dialog_client)

        #init la fenetre dialog d'ajout bus 
        self.Dialog_bus = QDialog()
        self.ui_bus = myBusWindow.Ui_Dialog()
        self.ui_bus.setupUi(self.Dialog_bus)

        #init la fenetre dialog d'ajout reservation 
        self.Dialog_resa = QDialog()
        self.ui_resa = myResaWindow.Ui_Dialog()
        self.ui_resa.setupUi(self.Dialog_resa)

        #evenement sur la saisie prenom dans fenetre dialog d'ajout reservation 
        self.ui_resa.obj_resa_nom.editTextChanged.connect(self.update_combo)


    def init_frame_stock(self):
        liste = self.mySotckView.create_frame()

        self.ui.obj_table_stock.setRowCount(len(liste))

        for i in range(len(liste)):
            for j in range(len(liste[i])):
                item = QTableWidgetItem(liste[i][j])
                self.ui.obj_table_stock.setItem(i, j, item)

    def init_frame_bus(self):
        liste = self.myBusView.create_frame()

        self.ui.obj_table_bus.setRowCount(len(liste))

        for i in range(len(liste)):
            for j in range(len(liste[i])):
                item = QTableWidgetItem(liste[i][j])
                self.ui.obj_table_bus.setItem(i, j, item)

    def init_frame_reservation(self):
        liste = self.myReservationView.create_frame(self.actual_search_tel, self.actual_search_client, self.actual_search_desti)

        self.ui.obj_table_reservation.setRowCount(len(liste))

        for i in range(len(liste)):
            for j in range(len(liste[i])):
                item = QTableWidgetItem(str(liste[i][j]))
                self.ui.obj_table_reservation.setItem(i, j, item)

    def init_frame_resume(self):
        nb_pers, liste, nb_bat_desti = self.myResumeView.create_frame()

        self.ui.obj_nb_pers.setText(str(nb_pers))

        self.ui.obj_table_nb_pers_desti.setRowCount(len(liste))

        for i in range(len(liste)):
            for j in range(len(liste[i])):
                item = QTableWidgetItem(str(liste[i][j]))
                self.ui.obj_table_nb_pers_desti.setItem(i, j, item)

        
        nom_bat = ["Canoë", "Canoë confort","Kayak","Grand canoë","Paddle","Big Sup"]

        self.ui.obj_tree.setHeaderLabels(["", ""])
        self.ui.obj_tree.setColumnWidth(0,200)
        for i in range(len(nb_bat_desti)):
            for j in range(len(nb_bat_desti[i])):
                if j == 0:
                    item = QTreeWidgetItem([str(nb_bat_desti[i][j]), ""])
                    self.ui.obj_tree.addTopLevelItem(item)
                else:
                    if nb_bat_desti[i][j] != 0:
                        item.addChild(QTreeWidgetItem([nom_bat[j-1], str(nb_bat_desti[i][j])]))
        self.ui.obj_tree.expandAll()

    def search(self):
        self.actual_date = str(self.ui.obj_dateEdit.date().toPyDate())
        self.actual_search_tel = str(self.ui.obj_search_tel.text())
        self.actual_search_client = str(self.ui.obj_search_client.text())
        self.actual_search_desti = str(self.ui.obj_search_desti.currentText())


        #on remet les tables à 0
        self.ui.obj_table_stock.setRowCount(0)
        self.ui.obj_table_bus.setRowCount(0)
        self.ui.obj_table_reservation.setRowCount(0)
        self.ui.obj_table_nb_pers_desti.setRowCount(0)

        #on remet le tree à 0
        self.ui.obj_tree.clear()

        #on change la date actuelle des vues
        self.mySotckView.setdate(self.actual_date)
        self.myBusView.setdate(self.actual_date)
        self.myReservationView.setdate(self.actual_date)
        self.myResumeView.setdate(self.actual_date)

        #on met à jour toutes les frames 
        self.init_frame_stock()
        self.init_frame_bus()
        self.init_frame_reservation()
        self.init_frame_resume()

    def remise_zero(self):
        #on reinitialise les obj 
        self.ui.obj_search_tel.setText("")
        self.ui.obj_search_client.setText("")
        self.ui.obj_search_desti.setCurrentText("")

        self.search()

    def add_client(self):
        #on lance la fenetre d'ajout 
        returnValue = self.Dialog_client.exec_()

        if returnValue == 1:
            #on ajoute le client à la base de données, on recupere les infos 
            client_nom = self.ui_client.obj_client_nom.text()
            client_prenom = self.ui_client.obj_client_prenom.text()
            client_telephone = self.ui_client.obj_client_tel.text()

            self.myClientView = clientView.FrameClient()
            self.myClientView.insert(client_nom, client_prenom, client_telephone)

    def add_bus(self):
        #on lance la fenetre d'ajout
        returnValue = self.Dialog_bus.exec_()

        if returnValue == 1:
            bus_nom = self.ui_bus.obj_bus_nom.text()
            bus_place = self.ui_bus.obj_bus_place.value()
            bus_date = str(self.ui_bus.obj_bus_date.date().toPyDate())
            bus_heure = str(self.ui_bus.obj_bus_date.time().toPyTime())
            bus_desti = self.ui_bus.obj_bus_desti.currentIndex()

            self.myBusView.insert(bus_nom, bus_place, bus_heure, bus_date, bus_desti)

            #on met à jour la fenetre bus 
            self.ui.obj_table_bus.setRowCount(0)
            self.init_frame_bus()

    def add_resa(self):
        #on saisie les index de la combobox client 
        list_client = self.myReservationView.get_client("")
        self.ui_resa.obj_resa_nom.addItem("")
        for i in range(len(list_client)):
            self.ui_resa.obj_resa_nom.addItem(list_client[i].getNom()+" "+list_client[i].getPrenom())

        #on lance la fenetre d'ajout 
        self.Dialog_resa.exec_()
     
    def update_combo(self):
        _saisie = self.ui_resa.obj_resa_nom.currentText()

        list_client = self.myReservationView.get_client(_saisie)

        for i in range(4):
            if i < len(list_client):
                self.ui_resa.obj_resa_nom.setItemText(i+1,list_client[i].getNom()+" "+list_client[i].getPrenom())
            else: 
                self.ui_resa.obj_resa_nom.setItemText(i+1,"")

    def export(self):
        self.myExportPDF = PDFExport.PDFExport("")
        self.myExportPDF.create_PDF()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()