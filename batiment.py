class Batiment:
    def __init__(self, id_batiment, liste_infras):
        self.id_batiment = id_batiment
        self.liste_infras = liste_infras
    
    def obtenir_difficulte_batiment(self):
        return sum(self.liste_infras)

    def __lt__(self, autre_batiment):
        return self.obtenir_difficulte_batiment() < autre_batiment.obtenir_difficulte_batiment()
