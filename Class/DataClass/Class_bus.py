import Class.DataClass.Class_destination as destination

class Bus:
    def __init__(self, _id, _nom, _nb_place, _heure, _date, _id_desti, _nom_desti) -> None:
        self.id = _id
        self.nom = _nom
        self.nb_place = _nb_place
        self.destination = destination.Destination(_id_desti, _nom_desti)
        self.heure = _heure
        self.date = _date

    def getId(self) -> int:
        return self.id

    def getNom(self) -> str:
        return self.nom

    def getNb_place(self) -> int:
        return self.nb_place

    def getDestination(self) -> destination.Destination:
        return self.destination

    def getHeure(self) -> str:
        return self.heure

    def getDate(self) -> str:
        return self.date

    def setId(self, _id) -> None:
        self.id = _id

    def setNom(self, _nom) -> None:
        self.nom = _nom

    def setNb_place(self, _nb_place) -> None:
        self.nb_place = _nb_place

    def setDestination(self, _destination) -> None:
        self.destination = _destination

    def setHeure(self, _heure) -> None:
        self.heure = _heure

    def setDate(self, _date) -> None:
        self.date = _date