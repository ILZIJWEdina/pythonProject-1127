class Jegyszamolo:
    def __init__(self, teszteredmeny, fejlesztesi_feladat):
        self.teszteredmeny = teszteredmeny
        self.fejlesztesi_feladat = fejlesztesi_feladat

    def szamol_erdemjegyet(self):
        osszpont = self.teszteredmeny + self.fejlesztesi_feladat

        if osszpont >= 90:
            return "Jeles (5)"
        elif osszpont >= 80:
            return "Jó (4)"
        elif osszpont >= 70:
            return "Közepes (3)"
        elif osszpont >= 60:
            return "Elégséges (2)"
        else:
            return "Elégtelen (1)"

# Felhasználótól bekérjük a teszteredmenyt
teszteredmeny = int(input("Kérem, adja meg a teszteredményt: "))
fejlesztesi_feladat = int(input("Kérem, adja meg a fejlesztési feladat eredményét: "))

# Példa használat
jegyszamolo = Jegyszamolo(teszteredmeny, fejlesztesi_feladat)
erdemjegy = jegyszamolo.szamol_erdemjegyet()

print(f"Az érdemjegy: {erdemjegy}")