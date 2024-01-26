import time

tipo_papel=['A2','A3','A4','A5','A6']
clients_compra=['paper corporation','WestRock','UPM']
clients_venta=['corte ingles','La Sol papereria','Amazon']
zonas=['A','B','C']
preu_venda=['24.15','12.25','9,45','8.1','7,35']
preu_compra=['18.95','11.34','7.98','7,13','6,40']

contrasenya=int(input("introdueix el teu codi "))

A2=50
A3=50
A4=50
A5=50
A6=50

diners=1000


if contrasenya== 101 or contrasenya== 102:
    print("""Benvingut comprador!! 
    Carregant programa...""")
    time.sleep(3)
    while True:
        opcio=int(input("""Que vol fer?
                        1-consultar diners de la empresa
                        2-comprar 
                        3-consultar clients
                        4-tancar programa
                        """))
        if opcio==1:
            print(f"La empresa té {diners}€")
            break
        
        elif opcio==2:
            while True:
                opcio_papers=str(input("Quin tipues de paper vols comprar (A2, A3, A4, A5, A6) x-tornar a la pàgina anterior: " ))
                
                if opcio_papers=="A2":
                    if diners<=100:
                        print("No hi han suficients diners a la empresa") 
                        break
                    else:
                        print("Un paquet de 500ut de A2 costa 18,95€")
                        unitats_paper=int(input("Quantitat de paquets que vols comprar: "))
                        preu=unitats_paper*18.95
                        confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {preu.}"))
                        
                        
                        if confirmar_compra=="si":
                            print("Compra realitzada amb èxit")
                            diners=diners-preu
                            A2=A2-unitats_paper
                            break
                        elif confirmar_compra=="no":
                            print("Compra cancelada")
                            break


                if opcio_papers=="A3":
                    if diners<=100:
                        print("No hi ha suficien diners a la empresa")

                if opcio_papers=="x":
                    print("Tornant a l'inici")
                    time.sleep(3)
                    break
        
        elif opcio ==3:
            while True:
                opcio_clients=int(input("""Que vols fer:
                                        1-veure clients
                                        2-afegir clients
                                        3-eliminar clients 
                                        4-tornar 
                                        """))
                if opcio_clients==1:
                    print(f"Els clients són{clients_compra}" )
                
                if opcio_clients==2:
                    afegir_client=str(input("Nom del client que vols afegir: "))
                    clients_compra.append(afegir_client)
                    print(f"Els clients són{clients_compra}" )
                
                if opcio_clients==3:
                    eliminar_client=str(input("Nom del client que vols eliminar: "))
                    clients_compra.remove(eliminar_client)
                    print(f"Els clients són{clients_compra}" )
                if opcio_clients==4:
                    print("Tornant a la pàgina anterior")
                    time.slepp(3)
                    break
            
        elif opcio==4:
            print("tancant programa ...")
            time.slepp(4)
            break
    

elif contrasenya== 103 or contrasenya==104 or contrasenya==105:
    print("""Benvingut venedor!! 
    Carregant programa...""")
    time.sleep(3)  
    while True:
        opcio=int(input("""Que vol fer?
                        1-consultar paquets de paper en el magatzem 
                        2-vendre 
                        3-consultar clients
                        4-peper venut
                        5-volum vendas
                        6-tancar programa
                        """))
        if opcio==1:
            print(f"La empresa té {diners}€")
            break
        
        elif opcio==2:
            while True:
                opcio_papers=str(input("Quin tipues de papeers vols vendre (A2, A3, A4, A5, A6) " ))
                
                    
        
        
        
        if opcio==3:
            while True:
                opcio_clients=int(input("""Que vols fer:
                                        1-veure clients
                                        2-afegir clients
                                        3-eliminar clients 
                                        4-tornar """))
                if opcio_clients==1:
                    print(f"Els clients són{clients_venta}" )
                
                elif opcio_clients==2:
                    afegir_client=str(input("Nom del client que vols afegir: "))
                    clients_venta.append(afegir_client)
                    print(f"Els clients són{clients_venta}" )
                
                elif opcio_clients==3:
                    eliminar_client=str(input("Nom del client que vols eliminar: "))
                    clients_venta.remove(eliminar_client)
                    print(f"Els clients són{clients_venta}" )
                elif opcio==4:
                    print("Tornant a la pàgina anterior")
                    time.sleep(3)
                    break
            
        if opcio==6:
            print("tancant programa ...")
            time.slepp(4)

else:
    print("codi incorrecte. Torna a provar")