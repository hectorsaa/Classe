import time

clients_compra=['paper corporation','WestRock','UPM']
clients_venta=['corte ingles','La Sol papereria','Amazon']
zonas=['A','B','C']

codi=int(input("introdueix el teu codi "))

A2=50
A3=50
A4=50
A5=50
A6=50

diners=1000


if codi== 101 or codi== 102:
    print("""Benvingut comprador!! 
    Carregant programa...""")
    time.sleep(3)
    while True:
        opcio=int(input("""Que vol fer?
                        1-Consultar diners de la empresa
                        2-Comprar 
                        3-Consultar clients
                        4-Tancar programa
                        """))
        if opcio==1:
            print(f"La empresa té {diners}€")
            break
        
        elif opcio==2:
            if diners<=100:
                print("No hi han suficients diners a la empresa")
                break
            
            else:
                while True:
                    opcio_papers=str(input("Quin tipues de paper vols comprar (A2, A3, A4, A5, A6) x-tornar a la pàgina anterior: " ))
                
                    if opcio_papers=="A2":
                        print("Un paquet de A2 de 500ut costa 18,95€")
                        unitats_paper=int(input("Quantitat de paquets que vols comprar: "))
                        preu=unitats_paper*18.95
                        confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu,2)} "))
                        
                        if confirmar_compra=="si":
                            print("Compra realitzada amb èxit")
                            diners=diners-preu
                            A2=A2+unitats_paper
                            break
                        elif confirmar_compra=="no":
                            print("Compra cancel·lada")
                            break

                    elif opcio_papers=="A3":
                        print("Un paquet de A3 de 500ut costa 11,34€")
                        unitats_paper=int(input("Quantitat de paquets que vols comprar: "))
                        preu=11.34
                        preu_caixa=58.45
                        caixa=unitats_paper//5                        
                        caixa1=caixa*preu_caixa
                        preu_individual=(unitats_paper-(caixa*5))*preu
                        preu_total=preu_individual+caixa1
                        
                        confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu_total,2)} "))
                        
                        if confirmar_compra=="si":
                            print("Compra realitzada amb èxit")
                            diners=diners-preu_total
                            A3=A3+unitats_paper
                            print(A3)
                            print(diners)
                            break

                        elif confirmar_compra=="no":
                            print("Compra cancel·lada")
                            break
                    
                    elif opcio_papers=="A4":
                        print("Un paquet de A4 de 500ut costa 7,98€")
                        unitats_paper=int(input("Quantitat de paquets que vols comprar: "))
                        preu=unitats_paper*7.98
                        confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu,2)} "))
                        
                        if confirmar_compra=="si":
                            print("Compra realitzada amb èxit")
                            diners=diners-preu
                            A4=A4+unitats_paper
                            break
                        elif confirmar_compra=="no":
                            print("Compra cancel·lada")
                            break
                
                    elif opcio_papers=="A5":
                        print("Un paquet de A5 de 500ut costa 7,13€")
                        unitats_paper=int(input("Quantitat de paquets que vols comprar: "))
                        preu=unitats_paper*7.13
                        confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu,2)} "))
                        
                        if confirmar_compra=="si":
                            print("Compra realitzada amb èxit")
                            diners=diners-preu
                            A5=A5+unitats_paper
                            break
                        elif confirmar_compra=="no":
                            print("Compra cancel·lada")
                            break
                    elif opcio_papers=="A6":
                        print("Un paquet de A6 de 500ut costa 6,45€")
                        unitats_paper=int(input("Quantitat de paquets que vols comprar: "))
                        preu=unitats_paper*6,45
                        confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu,2)} "))
                        if confirmar_compra=="si":
                            print("Compra realitzada amb èxit")
                            diners=diners-preu
                            A6=A6+unitats_paper                          
                            break
                        elif confirmar_compra=="no":
                            print("Compra cancel·lada")
                            break

                    elif opcio_papers=="x":
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
                    time.sleep(3)
                    break
            
        elif opcio==4:
            print("Tancant programa ...")
            time.sleep(4)
            break
    

elif codi== 103 or codi==104 or codi==105:
    print("""Benvingut venedor!! 
    Carregant programa...""")
    time.sleep(3)  
    while True:
        opcio=int(input("""Que vol fer?
                        1-Consultar paquets de paper en el magatzem 
                        2-Vendre 
                        3-Consultar clients
                        4-Paper venut
                        5-Volum vendas
                        6-Tancar programa
                        """))
        if opcio==1:
            print(f"La empresa té {diners}€")
            break
        
        elif opcio==2:
            while True:
                opcio_papers=str(input("Quin tipues de papeers vols vendre (A2, A3, A4, A5, A6)   x-Tornar a la pàgina anterior " ))
                
                if opcio_papers=="A2":
                    if A2<=10:
                        print("No hi ha suficient estoc")
                        break
                    else:
                        quantitat_vendre=int(input("Quantitat de paquets de A2 que vols vendre: "))
                        benefici=quantitat_vendre*24.15
                        confirmar_venda=str(input("Confirma la venda (si/no): "))
                        if confirmar_venda=="si":
                            print("Venda realitzada amb èxit")
                            diners=diners+benefici
                            A2=A2-quantitat_vendre
                            break
                        elif confirmar_venda=="no":
                            print("Venda cancel·lada")
        elif opcio==3:
            while True:
                opcio_clients=int(input("""Que vols fer:
                                        1-Veure clients
                                        2-Afegir clients
                                        3-Eliminar clients 
                                        4-Tornar """))
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
            
        elif opcio==6:
            print("Tancant programa ...")
            time.slepp(4)
            break

else:
    print("Codi incorrecte. Torna a provar")