class Stock:
    def __init__(self, _id, _nom, _nombre) -> None:
        self.id = _id
        self.nom = _nom
        self.nombre = _nombre

    def getId(self) -> int:
        return self.id

    def getNom(self) -> str:
        return self.nom

    def getNombre(self) -> int:
        return self.nombre

    def setId(self, _id) -> None:
        self.id = _id

    def setNom(self, _nom) -> None:
        self.nom = _nom

    def setNombre(self, _nombre) -> None:
        self.nombre = _nombre

    