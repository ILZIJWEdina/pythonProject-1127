class Jarmu:
    def __init__(self, rendszam, tipus, uzemido):
        self.rendszam = rendszam
        self.tipus = tipus
        self.uzemido = uzemido
        self.karbantartas_alatt = False

    def indulas(self):
        if not self.karbantartas_alatt:
            print(f"{self.tipus} ({self.rendszam}) indulásra kész.")
        else:
            print(f"{self.tipus} ({self.rendszam}) karbantartás alatt áll, nem indulhat.")

    def karbantartas(self):
        self.karbantartas_alatt = True
        print(f"{self.tipus} ({self.rendszam}) karbantartás alatt van.")

    def befejez_karbantartas(self):
        self.karbantartas_alatt = False
        print(f"{self.tipus} ({self.rendszam}) karbantartása befejeződött.")
        