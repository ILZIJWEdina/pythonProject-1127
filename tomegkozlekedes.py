from datetime import datetime, timedelta

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

class Megallo:
    def __init__(self, nev):
        self.nev = nev
        self.jarmuvek = []

    def hozzaad_jarmu(self, jarmu):
        self.jarmuvek.append(jarmu)
        print(f"{jarmu.tipus} ({jarmu.rendszam}) hozzáadva a {self.nev} megállóhoz.")

class Utas:
    def __init__(self, nev, jegy):
        self.nev = nev
        self.jegy = jegy

class Utazas:
    def __init__(self, utas, jarmu, indulas, erkezes):
        self.utas = utas
        self.jarmu = jarmu
        self.indulas = indulas
        self.erkezes = erkezes

# Példa használat
busz1 = Jarmu("B001", "Busz", "08:00-18:00")
megallo1 = Megallo("Kossuth tér")

busz1.indulas()

busz1.karbantartas()

busz1.befejez_karbantartas()

busz1.indulas()

megallo1.hozzaad_jarmu(busz1)

utas1 = Utas("Alice", "napijegy")
utas2 = Utas("Bob", "havi_bérlet")

utazas1 = Utazas(utas1, busz1, datetime.now(), datetime.now() + timedelta(hours=1))
utazas2 = Utazas(utas2, busz1, datetime.now(), datetime.now() + timedelta(minutes=30))

print(f"{utas1.nev} utazik a(z) {utazas1.jarmu.tipus}-on.")
print(f"{utas2.nev} utazik a(z) {utazas2.jarmu.tipus}-on.")