import Class.ModelClass.Model_bus as model 

class FrameBus():
    def __init__(self):
        self.model = model.BusModel()

    def setdate(self, _date):
        self.date = _date 

    def create_frame(self):
        self.bus = self.model.get_bus(self.date)
        self.location = self.model.get_bus_location(self.date)

        self.liste = []
        for i in range(len(self.bus)):
            if len(self.location) > i:
                place = self.bus[i].getNb_place() - self.location[i][1]
            else:
                place = self.bus[i].getNb_place()
            _list = [self.bus[i].getDestination().getNom() + " " + self.bus[i].getHeure() , str(place)]
            self.liste.append(_list)

        return self.liste

    def insert(self, _nom, _nbr_place, _heure, _date, _desti):
        self.model.insert_bus(_nom, _nbr_place, _heure, _date, _desti)