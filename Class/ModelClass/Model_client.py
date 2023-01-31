import Class.DataClass.Class_client as client
import Class.ModelClass.Model as model

class ClientModel(model.Model):
    def __init__(self):
        self.mymodel = model.Model()

    def insert_client(self, _nom, _prenom, _tel):
        _client = [_nom, _prenom, _tel]

        self.mymodel.insert_client_data(_client)