HINTA = 5

class Kassapaate:
    def __init__(self):
        pass

    def osta_lounas(self, maksukortti):
        if maksukortti.saldo >= HINTA:
            maksukortti.osta(HINTA)

    def lataa(self, maksukortti, summa):
        if summa > 0:
            maksukortti.lataa(summa)
