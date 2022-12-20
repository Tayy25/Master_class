class Vivan:
    def __init__(self, pye, men, non, laj):
        self.pye = pye
        self.men = men
        self.non = non
        self.laj = laj

    def sepresenter(self):
        print("je m'appelle",self.non,"j'ai",self.laj,"ans", "et j'ai",self.men,"main et",self.pye,"pied")

taina = Vivan(2, 2, "Taina", 23)


taina.sepresenter()

doumy = Vivan(2, 2, "Doumy", 22)

doumy.sepresenter()

class Poul(Vivan):

    def __init__(self, pye, laj, men, non):
        super().__init__(pye, men, non, laj)


poul1 = Poul(2, 1, 2, "tipoul",)
poul1.sepresenter()