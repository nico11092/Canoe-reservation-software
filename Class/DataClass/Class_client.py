class Client:
    def __init__(self, _id, _nom, _prenom, _telephone) -> None:
        self.id = _id
        self.nom = _nom
        self.prenom = _prenom
        self.telephone = _telephone

    def getId(self) -> int:
        return self.id

    def getNom(self) -> str:
        return self.nom

    def getPrenom(self) -> str:
        return self.prenom

    def getTelephone(self) -> str:
        return self.telephone

    def setId(self, _id) -> None:
        self.id = _id

    def setNom(self, _nom) -> None:
        self.nom = _nom

    def setPrenom(self, _prenom) -> None:
        self.prenom = _prenom

    def setTelephone(self, _telephone) -> None:
        self.telephone = _telephone
