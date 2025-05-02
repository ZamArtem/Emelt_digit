class Met:
    def __init__(self,sor):
        telepules, ido, szel_ero, fok = sor.strip().split(" ")
        self.telepules  = telepules
        self.ido        = ido
        self.ido_int    = int(self.ido)
        self.szel_ero   = szel_ero
        self.fok        = int(fok)
        self.ora_perc   = self.ido[:2]+":"+self.ido[2:]
        self.ora        = self.ido[:2]
        self.perc       = self.ido[2:]
        self.szel       = self.szel_ero[:3]
        self.ero        = int(self.szel_ero[3:])

with open("tavirathu13.txt")as f:
    adatok = [Met(sor) for sor in f]



print("2. feladat")
beker = input("Adja meg egy település kódját! Település: ")
print(f"Az utolsó mérési adat a megadott településről {str(max([sor.ido_int for sor in adatok if sor.telepules == beker]))[:2]}:{str(max([sor.ido_int for sor in adatok if sor.telepules == beker]))[2:]}-kor érkezett.")
print("3. feladat")
for sor in adatok:
    if sor.fok == min([sor.fok for sor in adatok]):
        kicsi = [sor.telepules," ",sor.ora,":",sor.perc," ",sor.fok," fok"]
        break 
print(f"A legalacsonyabb hőmérséklet: ",end="")
for sor in kicsi:       
    print(sor,end="")
print()

for sor in adatok:
    if sor.fok == max([sor.fok for sor in adatok]):
        kicsi = [sor.telepules," ",sor.ora,":",sor.perc," ",sor.fok," fok"]
        break 
print(f"A legmagasabb hőmérséklet: ",end="")
for sor in kicsi:       
    print(sor,end="")
print()

print("4. feladat")
szelcsend = [sor for sor in adatok if sor.szel_ero == "00000"]
if len(szelcsend) > 0:
    for sor in szelcsend:
        print(sor.telepules,sor.ora+":"+sor.perc)
else:
    print("Nem volt szélcsend a mérések idején.")

print("5. feladat")

varosok = []
for sor in adatok:
    if sor.telepules not in varosok:
        varosok.append(sor.telepules)
#1., 7., 13., 19.
fokok = []
egy,het,tizharom,tizkilenc = False,False,False,False

for i in range(len(varosok)):
    for sor in adatok:
        if sor.telepules == varosok[i]:
            if int(sor.ora) == 1:
                fokok.append(sor.fok)
                egy = True
            if int(sor.ora) == 7:
                fokok.append(sor.fok)
                het = True
            if int(sor.ora) == 13:
                fokok.append(sor.fok)
                tizharom = True
            if int(sor.ora) == 19:
                fokok.append(sor.fok)
                tizkilenc = True
            
    if egy == True and het == True and tizharom == True and tizkilenc == True:
        print(f"{varosok[i]} Középhőmérséklet: {round(sum(fokok)/len(fokok))}; Hőmérséklet-ingadozás: {max([sor.fok for sor in adatok if sor.telepules == varosok[i]])-min([sor.fok for sor in adatok if sor.telepules == varosok[i]])}")
    else:
        print(f"{varosok[i]} NA; Hőmérséklet-ingadozás: {max([sor.fok for sor in adatok if sor.telepules == varosok[i]])-min([sor.fok for sor in adatok if sor.telepules == varosok[i]])}")
    egy,het,tizharom,tizkilenc = False,False,False,False    
    fokok = []

print("6. feladat")
for i in range(len(varosok)):
    with open(f"{varosok[i]}","w")as w:
        w.write(varosok[i]+"\n")
        for sor in adatok:
            if sor.telepules == varosok[i]:
                w.write(sor.ora+":"+sor.perc+" "+("#"*sor.ero)+"\n")
print("A fájlok elkészültek.")