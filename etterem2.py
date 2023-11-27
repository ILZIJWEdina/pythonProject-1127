class Etterem:
    def __init__(self, nev, menu):
        self.nev = nev
        self.menu = menu
        self.ertekelesek = []

    def frissit_menu(self, uj_menu):
        self.menu = uj_menu
        print(f"{self.nev} étterem menüje frissítve.")

    def erdkelesek_megtekintese(self):
        print(f"{self.nev} étterem értékelései:")
        for ertekeles in self.ertekelesek:
            print(f"{ertekeles['felhasznalo']}: {ertekeles['ertekeles']}")

class Felhasznalo:
    def __init__(self, nev, email):
        self.nev = nev
        self.email = email

class Rendeles:
    def __init__(self, felhasznalo, etterem, tetelek):
        self.felhasznalo = felhasznalo
        self.etterem = etterem
        self.tetelek = tetelek
        self.statusz = "Feldolgozás alatt"

    def rendeles_megtekintese(self):
        print(f"Rendelés a következő étteremből: {self.etterem.nev}")
        print("Rendelt tételek:")
        for tetelek in self.tetelek:
            print(f"{tetelek['nev']} - {tetelek['ar']}")
        print(f"Rendelés állapota: {self.statusz}")

# Példa használat
etterem1 = Etterem("Kifőzde Kuckó", [{"nev": "Halászlé", "ar": 1500}, {"nev": "Lecsó", "ar": 1200}])
etterem2 = Etterem("Pasta Paradiso", [{"nev": "Spagetti Bolognese", "ar": 1800}, {"nev": "Pizza Margherita", "ar": 1600}])

felhasznalo = Felhasznalo("Alice Smith", "alice.smith@example.com")

rendel1 = Rendeles(felhasznalo, etterem1, [{"nev": "Halászlé", "ar": 1500}, {"nev": "Pizza Margherita", "ar": 1600}])

etterem1.erdkelesek_megtekintese()

rendel1.rendeles_megtekintese()