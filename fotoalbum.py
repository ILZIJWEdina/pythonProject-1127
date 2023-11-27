class Felhasznalo:
    def __init__(self, felhasznalonev, jelszo):
        self._felhasznalonev = felhasznalonev
        self._jelszo = jelszo

    def ellenoriz_jelszo(self, jelszo):
        return self._jelszo == jelszo

class Kep:
    def __init__(self, nev, meret, formatum, tulajdonos):
        self._nev = nev
        self._meret = meret
        self._formatum = formatum
        self._tulajdonos = tulajdonos

    @property
    def meret(self):
        return self._meret

    @property
    def formatum(self):
        return self._formatum

    @property
    def nev(self):
        return self._nev

    @meret.setter
    def meret(self, uj_meret):
        if self._tulajdonos:
            self._meret = uj_meret
        else:
            print("Nincs engedélye a méret módosítására.")

    @formatum.setter
    def formatum(self, uj_formatum):
        if self._tulajdonos:
            self._formatum = uj_formatum
        else:
            print("Nincs engedélye a formátum módosítására.")

class Album:
    def __init__(self, nev, tulajdonos):
        self._nev = nev
        self._tulajdonos = tulajdonos
        self._kepek = []

    def kep_hozzaad(self, kep):
        if kep.nev not in [k.nev for k in self._kepek]:
            self._kepek.append(kep)
            print(f"{kep.nev} hozzáadva az albumhoz.")
        else:
            print("Ez a kép már szerepel az albumon.")

    def kep_kivesz(self, kep):
        if kep in self._kepek:
            self._kepek.remove(kep)
            print(f"{kep.nev} eltávolítva az albumból.")
        else:
            print("A kép nem található az albumon.")

    def get_kepek(self):
        return [k.nev for k in self._kepek]

# Példa használat
felhasznalo = Felhasznalo("user1", "password")

kep1 = Kep("Nature", "5MB", "JPEG", felhasznalo)
kep2 = Kep("Beach", "3MB", "PNG", felhasznalo)

album = Album("Holiday", felhasznalo)

album.kep_hozzaad(kep1)
album.kep_hozzaad(kep2)

print(f"Album képei: {album.get_kepek()}")

kep1.meret = "8MB"  # Méret módosítása, mivel a felhasználó a kép tulajdonosa

kep3 = Kep("Sunset", "6MB", "JPEG", None)
album.kep_hozzaad(kep3)  # Hozzáadás kísérlete, de nem sikerül, mert nincs tulajdonosa

album.kep_kivesz(kep2)

print(f"Album képei a változtatások után: {album.get_kepek()}")