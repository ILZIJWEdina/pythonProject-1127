class Etel:
    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar

    def __str__(self):
        return f"{self.nev}.................{self.ar} Ft"

class Etterem:
    def __init__(self, nev):
        self.nev = nev
        self.menu = []

    def __str__(self):
        return f"{self.nev}"

    def get_menu_items(self):
        if not self.menu:
            return "Az étteremnek nincs még menüje."

        menu_str = f"{self.nev} Menü:\nNÉV......................ÁR Ft"
        for etel in self.menu:
            menu_str += f"\n{etel}"
        return menu_str

    def hozzaad_menu_elem(self, etel):
        if etel.ar <= 0 or etel.ar > 100000:
            print("Hibás érték. Az étel ára nem lehet 0-nál kisebb, vagy 100000 Ft-nál nagyobb.")
        else:
            self.menu.append(etel)
            print(f"{etel.nev} hozzáadva a(z) {self.nev} étterem menüjéhez.")

    def __add__(self, etel):
        if etel.ar <= 0 or etel.ar > 100000:
            print("Hibás érték. Az étel ára nem lehet 0-nál kisebb, vagy 100000 Ft-nál nagyobb.")
        else:
            self.menu.append(etel)
            print(f"{etel.nev} hozzáadva a(z) {self.nev} étterem menüjéhez.")

# Példa használat
etterem = Etterem("Vidám Kifőzde")

while True:
    nev = input("Kérem, adja meg az étel nevét: ")
    ar = int(input("Kérem, adja meg az étel árát: "))

    uj_etel = Etel(nev, ar)
    etterem + uj_etel

    valasz = input("Szeretne még hozzáadni ételt? (igen/nem): ")
    if valasz.lower() != "igen":
        break

# Menü kiírása
print(etterem.get_menu_items())