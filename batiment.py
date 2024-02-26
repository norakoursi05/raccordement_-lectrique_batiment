class Building:
    def __init__(self, id_batiment, list_infras):
        self.id_batiment = id_batiment
        self.list_infras = list_infras
    
    def get_building_difficulty(self):
        return sum(self.list_infras)

    def __lt__(self, autre_batiment):
        return self.get_building_difficulty() < autre_batiment.get_building_difficulty()
