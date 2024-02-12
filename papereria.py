import time

clients_compra=['paper corporation','WestRock','UPM']
clients_venta=['El Corte Ingles','La Sol papereria','Amazon']
volum_vendassobres=[]
volum_venda=[]
paper_venutA2=[]
paper_venutA3=[]
paper_venutA4=[]
paper_venutA5=[]
paper_venutA6=[]

sobres_venutC2=[]
sobres_venutC3=[]
sobres_venutC4=[]
sobres_venutC5=[]
sobres_venutC6=[]

volum_compra=[]
volum_compraso=[]

usuari=str(input("Introdueix nom d'usuari: "))
codi=int(input("Introdueix el teu codi: "))

C2=50
C3=50
C4=50
C5=50
C6=50

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
                        2-Comprar paper
                        3-comprar sobres
                        4-Consultar clients
                        5-Volum diners
                        6-Tancar programa
                        """))
        time.sleep(3)
        if opcio==1:
            print(f"La empresa té {diners}€")
            
        
        elif opcio==2:         
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
                        preu_total=(preunodescompte+descompte1)*1.04
                        if A2+unitats_paper<100:
                            confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu_total,2)}€ "))
                            if confirmar_compra=="si":
                                print("Compra realitzada amb èxit")
                                diners=diners-preu_total
                                A2=A2+unitats_paper
                                volum_compra.append(preu_total)
                            elif confirmar_compra=="no":
                                print("Compra cancel·lada")
                        else:
                            print("Estàs superant el màxim de stock del magatzem")
                            

                    elif opcio_papers=="A3":
                        print("Un paquet de A3 de 500ut costa 11,34€")
                        unitats_paper=int(input("Quantitat de paquets que vols comprar: "))
                        preu=11.34
                        preu_caixa=58.45
                        caixa=unitats_paper//5                        
                        caixa1=caixa*preu_caixa
                        preu_individual=(unitats_paper-(caixa*5))*preu
                        preu_total=((preu_individual*0.94)+(caixa1*0.97))*1.04
                        if A3+unitats_paper<150:                        
                            confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu_total,2)}€ "))                       
                            if confirmar_compra=="si":
                                print("Compra realitzada amb èxit")
                                diners=diners-preu_total
                                A3=A3+unitats_paper
                                volum_compra.append(preu_total)
                            elif confirmar_compra=="no":
                                print("Compra cancel·lada")
                        else:
                            print("Estàs superant el màxim de stock del magatzem")
                                              
                    elif opcio_papers=="A4":
                        print("Un paquet de A4 de 500ut costa 7,98€")
                        unitats_paper=int(input("Quantitat de paquets que vols comprar: "))
                        preu=7.98
                        preu_caixa=42.95
                        caixa=unitats_paper//5                        
                        caixa1=caixa*preu_caixa
                        preu_individual=(unitats_paper-(caixa*5))*preu
                        preu_total=((preu_individual*0.95)+(caixa1*0.98))*1.04
                        if A4+unitats_paper<400:                        
                            confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu_total,2)}€ "))
                            if confirmar_compra=="si":
                                print("Compra realitzada amb èxit")
                                diners=diners-preu_total
                                A4=A4+unitats_paper
                                volum_compra.append(preu_total)                           
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
                        preu_total=(preunodescompte+descompte1)*1.04
                        confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu_total,2)}€ "))
                        if A5+unitats_paper<150:                        
                            if confirmar_compra=="si":
                                print("Compra realitzada amb èxit")
                                diners=diners-preu_total
                                A5=A5+unitats_paper
                                volum_compra.append(preu_total)
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
                        preu_total=(preunodescompte+descompte1)*1.04
                        if A6+unitats_paper<300:                        
                            confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_paper} paquets i et gastaràs {round(preu_total,2)}€ "))
                            if confirmar_compra=="si":
                                print("Compra realitzada amb èxit")
                                diners=diners-preu_total
                                A6=A6+unitats_paper  
                                volum_compra.append(preu_total)                        
                            elif confirmar_compra=="no":
                                print("Compra cancel·lada")
                        else:
                            print("Estàs superant el màxim de stock del magatzem")
                    elif opcio_papers=="x":
                        print("Tornant a l'inici")
                        time.sleep(3)
                        break
        
        elif opcio==3:
            while True:
                opcio_sobres=str(input("Quin tipues de paper vols comprar (C2, C3, C4, C5, c6) x-tornar a la pàgina anterior: " ))
                time.sleep(3)
                if opcio_sobres=="C2":
                    print("Un paquet de C2 de 100ut costa 33,45€")
                    unitats_sobre=int(input("Quantitat de paquets que vols comprar: "))
                    descompte=unitats_paper//4
                    descompte1=(7*descompte)/100
                    preunodescompte=(unitats_sobre-(descompte*4))*33.45
                    preu_total=(preunodescompte+descompte1)*1.04
                    if C2+unitats_sobre<100:
                        confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_sobre} paquets i et gastaràs {round(preu_total,2)}€ "))
                        if confirmar_compra=="si":
                            print("Compra realitzada amb èxit")
                            diners=diners-preu_total
                            C2=C2+unitats_sobre
                            volum_compraso.append(preu_total)
                        elif confirmar_compra=="no":
                            print("Compra cancel·lada")
                    else:
                        print("Estàs superant el màxim de stock del magatzem")
                
                elif opcio_sobres=="C3":
                    print("Un paquet de C3 de 100ut costa 30,58€")
                    unitats_sobre=int(input("Quantitat de paquets que vols comprar: "))
                    descompte=unitats_paper//4
                    descompte1=(6*descompte)/100
                    preunodescompte=(unitats_sobre-(descompte*4))*30.58
                    preu_total=(preunodescompte+descompte1)*1.04
                    if C3+unitats_sobre<300:
                        confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_sobre} paquets i et gastaràs {round(preu_total,2)}€ "))
                        if confirmar_compra=="si":
                            print("Compra realitzada amb èxit")
                            diners=diners-preu_total
                            volum_compraso.append(preu_total)
                            C3=C3+unitats_sobre
                        elif confirmar_compra=="no":
                            print("Compra cancel·lada")
                    else:
                        print("Estàs superant el màxim de stock del magatzem")
                
                elif opcio_papers=="C4":
                    print("Un paquet de C4 de 100ut costa 24,78€")
                    unitats_sobre=int(input("Quantitat de paquets que vols comprar: "))
                    descompte=unitats_paper//4
                    descompte1=(5*descompte)/100
                    preunodescompte=(unitats_sobre-(descompte*4))*24.78
                    preu_total=(preunodescompte+descompte1)*1.04
                    if C4+unitats_sobre<400:
                        confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_sobre} paquets i et gastaràs {round(preu_total,2)}€ "))
                        if confirmar_compra=="si":
                            print("Compra realitzada amb èxit")
                            diners=diners-preu_total
                            volum_compraso.append(preu_total)
                            C4=C4+unitats_sobre
                        elif confirmar_compra=="no":
                            print("Compra cancel·lada")
                    else:
                        print("Estàs superant el màxim de stock del magatzem")
                
                elif opcio_sobres=="C5":
                    print("Un paquet de C5 de 100ut costa 20,8€")
                    unitats_sobre=int(input("Quantitat de paquets que vols comprar: "))
                    descompte=unitats_paper//4
                    descompte1=(4*descompte)/100
                    preunodescompte=(unitats_sobre-(descompte*4))*20.8
                    preu_total=(preunodescompte+descompte1)*1.04
                    if C5+unitats_sobre<150:
                        confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_sobre} paquets i et gastaràs {round(preu_total,2)}€ "))
                        if confirmar_compra=="si":
                            print("Compra realitzada amb èxit")
                            diners=diners-preu_total
                            volum_compraso.append(preu_total)
                            C5=C5+unitats_sobre
                        elif confirmar_compra=="no":
                            print("Compra cancel·lada")
                    else:
                        print("Estàs superant el màxim de stock del magatzem")
                
                elif opcio_sobres=="C6":
                    print("Un paquet de C6 de 100ut costa 16,15€")
                    unitats_sobre=int(input("Quantitat de paquets que vols comprar: "))
                    descompte=unitats_paper//4
                    descompte1=(3*descompte)/100
                    preunodescompte=(unitats_sobre-(descompte*4))*16.15
                    preu_total=(preunodescompte+descompte1)*1.04
                    if C6+unitats_sobre<300:
                        confirmar_compra=str(input(f"Vols confirmar la compra? (si/no). Compraràs {unitats_sobre} paquets i et gastaràs {round(preu_total,2)}€ "))
                        if confirmar_compra=="si":
                            print("Compra realitzada amb èxit")
                            diners=diners-preu_total
                            volum_compraso.append(preu_total)
                            C6=C6+unitats_sobre
                        elif confirmar_compra=="no":
                            print("Compra cancel·lada")
                    else:
                        print("Estàs superant el màxim de stock del magatzem")
                
                elif opcio_sobres=="x":
                    print("Tornant a la pàgina anterior")
                    time.sleep(3)
                    break
        elif opcio ==4:           
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
            
        elif opcio==5:
            volum_compratotal=sum(volum_compra)
            print(f"La emprese s'ha gastat {volum_compra} en cada compara de paper.")
            print(f"I en total s'ha gastat en paper {volum_compratotal}€")

            volum_comprasototal=sum(volum_compraso)
            print(f"La emprese s'ha gastat {volum_compraso} en cada compara de sobres.")
            print(f"I en total s'ha gastat en sobres {volum_comprasototal}€")

        elif opcio==6:
            print("Tancant programa ...")
            time.sleep(3)
            break
    

elif codi== 103 and usuari=="Dwight Schrute" or codi==104 and usuari=="Jim Halpert" or codi==105 and usuari=="Andy Bernard":
    print("""Benvingut venedor!! 
    Carregant programa...""")
    time.sleep(3)  
    while True:
        opcio=int(input("""Que vol fer?
                        1-Consultar el magatzem 
                        2-Vendre paper
                        3-vendre sobres
                        4-Consultar clients
                        5-Paper i sobres venuts venut
                        6-Volum vendas
                        7-Tancar programa
                        """))
        if opcio==1:
            print(f"La empresa té al magatzem {A2} paquets de A2")
            print(f"La empresa té al magatzem {A3} paquets de A3")
            print(f"La empresa té al magatzem {A4} paquets de A4")
            print(f"La empresa té al magatzem {A5} paquets de A5")
            print(f"La empresa té al magatzem {A6} paquets de A6")           

            print(f"La empresa té al magatzem {C2} paquets de C2")
            print(f"La empresa té al magatzem {C3} paquets de c3")
            print(f"La empresa té al magatzem {C4} paquets de C4")
            print(f"La empresa té al magatzem {C5} paquets de C5")
            print(f"La empresa té al magatzem {C6} paquets de C6") 
        
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
                        preu_total=(preunodescompte+descompte1)*1.04
                        
                        if preu_total>1000:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=diners+preu_total
                                A2=A2-quantitat_vendre
                                volum_venda.append(preu_total)
                                paper_venutA2.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 999>preu_total>500:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+9.95
                                A2=A2-quantitat_vendre
                                volum_venda.append(preu_total)
                                paper_venutA2.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 499>preu_total>0:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+19.95
                                A2=A2-quantitat_vendre
                                volum_venda.append(preu_total)
                                paper_venutA2.append(quantitat_vendre)
                            
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
                            preu_total=((preu_individual*0.96)+(caixa1*0.98))*1.04

                            if preu_total>1000:
                                confirmar_venda=str(input("Confirma la venda (si/no): "))
                                if confirmar_venda=="si":
                                    print("Venda realitzada amb èxit")
                                    diners=diners+preu_total
                                    A3=A3-quantitat_vendre
                                    volum_venda.append(preu_total)
                                    paper_venutA3.append(quantitat_vendre)
                                
                                elif confirmar_venda=="no":
                                    print("Venda cancel·lada")
                            if 999>preu_total>500:
                                confirmar_venda=str(input("Confirma la venda (si/no): "))
                                if confirmar_venda=="si":
                                    print("Venda realitzada amb èxit")
                                    diners=(diners+preu_total)+9.95
                                    A3=A3-quantitat_vendre
                                    volum_venda.append(preu_total)
                                    paper_venutA3.append(quantitat_vendre)
                                
                                elif confirmar_venda=="no":
                                    print("Venda cancel·lada")
                            if 499>preu_total>0:
                                confirmar_venda=str(input("Confirma la venda (si/no): "))
                                if confirmar_venda=="si":
                                    print("Venda realitzada amb èxit")
                                    diners=(diners+preu_total)+19.95
                                    A3=A3-quantitat_vendre
                                    volum_venda.append(preu_total)
                                    paper_venutA3.append(quantitat_vendre)
                                
                                elif confirmar_venda=="no":
                                    print("Venda cancel·lada")
                            
                if opcio_papers=="A4":
                        if A4<=100:
                            print("No hi ha suficient estoc")
                            
                        else:
                            quantitat_vendre=int(input("Quantitat de paquets de A4 que vols vendre: "))
                            preu=9.45
                            preu_caixa=42.95
                            caixa=quantitat_vendre//5                        
                            caixa1=caixa*preu_caixa
                            preu_individual=(quantitat_vendre-(caixa*5))*preu
                            preu_total=((preu_individual*0.97)+(caixa1*0.99))*1.04                                       
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            
                            if preu_total>1000:
                                confirmar_venda=str(input("Confirma la venda (si/no): "))
                                if confirmar_venda=="si":
                                    print("Venda realitzada amb èxit")
                                    diners=diners+preu_total
                                    A4=A4-quantitat_vendre
                                    volum_venda.append(preu_total)
                                    paper_venutA4.append(quantitat_vendre)
                                
                                elif confirmar_venda=="no":
                                    print("Venda cancel·lada")
                            if 999>preu_total>500:
                                confirmar_venda=str(input("Confirma la venda (si/no): "))
                                if confirmar_venda=="si":
                                    print("Venda realitzada amb èxit")
                                    diners=(diners+preu_total)+9.95
                                    A4=A4-quantitat_vendre
                                    volum_venda.append(preu_total)
                                    paper_venutA4.append(quantitat_vendre)
                                
                                elif confirmar_venda=="no":
                                    print("Venda cancel·lada")
                            if 499>preu_total>0:
                                confirmar_venda=str(input("Confirma la venda (si/no): "))
                                if confirmar_venda=="si":
                                    print("Venda realitzada amb èxit")
                                    diners=(diners+preu_total)+19.95
                                    A4=A4-quantitat_vendre
                                    volum_venda.append(preu_total)
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
                        preu_total=(preunodescompte+descompte1)*1.04
                        confirmar_venda=str(input("Confirma la venda (si/no): "))
                        
                        if preu_total>1000:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=diners+preu_total
                                A5=A5-quantitat_vendre
                                volum_venda.append(preu_total)
                                paper_venutA5.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 999>preu_total>500:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+9.95
                                A5=A5-quantitat_vendre
                                volum_venda.append(preu_total)
                                paper_venutA5.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 499>preu_total>0:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+19.95
                                A5=A5-quantitat_vendre
                                volum_venda.append(preu_total)
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
                        preu_total=(preunodescompte+descompte1)*1.04
                        confirmar_venda=str(input("Confirma la venda (si/no): "))
                        
                        if preu_total>1000:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=diners+preu_total
                                A6=A6-quantitat_vendre
                                volum_venda.append(preu_total)
                                paper_venutA6.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 999>preu_total>500:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+9.95
                                A6=A6-quantitat_vendre
                                volum_venda.append(preu_total)
                                paper_venutA6.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 499>preu_total>0:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+19.95
                                A6=A6-quantitat_vendre
                                volum_venda.append(preu_total)
                                paper_venutA6.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                
                if opcio_papers=="x":
                    print("Tornant a la pàgina anterior")
                    break
               
        elif opcio==3:
             while True:
                opcio_sobres=str(input("Quin tipues de sobres vols vendre (C2, C3, C4, C5, C6)   x-Tornar a la pàgina anterior " ))
                time.sleep(2)
                if opcio_sobres=="C2":
                    if C2<=20:
                     print("No hi ha suficient estoc")
                                        
                    else:
                        quantitat_vendre=int(input("Quantitat de paquets de C2 que vols vendre: "))
                        descompte=quantitat_vendre//4
                        descompte1=(5*descompte)/100
                        preunodescompte=(quantitat_vendre-(descompte*4))*36.45
                        preu_total=preunodescompte+descompte1
                            
                        if preu_total>1000:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=diners+preu_total
                                C2=C2-quantitat_vendre
                                volum_vendassobres.append(preu_total)
                                sobres_venutC2.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 999>preu_total>500:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+9.95
                                C2=C2-quantitat_vendre
                                volum_vendassobres.append(preu_total)
                                sobres_venutC2.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 499>preu_total>0:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+19.95
                                C2=C2-quantitat_vendre
                                volum_venda.append(preu_total)
                                sobres_venutC2.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
   
                if opcio_sobres=="C3":
                    if C3<=30:
                        print("No hi ha suficient estoc")
                                                            
                    else:
                        quantitat_vendre=int(input("Quantitat de paquets de C3 que vols vendre: "))
                        descompte=quantitat_vendre//4
                        descompte1=(4*descompte)/100
                        preunodescompte=(quantitat_vendre-(descompte*4))*32.68
                        preu_total=preunodescompte+descompte1
                                            
                        if preu_total>1000:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=diners+preu_total
                                C3=C3-quantitat_vendre
                                volum_vendassobres.append(preu_total)
                                sobres_venutC3.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 999>preu_total>500:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+9.95
                                C3=C3-quantitat_vendre
                                volum_vendassobres.append(preu_total)
                                sobres_venutC3.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 499>preu_total>0:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+19.95
                                C3=C3-quantitat_vendre
                                volum_venda.append(preu_total)
                                sobres_venutC3.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                
                if opcio_sobres=="C4":     
                    if C4<=60:
                        print("No hi ha suficient estoc")
                                                            
                    else:
                        quantitat_vendre=int(input("Quantitat de paquets de C4 que vols vendre: "))
                        descompte=quantitat_vendre//4
                        descompte1=(3*descompte)/100
                        preunodescompte=(quantitat_vendre-(descompte*4))*26.74
                        preu_total=preunodescompte+descompte1
                                            
                        if preu_total>1000:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=diners+preu_total
                                C4=C4-quantitat_vendre
                                volum_vendassobres.append(preu_total)
                                sobres_venutC4.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 999>preu_total>500:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+9.95
                                C4=C4-quantitat_vendre
                                volum_vendassobres.append(preu_total)
                                sobres_venutC4.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 499>preu_total>0:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+19.95
                                C4=C4-quantitat_vendre
                                volum_venda.append(preu_total)
                                sobres_venutC4.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                
                if opcio_sobres=="C5":     
                    if C5<=40:
                        print("No hi ha suficient estoc")
                                                            
                    else:
                        quantitat_vendre=int(input("Quantitat de paquets de C5 que vols vendre: "))
                        descompte=quantitat_vendre//4
                        descompte1=(2*descompte)/100
                        preunodescompte=(quantitat_vendre-(descompte*4))*22.95
                        preu_total=preunodescompte+descompte1
                                            
                        if preu_total>1000:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=diners+preu_total
                                C5=C5-quantitat_vendre
                                volum_vendassobres.append(preu_total)
                                sobres_venutC5.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 999>preu_total>500:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+9.95
                                C5=C5-quantitat_vendre
                                volum_vendassobres.append(preu_total)
                                sobres_venutC5.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 499>preu_total>0:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+19.95
                                C5=C5-quantitat_vendre
                                volum_venda.append(preu_total)
                                sobres_venutC5.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")   
                
                if opcio_sobres=="C6":     
                    if C6<=100:
                        print("No hi ha suficient estoc")
                                                            
                    else:
                        quantitat_vendre=int(input("Quantitat de paquets de C6 que vols vendre: "))
                        descompte=quantitat_vendre//4
                        descompte1=(1*descompte)/100
                        preunodescompte=(quantitat_vendre-(descompte*4))*17.15
                        preu_total=preunodescompte+descompte1
                                            
                        if preu_total>1000:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=diners+preu_total
                                C6=C6-quantitat_vendre
                                volum_vendassobres.append(preu_total)
                                sobres_venutC6.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 999>preu_total>500:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+9.95
                                C6=C6-quantitat_vendre
                                volum_vendassobres.append(preu_total)
                                sobres_venutC6.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                        if 499>preu_total>0:
                            confirmar_venda=str(input("Confirma la venda (si/no): "))
                            if confirmar_venda=="si":
                                print("Venda realitzada amb èxit")
                                diners=(diners+preu_total)+19.95
                                C6=C6-quantitat_vendre
                                volum_venda.append(preu_total)
                                sobres_venutC6.append(quantitat_vendre)
                            
                            elif confirmar_venda=="no":
                                print("Venda cancel·lada")
                
                if opcio_sobres=="x":
                    print("Tornant a la pàgina anterior")
                    time.sleep(3)
                    break                
        
        elif opcio==4:
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
            
        elif opcio==5:
            ventas_total=sum(paper_venutA2)+sum(paper_venutA3)+sum(paper_venutA4)+sum(paper_venutA5)+sum(paper_venutA6)            
            print(f"La empresesa ha venut aquesta quantitat de paquets de A2: {sum(paper_venutA2)}")
            print(f"La empresesa ha venut aquesta quantitat de paquets de A3: {sum(paper_venutA3)}")
            print(f"La empresesa ha venut aquesta quantitat de paquets de A4: {sum(paper_venutA4)}")
            print(f"La empresesa ha venut aquesta quantitat de paquets de A5: {sum(paper_venutA5)}")
            print(f"La empresesa ha venut aquesta quantitat de paquets de A6: {sum(paper_venutA6)}")
            print(f"i en total ha venut {ventas_total} paquets")
            
            ventas_totalso=sum(sobres_venutC2)+sum(sobres_venutC3)+sum(sobres_venutC4)+sum(sobres_venutC5)+sum(sobres_venutC6)            
            print(f"La empresesa ha venut aquesta quantitat de paquets de C2: {sum(sobres_venutC2)}")
            print(f"La empresesa ha venut aquesta quantitat de paquets de C3: {sum(sobres_venutC3)}")
            print(f"La empresesa ha venut aquesta quantitat de paquets de C4: {sum(sobres_venutC4)}")
            print(f"La empresesa ha venut aquesta quantitat de paquets de C5: {sum(sobres_venutC5)}")
            print(f"La empresesa ha venut aquesta quantitat de paquets de C6: {sum(sobres_venutC6)}")
            print(f"i en total ha venut {ventas_totalso} paquets")
        
        elif opcio==6:
            benefici_totalso=sum(volum_vendassobres)
            print(f"La empresa ha guanyat {volum_vendassobres} en cada venda de sobres")
            print(f"i en total ha guanyat {benefici_totalso}")

            benefici_total=sum(volum_venda)
            print(f"La empresa ha guanyat {volum_venda} en cada venda de sobres")
            print(f"i en total ha guanyat {benefici_total}")
        
        elif opcio==7:
            print("Tancant programa ...")
            time.slepp(4)
            break

else:
    print("Codi incorrecte. Torna a provar")