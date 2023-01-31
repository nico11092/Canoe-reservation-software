import Class.ModelClass.Model_reservation as model
import Class.DataClass.Class_client as Client

class FrameReservation():
    def __init__(self):
        self.liste_client = []
        self.model = model.ReservationModel()

    def setdate(self, _date):
        self.date = _date

    def create_frame(self, _tel, _nom, _desti):
        search = "and c.telephone like '0ù%' and c.nom like '0ù%' and d.nom like '0ù%'"
        search = search.replace("0ù", str(_tel), 1)
        search = search.replace("0ù", str(_nom), 1)
        search = search.replace("0ù", str(_desti), 1)

        self.reservation = self.model.get_reservation(self.date, search)
        
        self.liste = []

        for i in range(len(self.reservation)):
            bateau = self.setBateau(self.reservation[i])
            _list = [self.reservation[i][0], self.reservation[i][1], self.reservation[i][2], self.reservation[i][3], self.reservation[i][4], self.reservation[i][5], bateau]
            self.liste.append(_list)

        return self.liste

    def setBateau(self, liste):
        bateau = "C 0B | CC 0B | K 0B | GC 0B | PAD 0B | BSU 0B"

        for i in range(6, len(liste)):
            if liste[i] > 10:
                bateau = bateau.replace("0B", str(liste[i]), 1)
            else: 
                bateau = bateau.replace("0B", str("0"+str(liste[i])), 1)
        
        return bateau

    def get_client(self, _saisie):
        self.liste_client.clear()
        
        _lists = self.model.get_resa_client(_saisie)
        for _list in _lists:
            client = Client.Client(_list[0], _list[1], _list[2], _list[3])
            self.liste_client.append(client)

        return self.liste_client
