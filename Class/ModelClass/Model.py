import Class.DataBase.Config as database

class Model:
    def __init__(self):
        mybd = database.Database()
        self.connexion = mybd.getConnexion()


    ###########################
    #    requete vue stock    #
    ###########################

    #Recuperation des stocks 
    def get_stock_data(self):
        myRequest = "Select * from Stock"

        link = self.connexion.cursor()
        link.execute(myRequest)

        results = link.fetchall()

        return results

    #Recuperation du nombre de location par bateau en fonction d'une date donnée 
    def get_stock_location_data(self, _date):
        myRequest = "select sum(nbr_c), sum(nbr_cc), sum(nbr_k), sum(nbr_gc), sum(nbr_p), sum(nbr_b) from Reservation_bateau rb join Reservation r on r.id = rb.id where r.date = '" + str(_date) + "'"

        link = self.connexion.cursor()
        link.execute(myRequest)

        results = link.fetchall()

        return results


    ###########################
    #     requete vue bus     #
    ###########################

    #Recuperation des bus en fonction d'une date donnée
    def get_bus_data(self, _date):
        myRequest = "Select b.id, b.nom, b.nbr_place, b.heure, b.date, d.id, d.nom from Bus b join Destination d on d.id = b.destination where date = '" + str(_date) +"'"

        link = self.connexion.cursor()
        link.execute(myRequest)

        results = link.fetchall()

        return results

    #Recuperation du nombre de personne dans chaque bus en fonction d'une date donnée 
    def get_bus_location_data(self, _date):
        myRequest = "Select bus, sum(nbr_perso) from Reservation where date = '" + str(_date) +"' group by bus"

        link = self.connexion.cursor()
        link.execute(myRequest)

        results = link.fetchall()

        return results

    ###########################
    #   requete vue resume    #
    ###########################

    #Recuperation du nombre de personne en fonction d'une date donnée
    def get_resum_day_data(self, _date):
        myRequest = "select sum(nbr_perso) from reservation where date = '" + str(_date) +"'"

        link = self.connexion.cursor()
        link.execute(myRequest)

        results = link.fetchall()

        return results

    #Recuperation du nombre de personne par destination en fonction d'une date donnée 
    def get_resum_people_desti_data(self, _date):
        myRequest = "select d.nom, sum(r.nbr_perso) from reservation r join Destination d on d.id = r.destination where r.date = '" + str(_date) + "' group by r.destination"

        link = self.connexion.cursor()
        link.execute(myRequest)

        results = link.fetchall()

        return results

    #Recuperation du nombre et du type de bateau en fonction d'une destination et d'une date donnée
    def get_resum_desti_bat_data(self, _date):
        myRequest = " select d.nom, sum(rb.nbr_c), sum(rb.nbr_cc), sum(rb.nbr_k), sum(rb.nbr_gc), sum( rb.nbr_p), sum( rb.nbr_b) from Reservation r join Destination d on d.id = r.destination join Reservation_bateau rb on rb.id = r.id where r.date = '" + str(_date) + "' group by d.id"

        link = self.connexion.cursor()
        link.execute(myRequest)

        results = link.fetchall()

        return results


    ###########################
    #    requete vue resa     #
    ###########################

    #Recuperation des reservations en fonction d'une date donnée 
    def get_resa_data(self, _date, _search):
        myRequest = "select d.nom as Desti, c.nom as Client, r.nbr_perso, c.telephone, r.heure, r.date, rb.nbr_c, rb.nbr_cc, rb.nbr_k, rb.nbr_gc, rb.nbr_p, rb.nbr_b from Reservation r join Destination d on d.id = r.destination join Client c on c.id = r.client  join Reservation_bateau rb on rb.id = r.id where r.date = '" + str(_date) +"' " + _search

        link = self.connexion.cursor()
        link.execute(myRequest)

        results = link.fetchall()

        return results


    ###########################
    #   requete Diag Client   #
    ###########################
    def insert_client_data(self, _client):
        myRequest = "insert into CLient(nom, prenom, telephone) values(?,?,?)"

        link = self.connexion.cursor()
        link.execute(myRequest, _client)

        self.connexion.commit()

    ###########################
    #     requete Diag Bus    #
    ###########################
    def insert_bus_data(self, _bus):
        myRequest = "insert into Bus(nom, nbr_place, heure, date, destination) values(?,?,?,?,?)"

        link = self.connexion.cursor()
        link.execute(myRequest, _bus)

        self.connexion.commit()

    ###########################
    #    requete Diag Resa    #
    ###########################
    def get_resa_client_data(self, _saisie):
        myRequest = "select * from Client where nom like '"+str(_saisie)+"%' limit 4"

        link = self.connexion.cursor()
        link.execute(myRequest)

        results = link.fetchall()

        return results

    ###########################
    #   requete Diag Export   #
    ###########################
    def get_export_data(self, _date):
        myRequest = "select d.nom, c.nom, c.prenom, c.telephone, r.date, r.heure, r.nbr_perso, rb.nbr_c, rb.nbr_cc, rb.nbr_k, rb.nbr_gc, rb.nbr_p, rb.nbr_b from Reservation r join Client c on c.id = r.client join Destination d on d.id = r.destination join Reservation_bateau rb on rb.id = r.id order by d.nom desc, r.heure"

        link = self.connexion.cursor()
        link.execute(myRequest)

        results = link.fetchall()

        return results



    