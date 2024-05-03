class Sportolo:
    def __init__(self, line) -> None:
        splitted = line.strip().split(";")
        self.nev = splitted[0]
        self.ev = splitted[1]
        self.sportag = splitted[2]
        self.arany = splitted[3]
sportolok = []
def main():
    readFile("sportolok.txt")

def readFile(filename):
    f = open(filename, "r", encoding="utf-8")
    for line in f:
        sportolok.append(Sportolo(line))
    f.close()
main()