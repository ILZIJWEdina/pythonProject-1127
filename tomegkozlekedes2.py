from datetime import datetime, timedelta
from jarmu import Jarmu
from megallo import Megallo
from utas import Utas
from utazas import Utazas

busz = Jarmu("B001", "Busz", "08:00-18:00")
megallo = Megallo("Kossuth tér")
utas = Utas("Alice", "napijegy")
utazas = Utazas(utas, busz, datetime.now(), datetime.now() + timedelta(hours=1))

busz.indulas()
megallo.hozzaad_jarmu(busz)
print(f"{utas.nev} utazik a(z) {utazas.jarmu.tipus}-on.")
