import datetime as dt
class Adatok(object):
    def __init__(self,sor):
        split =sor.split(';')
        self.taxi_id=int(split[0])
        self.indulas=dt.datetime.strptime(split[1],"%Y-%m-%d %H:%M:%S")
        self.idotartam=int(split[2])
        self.tavolsag=float(split[3].replace(",",'.'))
        self.viteldij=float(split[4].replace(",",'.'))
        self.borravalo=float(split[5].replace(",",'.'))
        self.fizetes_modja=split[6]
with open("fuvar.csv","r", encoding="utf-8") as Beolvasas:
    fejlec = Beolvasas.readline().strip()
    lista=[Adatok(x.strip()) for x in Beolvasas]

print(f"3. feladat: {len(lista)} fuvar")
fuvarszam = [x.viteldij for x in lista if x.taxi_id==6185]
print(f"4. feladat: {len(fuvarszam)} fuvar alatt: {str(sum(fuvarszam)).replace('.',',')}$")
print("5. feladat:")
fizetes = {x.fizetes_modja for x in lista}
for x in fizetes:
    szam = sum(1 for y in lista if x==y.fizetes_modja)
    print(f"\t{x}: {szam} fuvar ")
print("6. feladat: %.2f km" %sum(x.tavolsag*1.6 for x in lista))
print("7. feladat: Leghosszabb fuvar")
leghosszabb = max(x.idotartam for x in lista)
for x in lista:
    if x.idotartam == leghosszabb:
        print(
        f"""\tFuvar hossza: {x.idotartam} másodperc
        Taxi azonosító: {x.taxi_id}
        Megtett távolsűg: {x.tavolsag}km
        Viteldíj: {x.viteldij}$""")
print("8. feladat: hibak.txt")
with open("hibak.txt","w", encoding="utf-8") as kiiras:
    kiiras.write(f"{fejlec}\n")
    [kiiras.write(f"{x.taxi_id};{x.indulas};{x.idotartam};{x.tavolsag};{x.viteldij};{x.borravalo};{x.fizetes_modja}\n") 
     for x in sorted(lista, key=lambda y: y.indulas) if x.idotartam>0 and x.viteldij>0 and x.tavolsag==0]