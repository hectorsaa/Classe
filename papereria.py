import time

clients_compra=['paper corporation','WestRock','UPM']
clients_venta=['El Corte Ingles','La Sol papereria','Amazon']
volum_vendas=[]
paper_venutA2=[]
paper_venutA3=[]
paper_venutA4=[]
paper_venutA5=[]
paper_venutA6=[]

usuari=str(input("Introdueix nom d'usuari: "))
codi=int(input("Introdueix el teu codi: "))

A2=50
A3=50
A4=50
A5=50
A6=50
diners=1000

if codi== 101 and usuari=="Stanley Hudson" or codi== 102 and usuari=="Angela Martin":
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
            time.sleep(3)
            print(f"La empresa té {diners}€")
            
        
        elif opcio==2:
            time.sleep(3)          
            if diners<=100:
                print("No hi han suficients diners a la empresa")
            
            else:
                while True:
                    opcio_papers=str(input("Quin tipues de paper vols comprar (A2, A3, A4, A5, A6) x-tornar a la pàgina anterior: " ))
                    time.sleep(3)
                    if opcio_papers=="A2":
                        print("Un paquet de A2 de 500ut costa 18,95€")
                        unitats_paper=int(input("Quantitat de paquets que vols comprar: "))
                        descompte=unitats_paper//4
                        descompte1=(7*descompte)/100
                        preunodescompte=(unitats_paper-(descompte*4))*18.95
                        preu_total=preunodescompte+descompte1
                        if A2+unitats_paper<100:
                            confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu_total,2)}€ "))
                            if confirmar_compra=="si":
                                print("Compra realitzada amb èxit")
                                diners=diners-preu_total
                                A2=A2+unitats_paper
                            elif confirmar_compra=="no":
                                print("Compra cancel·lada")
                        else:
                            print("Estàs superant el màxim de stock del magatzem")
                            

                    elif opcio_papers=="A3":
                        print("Un paquet de A3 de 500ut costa 11,34€")
                        unitats_paper=int(input("Quantitat de paquets que vols comprar: "))
                        preu=7.98
                        preu_caixa=37,65
                        caixa=unitats_paper//5                        
                        caixa1=caixa*preu_caixa
                        preu_individual=(unitats_paper-(caixa*5))*preu
                        preu_total=(preu_individual*0.94)+(caixa1*0.97)
                        if A3+unitats_paper<150:                        
                            confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu_total,2)}€ "))                       
                            if confirmar_compra=="si":
                                print("Compra realitzada amb èxit")
                                diners=diners-preu_total
                                A3=A3+unitats_paper
                            elif confirmar_compra=="no":
                                print("Compra cancel·lada")
                        else:
                            print("Estàs superant el màxim de stock del magatzem")
                                              
                    elif opcio_papers=="A4":
                        print("Un paquet de A4 de 500ut costa 7,98€")
                        unitats_paper=int(input("Quantitat de paquets que vols comprar: "))
                        preu=11.34
                        preu_caixa=58.45
                        caixa=unitats_paper//5                        
                        caixa1=caixa*preu_caixa
                        preu_individual=(unitats_paper-(caixa*5))*preu
                        preu_total=(preu_individual*0.95)+(caixa1*0*98)
                        if A4+unitats_paper<400:                        
                            confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu_total,2)}€ "))
                            if confirmar_compra=="si":
                                print("Compra realitzada amb èxit")
                                diners=diners-preu_total
                                A4=A4+unitats_paper                           
                            elif confirmar_compra=="no":
                                print("Compra cancel·lada")
                        else:
                            print("Estàs superant el màxim de stock del magatzem")
                
                    elif opcio_papers=="A5":
                        print("Un paquet de A5 de 500ut costa 7,13€")
                        unitats_paper=int(input("Quantitat de paquets que vols comprar: "))
                        descompte=unitats_paper//4
                        descompte1=(4*descompte)/100
                        preunodescompte=(unitats_paper-(descompte*4))*7.13
                        preu_total=preunodescompte+descompte1
                        confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu_total,2)}€ "))
                        if A5+unitats_paper<150:                        
                            if confirmar_compra=="si":
                                print("Compra realitzada amb èxit")
                                diners=diners-preu_total
                                A5=A5+unitats_paper
                            elif confirmar_compra=="no":
                                print("Compra cancel·lada")
                        else:
                            print("Estàs superant el màxim de stock del magatzem")
        
                    elif opcio_papers=="A6":
                        print("Un paquet de A6 de 500ut costa 6,45€")
                        unitats_paper=int(input("Quantitat de paquets que vols comprar: "))
                        descompte=unitats_paper//4
                        descompte1=(3*descompte)/100
                        preunodescompte=(unitats_paper-(descompte*4))*6.45
                        preu_total=preunodescompte+descompte1
                        if A6+unitats_paper<300:                        
                            confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu_total,2)}€ "))
                            if confirmar_compra=="si":
                                print("Compra realitzada amb èxit")
                                diners=diners-preu_total
                                A6=A6+unitats_paper                          
                            elif confirmar_compra=="no":
                                print("Compra cancel·lada")
                        else:
                            print("Estàs superant el màxim de stock del magatzem")
                    elif opcio_papers=="x":
                        print("Tornant a l'inici")
                        time.sleep(3)
                        break
        
        elif opcio ==3:           
            time.sleep(3)
            while True:
                opcio_clients=int(input("""Que vols fer:
                                        1-veure clients
                                        2-afegir clients
                                        3-eliminar clients 
                                        4-tornar 
                                        """))
                time.sleep(3)                
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
            time.sleep(3)
            break
    

