class Szoba:
    def __init__(self, szobaszam, foglalt=False):
        self.szobaszam = szobaszam
        self.foglalt = foglalt

    def __str__(self):
        return f"Szoba {self.szobaszam} - {'Foglalt' if self.foglalt else 'Szabad'}"


class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, foglalt=False, ar=10000, extras=[]):
        super().__init__(szobaszam, foglalt)
        self.ar = ar
        self.extras = extras


class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, foglalt=False, ar=15000, extras=[]):
        super().__init__(szobaszam, foglalt)
        self.ar = ar
        self.extras = extras


class Lakosztaly(Szoba):
    def __init__(self, szobaszam, foglalt=False, ar=25000, extras=[]):
        super().__init__(szobaszam, foglalt)
        self.ar = ar
        self.extras = extras


class Foglalas:
    def __init__(self, szoba, nev, kezdet, veg):
        self.szoba = szoba
        self.nev = nev
        self.kezdet = kezdet
        self.veg = veg

    def __str__(self):
        return f"{self.nev} foglalása a(z) {self.szoba.szobaszam}. szobában, {self.kezdet} - {self.veg}"

class Szalloda:
    def __init__(self):
        self.szobak = {}

    def adatfeltolto(self):
        egyagyas1 = EgyagyasSzoba(101, False, 12000, ["Wifi", "Reggeli"])
        egyagyas2 = EgyagyasSzoba(102, False, 10000, ["Wifi"])
        ketagyas1 = KetagyasSzoba(201, False, 18000, ["Wifi", "Reggeli", "TV"])
        ketagyas2 = KetagyasSzoba(202, False, 16000, ["Wifi", "TV"])
        lakosztaly1 = Lakosztaly(301, False, 30000, ["Wifi", "Reggeli", "TV", "Mini bár"])
        lakosztaly2 = Lakosztaly(302, False, 28000, ["Wifi", "TV", "Mini bár"])

        self.szobak = {
            101: egyagyas1,
            102: egyagyas2,
            201: ketagyas1,
            202: ketagyas2,
            301: lakosztaly1,
            302: lakosztaly2
        }

    def kiir_arak(self):
        for szobaszam, szoba in self.szobak.items():
            print(f"{szoba} - Ár: {szoba.ar} Ft/éjszaka")

    def foglalas_leadasa(self, szobaszam, nev, kezdet, veg):
        szoba = self.szobak.get(szobaszam)
        if szoba:
            if not szoba.foglalt:
                foglalas = Foglalas(szoba, nev, kezdet, veg)
                szoba.foglalt = True
                print(f"Foglalás elfogadva: {foglalas}")
            else:
                print("A szoba már foglalt.")
        else:
            print("Érvénytelen szobaszám.")

# Példa használat
szalloda = Szalloda()
szalloda.adatfeltolto()

while True:
    print("\n1. Árak megtekintése")
    print("2. Foglalás leadása")
    print("3. Kilépés")
    valasztas = input("Válasszon egy opciót (1/2/3): ")

    if valasztas == "1":
        szalloda.kiir_arak()
    elif valasztas == "2":
        szobaszam = int(input("Adja meg a szobaszámot: "))
        nev = input("Adja meg a nevét: ")
        kezdet = input("Adja meg a foglalás kezdetét (YYYY-MM-DD): ")
        veg = input("Adja meg a foglalás végét (YYYY-MM-DD): ")
        szalloda.foglalas_leadasa(szobaszam, nev, kezdet, veg)
    elif valasztas == "3":
        break
    else:
        print("Érvénytelen választás. Kérem, válasszon újra.")

