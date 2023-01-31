import Class.ModelClass.Model as model

class ReservationModel(model.Model):
    def __init__(self):
        self.myModel = model.Model()

    def get_reservation(self, _date, _search):
        return self.myModel.get_resa_data(_date, _search)

    def get_resa_client(self, _saisie):
        return self.myModel.get_resa_client_data(_saisie)