import Class.DataClass.Class_bus as bus
import Class.ModelClass.Model as model

class BusModel(model.Model):
    def __init__(self):
        self.myModel = model.Model()

    def get_bus(self, _date):
        results = self.myModel.get_bus_data(_date)

        bus_list = []

        for result in results:
            _bus = bus.Bus(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
            bus_list.append(_bus)

        return bus_list

    def get_bus_location(self, _date):
        return self.myModel.get_bus_location_data(_date)

    def insert_bus(self, _nom, _nbr_place, _heure, _date, _desti):
        _bus = [ _nom, _nbr_place, _heure, _date, _desti]

        self.myModel.insert_bus_data(_bus)