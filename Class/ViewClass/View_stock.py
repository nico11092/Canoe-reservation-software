import Class.ModelClass.Model_stock as model

class FrameStock():
    def __init__(self):
        self.model = model.StockModel()

    def setdate(self, _date):
        self.date = _date

    def create_frame(self):
        self.stock = self.model.get_stock()
        self.location = self.model.get_stock_location(self.date)[0]

        self.liste = []
        for i in range(len(self.stock)):
            if self.location[i] != None:
                location_jour = self.location[i]
                quantite = self.stock[i].getNombre() - location_jour
            else: 
                location_jour = 0
                quantite = self.stock[i].getNombre()
            _list = [self.stock[i].getNom(), str(location_jour), str(self.stock[i].getNombre()), str(quantite)]
            self.liste.append(_list)

        return self.liste