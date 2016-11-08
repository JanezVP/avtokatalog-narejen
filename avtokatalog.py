class vozni_park (object):
    def __init__(self, znamka, model, stevilo_kilometrov, servis):
        self.znamka = znamka
        self.model = model
        self.stevilo_kilometrov = stevilo_kilometrov
        self.servis = servis

    def izpisi_katalog(self):
        return (self.znamka  + ", " + self.model  + ", " "prevozenih: " + self.stevilo_kilometrov  + " km" + ", " + "zadnji servis: " + self.servis)


avtokatalog = []

def dodaj_vozilo():
    znamka = raw_input("znamka ")
    model = raw_input("model ")
    stevilo_kilometrov = raw_input("kilometri ")
    servis = raw_input("servis ")

    katalog = vozni_park(znamka, model, stevilo_kilometrov, servis)

    avtokatalog.append(katalog)

def izberi_avto():
    izpisi_avtomobile()
    num = int(raw_input("Vpisi zaporedno stevilko avtomobila"))
    if not (0 <= num < len(avtokatalog)):
        print ("Taksnega avtomobila ni v katalogu.")
        return -1
    return num

def izbrisi_avtomobil():
    num = izberi_avto()
    if num == -1:
        return
    print ("Brisem avtomobil iz seznama")
    bliznjica = False
    if bliznjica:
        izbrisani = avtokatalog.pop(num)
    else:
        izbrisani = avtokatalog[num]
        del avtokatalog[num]

    print ("Izbrisal: " + izbrisani.izpisi_katalog())

def uredi_vozilo():
    num = izberi_avto()
    if num == -1:
        return
    print ("Urejanje avtomobila: " + avtokatalog[num].izpisi_katalog())
    znamka = raw_input("znamka ")
    model = raw_input("model ")
    stevilo_kilometrov = raw_input("kilometri ")
    servis = raw_input("servis ")

    katalog = vozni_park(znamka, model, stevilo_kilometrov, servis)

    avtokatalog[num] = katalog

def izpisi_avtomobile():
    print ("St \t| Avtomobil")
    print ("-"*50)
    for j in range(len(avtokatalog)):
        print(str(j) + "\t| " + avtokatalog[j].izpisi_katalog())

while True:
    odgovor = raw_input("Povej kaj zelis narediti (dodaj, izbrisi, uredi, izpisi, koncaj)? ").lower()
    if odgovor == "dodaj":
        dodaj_vozilo()
    elif odgovor == "uredi":
        uredi_vozilo()
    elif odgovor == "izbrisi":
        izbrisi_avtomobil()
    elif odgovor == "izpisi":
        izpisi_avtomobile()
    elif odgovor == "koncaj":
        break
    else:
        print("Nisem razumel odgovora: ")
