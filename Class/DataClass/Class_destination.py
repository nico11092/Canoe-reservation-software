class Destination:
    def __init__(self, _id, _nom) -> None:
        self.id = _id
        self.nom = _nom

    def getId(self) -> int:
        return self.id

    def getNom(self) -> str:
        return self.nom

    def setId(self, _id) -> None:
        self.id = _id

    def setNom(self, _nom) -> None:
        self.nom = _nom

    