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

# Ételek létrehozása
porkolt = Etel("Pörkölt", 2500)
gulyas = Etel("Gulyásleves", 1800)

# Menüelemek hozzáadása
etterem.hozzaad_menu_elem(porkolt)
etterem.hozzaad_menu_elem(gulyas)

# Menü kiírása
print(etterem.get_menu_items())

# Új étel hozzáadása az étterem menüjéhez
uj_etel = Etel("Rántott hús", 3200)
etterem + uj_etel

# Új menü kiírása
print(etterem.get_menu_items())