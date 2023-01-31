import Class.ModelClass.Model as model

class ExportModel(model.Model):
    def __init__(self):
        self.mymodel = model.Model()

    def get_export(self, _date):
        return self.mymodel.get_export_data(_date)