elif codi== 103 and usuari=="Dwight Schrute" or codi==104 and usuari=="Jim Halpert" or codi==105 and usuari=="Andy Bernard":
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
            print(f"La empresa té al magatzem {A2} paquets de A2")
            print(f"La empresa té al magatzem {A3} paquets de A3")
            print(f"La empresa té al magatzem {A4} paquets de A4")
            print(f"La empresa té al magatzem {A5} paquets de A5")
            print(f"La empresa té al magatzem {A6} paquets de A6")            
        
        elif opcio==2:
            while True:
                opcio_papers=str(input("Quin tipues de papeers vols vendre (A2, A3, A4, A5, A6)   x-Tornar a la pàgina anterior " ))
                time.sleep(2)
                
                if opcio_papers=="A2":
                    if A2<=20:
                        print("No hi ha suficient estoc")
                        
                    else:
                        quantitat_vendre=int(input("Quantitat de paquets de A2 que vols vendre: "))
                        descompte=quantitat_vendre//4
                        descompte1=(5*descompte)/100
                        preunodescompte=(quantitat_vendre-(descompte*4))*24.15
                        preu_total=preunodescompte+descompte1
                        
                        confirmar_venda=str(input("Confirma la venda (si/no): "))
                        if confirmar_venda=="si":
                            print("Venda realitzada amb èxit")
                            diners=diners+preu_total
                            A2=A2-quantitat_vendre
                            volum_vendas.append(preu_total)
                            paper_venutA2.append(quantitat_vendre)
                            break
                        elif confirmar_venda=="no":
                            print("Venda cancel·lada")

                if opcio_papers=="A3":
                        if A3<=30:
                            print("No hi ha suficient estoc")
                            
                        else:
                            quantitat_vendre=int(input("Quantitat de paquets de A3 que vols vendre: "))
                            preu=13.25
                            preu_caixa=63.95
                            caixa=quantitat_vendre//5                        
                            caixa1=caixa*preu_caixa
                            preu_individual=(quantitat_vendre-(caixa*5))*preu
                            preu_total=(preu_individual*0.96)+(caixa1*0.98)

                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=diners+preu_total
                                A3=A3-quantitat_vendre
                                volum_vendas.append(preu_total)
                                paper_venutA3.append(quantitat_vendre)

                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                            
                if opcio_papers=="A4":
                        if A3<=100:
                            print("No hi ha suficient estoc")
                            
                        else:
                            quantitat_vendre=int(input("Quantitat de paquets de A4 que vols vendre: "))
                            preu=9.45
                            preu_caixa=42.95
                            caixa=quantitat_vendre//5                        
                            caixa1=caixa*preu_caixa
                            preu_individual=(quantitat_vendre-(caixa*5))*preu
                            preu_total=(preu_individual*0.97)+(caixa1*0.99)                                        
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=diners+preu_total
                                A3=A3-quantitat_vendre
                                volum_vendas.append(preu_total)
                                paper_venutA4.append(quantitat_vendre)

                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                            
                if opcio_papers=="A5":
                    if A5<=50:
                        print("No hi ha suficient estoc")
                        
                    else:
                        quantitat_vendre=int(input("Quantitat de paquets de A5 que vols vendre: "))
                        descompte=quantitat_vendre//4
                        descompte1=(2*descompte)/100
                        preunodescompte=(quantitat_vendre-(descompte*4))*8.1
                        preu_total=preunodescompte+descompte1
                        confirmar_venda=str(input("Confirma la venda (si/no): "))
                        if confirmar_venda=="si":
                            print("Venda realitzada amb èxit")
                            diners=diners+preu_total
                            A5=A5-quantitat_vendre
                            volum_vendas.append(preu_total)
                            paper_venutA5.append(quantitat_vendre)
                        elif confirmar_venda=="no":
                            print("Venda cancel·lada")

                if opcio_papers=="A6":
                    if A6<=60:
                        print("No hi ha suficient estoc")
                        
                    else:
                        quantitat_vendre=int(input("Quantitat de paquets de A6 que vols vendre: "))
                        descompte=quantitat_vendre//4
                        descompte1=(1*descompte)/100
                        preunodescompte=(quantitat_vendre-(descompte*4))*7.35
                        preu_total=preunodescompte+descompte1
                        confirmar_venda=str(input("Confirma la venda (si/no): "))
                        if confirmar_venda=="si":
                            print("Venda realitzada amb èxit")
                            diners=diners+preu_total
                            A6=A6-quantitat_vendre
                            volum_vendas.append(preu_total)
                            paper_venutA6.append(quantitat_vendre)
                        elif confirmar_venda=="no":
                            print("Venda cancel·lada")
                if opcio_papers=="x":
                    print("Tornant a la pàgina anterior")
                    break
               
        elif opcio==3:
            while True:
                opcio_clients=int(input("""Que vols fer:
                                        1-Veure clients
                                        2-Afegir clients
                                        3-Eliminar clients 
                                        4-Tornar """))
                time.sleep(3)
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
            
        elif opcio==4:
            ventas_total=sum(paper_venutA2)+sum(paper_venutA3)+sum(paper_venutA4)+sum(paper_venutA5)+sum(paper_venutA6)            
            print(f"La empresesa ha venut aquesta quantitat de paquets de A2: {paper_venutA2}")
            print(f"La empresesa ha venut aquesta quantitat de paquets de A3: {paper_venutA3}")
            print(f"La empresesa ha venut aquesta quantitat de paquets de A4: {paper_venutA4}")
            print(f"La empresesa ha venut aquesta quantitat de paquets de A5: {paper_venutA5}")
            print(f"La empresesa ha venut aquesta quantitat de paquets de A6: {paper_venutA6}")
            print(f"i en total ha venut {ventas_total}")
        elif opcio==5:
            benefici_total=sum(volum_vendas)
            print(f"La empresa ha guanyat {volum_vendas} en cada compra")
            print(f"i en total ha guanyat {benefici_total}")
        elif opcio==6:
            print("Tancant programa ...")
            time.slepp(4)
            break

else:
    print("Codi incorrecte. Torna a provar")