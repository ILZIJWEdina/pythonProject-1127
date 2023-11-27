class Megallo:
    def __init__(self, nev):
        self.nev = nev
        self.jarmuvek = []

    def hozzaad_jarmu(self, jarmu):
        self.jarmuvek.append(jarmu)
        print(f"{jarmu.tipus} ({jarmu.rendszam}) hozzáadva a {self.nev} megállóhoz.")

        