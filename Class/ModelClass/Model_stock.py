import Class.DataClass.Class_stock as stock
import Class.ModelClass.Model as model

class StockModel(model.Model):
    def __init__(self):
        self.myModel = model.Model()

    def get_stock(self):
        results = self.myModel.get_stock_data()

        stock_list = []

        for result in results:
            _stock = stock.Stock(result[0], result[1], result[2])
            stock_list.append(_stock)

        return stock_list

    def get_stock_location(self, _date):
        return self.myModel.get_stock_location_data(_date)

        