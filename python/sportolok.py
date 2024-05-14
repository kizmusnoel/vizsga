class Sportolo:
    def __init__(self, line) -> None:
        splitted = line.strip().split(";")
        self.nev = splitted[0]
        self.ev = int(splitted[1])
        self.sportag = splitted[2]
        self.arany = int(splitted[3])
sportolok = []
def main():
    readFile("sportolok.txt")
    print(f"1. feladat: Összesen {len(sportolok)} sportoló szerepel az adatbázisban.")
    a = input("2. feladat: Korkülönbség\n\tElső sportoló: ")
    b = input("\tMásodik sportoló: ")
    print(f"\n\t{a} és {b} közti korkülönbség: {korkulonbseg(a, b)} év")
    print("3. feladat: Aranyérmek")
    for k, v in aranyermek():
        print(f"\t{k}: {v}")
    evszam = int(input("4. feladat: Évszám: "))
    utansz = utanszuletett(evszam)
    for u in utansz:
        print(f"\t{u.nev}")
    print(f"5. feladat: {evszam} után születettek aranyérmeinek összege: {utanszOsszeg(utansz)}")

def readFile(filename):
    f = open(filename, "r", encoding="utf-8")
    for line in f:
        sportolok.append(Sportolo(line))
    f.close()

def korkulonbseg(a, b):
    for s in sportolok:
        if s.nev == a:
            a = s.ev
        if s.nev == b:
            b = s.ev
    return abs(a-b)

def aranyermek():
    dictionary = {}
    for s in sportolok:
        if s.sportag not in dictionary:
            dictionary[s.sportag] = s.arany
        else:
            dictionary[s.sportag] += s.arany
    return dictionary.items()

def utanszuletett(evszam):
    lista = []
    for s in sportolok:
        if s.ev >= evszam:
            lista.append(s)
    return lista

def utanszOsszeg(utansz):
    count = 0
    for u in utansz:
        count += u.arany
    return count
main()