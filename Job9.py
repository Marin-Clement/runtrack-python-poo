class Produit:
    def __init__(self, name, priceHT, TVA):
        self.name = name
        self.priceHT = priceHT
        self.TVA = TVA

    def calculateTTC(self):
        return round(self.priceHT * (1 + self.TVA / 100), 2)

    def change_name(self, name):
        self.name = name

    def change_price(self, price):
        self.priceHT = price

    def show_tva(self):
        return self.TVA

    def show_price(self):
        return self.priceHT

    def show_name(self):
        return self.name

    def show(self):
        return self.name, self.priceHT, self.TVA, self.calculateTTC()


print(Produit("Pot", 25, 20).show())
print(Produit("Xbox", 350, 20).show())
