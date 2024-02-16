noms=[]
edad=[]
while True:
    n=str(input("nom alumne "))
    e=int(input("edad alumne "))
    noms.append(n)
    edad.append(e)
    mitjana=sum(edad)/len(edad)
    print(f"la edad mitjana del almnes es {mitjana} anys")
    if n=="*":
        print("finalitzant programa ")
        break
