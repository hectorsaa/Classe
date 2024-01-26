import time


tipo_papel=['A2','A3','A4','A5','A6']
clients_compra=['paper corporation','WestRock','UPM']
clients_venta=['corte ingles','La Sol papereria','Amazon']
zonas=['A','B','C']
preu_venda=['24.15','12.25','9,45','8.1','7,35']
preu_compra=['18.95','11.34','7.98','7,13','6,40']

contrasenya=int(input("introdueix el teu codi "))

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
                opcio_papers=str(input("Quin tipues de papeers vols comprar (A2, A3, A4, A5, A6) " ))
                
        
        
        
        elif opcio ==3:
            print(f"Els clients són{clients_compra}" )
            
        elif opcio==4:
            print("tancant programa ...")
            time.slepp(4)
    

if contrasenya== 103 or 104 or 105:
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
                
        
        
        
        elif opcio ==3:
            print(f"Els clients són{clients_venta}" )
            
        elif opcio==6:
            print("tancant programa ...")
            time.slepp(4)

else:
    print("codi incorrecte")