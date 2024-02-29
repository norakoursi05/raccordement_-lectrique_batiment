class Infra:
    def __init__(self, infra_id, longueur, infra_type, nb_maisons):
        self.infra_id = infra_id
        self.longueur = longueur
        self.infra_type = infra_type
        self.nb_maisons = nb_maisons

    def reparer_infra(self):
        self.type_infra = "infra_intacte"
    
    def obtenir_difficulte_infra(self):
        if self.infra_type == "infra_intacte":
            return 0
        else:
            return self.longueur / self.nb_maisons
    
    def __radd__(self, autre_infra):
        return self.obtenir_difficulte_infra() + autre_infra
