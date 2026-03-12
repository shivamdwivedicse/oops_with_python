class Factory:
    def __init__(self,material,zip):
        self.material = material
        self.zip = zip

class BhopalFactory(Factory):
    def __init__(self, material, zip,color):
        super().__init__(material, zip)
        self.color = color

class PuneFactory(BhopalFactory):
    def __init__(self, material, zip, color,pockets):
        super().__init__(material, zip, color)
        self.pockets = pockets


obj = PuneFactory()
