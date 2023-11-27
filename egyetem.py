class Diak:
    def __init__(self, nev, diakazonosito, tanulmanyi_atlag):
        self.nev = nev
        self.diakazonosito = diakazonosito
        self.tanulmanyi_atlag = tanulmanyi_atlag
        self.osztalyzatok = []

    def diak_informacio(self):
        return f"{self.nev} (Diákazonosító: {self.diakazonosito}), Tanulmányi átlag: {self.tanulmanyi_atlag}"

class Tanar:
    def __init__(self, nev, munkatarsi_azonosito, szak):
        self.nev = nev
        self.munkatarsi_azonosito = munkatarsi_azonosito
        self.szak = szak

    def tanar_informacio(self):
        return f"{self.nev} (Munkatársi azonosító: {self.munkatarsi_azonosito}), Szak: {self.szak}"

class Kurzus:
    def __init__(self, kurzuskod, nev, tanar):
        self.kurzuskod = kurzuskod
        self.nev = nev
        self.tanar = tanar
        self.osztalyzatok = []

    def kurzus_informacio(self):
        return f"{self.nev} (Kurzuskód: {self.kurzuskod}), Tanár: {self.tanar.tanar_informacio()}"

class Osztalyzat:
    def __init__(self, diak, kurzus, erdemjegy):
        self.diak = diak
        self.kurzus = kurzus
        self.erdemjegy = erdemjegy

    def osztalyzat_informacio(self):
        return f"{self.diak.diak_informacio()} kapott osztályzatot a következő kurzuson: {self.kurzus.kurzus_informacio()}, Érdemjegy: {self.erdemjegy}"

# Példa használat
tanar1 = Tanar("Dr. Példa Tanár", "1234", "Informatika")
tanar2 = Tanar("Dr. Másik Tanár", "5678", "Matematika")

diak1 = Diak("John Doe", "001", 4.5)
diak2 = Diak("Jane Doe", "002", 4.2)

kurzus1 = Kurzus("CS101", "Programozás alapjai", tanar1)
kurzus2 = Kurzus("MATH101", "Matematika I", tanar2)

osztalyzat1 = Osztalyzat(diak1, kurzus1, 5)
osztalyzat2 = Osztalyzat(diak2, kurzus2, 4)

print(diak1.diak_informacio())
print(tanar1.tanar_informacio())
print(kurzus1.kurzus_informacio())
print(osztalyzat1.osztalyzat_informacio())