lista_routers=[]
lista_switches=[]
lista_otros=[]
lista_equipos=['R1','R2','R3','R4','S1','S2','S3','AP1','FW1','OLT1']

for item in lista_equipos:
    if 'R' in item:
        lista_routers.append(item)
    elif 'S' in item:
        lista_switches.append(item)
    else:
        lista_otros.append(item)
        
print(f'La lista de routers es: {lista_routers}')
print(f'La lista de switches es: {lista_switches}')
print(f'La lista de otros equipos es: {lista_otros}')

