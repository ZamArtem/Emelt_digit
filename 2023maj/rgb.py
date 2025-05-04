


with open("kep.txt")as f:
    adatok = [sor.strip().split(" ") for sor in[sor for sor in f]]
    


print("2. feladat:")
print("Kérem egy képpont adatait!")
beker_sor   = int(input("Sor:"))-1
beker_osz   = int(input("Oszlop:"))-1
rgb = adatok[beker_sor]

tarolo = []
lista = []
for i in rgb:
    tarolo.append(i)
    if len(tarolo) < 3:
        pass
    else:
        lista.append(tarolo)
        tarolo = []

print(f"A képpont színe RGB({lista[beker_osz][0]},{lista[beker_osz][1]},{lista[beker_osz][2]})")

print("3. feladat:")
tarolo = []
rgbk = []
for sor in adatok:
    for i in sor:
        tarolo.append(i)
        if len(tarolo) < 3:
            pass
        else:
            rgbk.append(tarolo)
            tarolo = []

print(f"A világos képpontok száma: {len([sor for sor in rgbk if int(sor[0])+int(sor[1])+int(sor[2]) > 600])}")
print("4. feladat:")

kicsi = 255 + 255 + 255
for sor in rgbk:
    if int(sor[0])+int(sor[1])+int(sor[2]) < kicsi:
        kicsi = int(sor[0])+int(sor[1])+int(sor[2])
print(f"A legsötétebb pont RGB összege:{kicsi}")
print("A legsötétebb pixelek színe:")

for sor in rgbk:
    if int(sor[0])+int(sor[1])+int(sor[2]) == kicsi:
        print(f"RGB({sor[0]},{sor[1]},{sor[2]})")

def hatar(besor,elter):
    besor     = int(besor)-1
    elter   = int(elter)
    rgb = adatok[besor]
    switch = False
    tarolo = []
    lista = []
    for i in rgb:
        tarolo.append(i)
        if len(tarolo) < 3:
            pass
        else:
            lista.append(tarolo)
            tarolo = []
    for index in range(len(lista)-1):
        if int(lista[index][2]) > int(lista[index+1][2]):
            diff = int(lista[index][2]) - int(lista[index+1][2])
            if diff > elter:
                switch = True
        if int(lista[index][2]) < int(lista[index+1][2]):
            diff = int(lista[index+1][2]) - int(lista[index][2])
            if diff > elter:
                switch = True

    return switch

print("6. feladat:")

elso = -10
utolso = -10
print()


for i in range(len(adatok)):
    if elso == -10 and hatar(i,10) == True:
        elso = i
    if hatar(i,10) == True:
        utolso = i
print(f"A felhő legfelső sora: {elso}")
print(f"A felhő legalsó sora: {utolso}")