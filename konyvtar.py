from datetime import datetime, timedelta

class Konyv:
    def __init__(self, szerzo, cim, kiadas_eve, isbn):
        self.szerzo = szerzo
        self.cim = cim
        self.kiadas_eve = kiadas_eve
        self.isbn = isbn
        self.kolcsonzesek = []

    def konyv_informacio(self):
        return f"{self.szerzo} - {self.cim} ({self.kiadas_eve}), ISBN: {self.isbn}"

class Tag:
    def __init__(self, nev, tagazonosito, email):
        self.nev = nev
        self.tagazonosito = tagazonosito
        self.email = email
        self.kolcsonzott_konyvek = []

    def tag_informacio(self):
        return f"{self.nev} (Tagazonosító: {self.tagazonosito}, Email: {self.email})"

class Kolcsonzes:
    def __init__(self, tag, konyv, kolcsonzes_datuma):
        self.tag = tag
        self.konyv = konyv
        self.kolcsonzes_datuma = kolcsonzes_datuma
        self.visszavetel_datuma = None

    def visszavetel(self):
        self.visszavetel_datuma = datetime.now()

    def kolcsonzes_informacio(self):
        return f"{self.tag.tag_informacio()} kölcsönözte ki: {self.konyv.konyv_informacio()}, Kölcsönzés dátuma: {self.kolcsonzes_datuma}, Visszavétel dátuma: {self.visszavetel_datuma}" if self.visszavetel_datuma else f"{self.tag.tag_informacio()} kölcsönözte ki: {self.konyv.konyv_informacio()}, Kölcsönzés dátuma: {self.kolcsonzes_datuma}"

# Példa használat
konyv1 = Konyv("J.K. Rowling", "Harry Potter és a bölcsek köve", 1997, "978-963-642-097-7")
konyv2 = Konyv("J.R.R. Tolkien", "A Gyűrűk Ura", 1954, "978-963-253-529-4")

tag1 = Tag("John Doe", "123456", "john.doe@example.com")
tag2 = Tag("Jane Doe", "654321", "jane.doe@example.com")

kolcsonzes1 = Kolcsonzes(tag1, konyv1, datetime.now() - timedelta(days=7))
kolcsonzes2 = Kolcsonzes(tag2, konyv2, datetime.now() - timedelta(days=14))

kolcsonzes1.visszavetel()
kolcsonzes2.visszavetel()

print(kolcsonzes1.kolcsonzes_informacio())
print(kolcsonzes2.kolcsonzes_informacio())