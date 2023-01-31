import Class.ModelClass.Model_resume as model 

class FrameResume():
    def __init__(self):
        self.model = model.ResumeModel()

    def setdate(self, _date):
        self.date = _date 

    def create_frame(self):
        self.nb_personne = self.model.get_resum_day(self.date)[0]
        self.nb_personne_desti = self.model.get_resum_people_desti(self.date)
        self.nb_canoe_dest = self.model.get_resum_desti_bat(self.date)

        if self.nb_personne == None:
            self.nb_personne = 0

        return self.nb_personne, self.nb_personne_desti, self.nb_canoe_dest