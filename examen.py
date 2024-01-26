noms=[]
kms_dilluns=[]
kms_dimarts=[]
dias=["dilluns","dimarts","dimecres","dijous","divendres","disapte","diumenga"]
total_km_dilluns=[]
total_km_dimarts=[]
mit_dia=[]

while True:

    nom_conductor=str(input("Nom del conductor que vols afegir: "))
    noms.append(nom_conductor)
    print(noms)

    kilometres_dilluns=int(input("Cuants kilometres ha fet el conductor el dilluns: "))
    kms_dilluns.append(kilometres_dilluns)
    print(kms_dilluns)
    
    kilometres_dimarts=int(input("Cuants kilometres ha fet el conductor el dimarts: "))
    kms_dimarts.append(kilometres_dimarts)
    print(kms_dimarts)
    
    print("la suma de tots els kilomestres del dilluns es:",sum(kms_dilluns))
    print("la suma de tots els kilomestres del dimarts es:",sum(kms_dimarts))
   
    