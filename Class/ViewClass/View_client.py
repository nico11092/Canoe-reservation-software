import Class.ModelClass.Model_client as model

class FrameClient():
    def __init__(self):
        self.model = model.ClientModel()

    def insert(self, _nom, _prenom, _tel):
        self.model.insert_client(_nom, _prenom, _tel)
