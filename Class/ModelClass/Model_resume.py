import Class.ModelClass.Model as model

class ResumeModel(model.Model):
    def __init__(self):
        self.myModel = model.Model()

    def get_resum_day(self, _date):
        return self.myModel.get_resum_day_data(_date)[0]

    def get_resum_people_desti(self, _date):
        return self.myModel.get_resum_people_desti_data(_date)

    def get_resum_desti_bat(self, _date):
        return self.myModel.get_resum_desti_bat_data(_date)