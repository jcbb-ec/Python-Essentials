
nombre=input('Ingrese su nombre: ')
apellido=input('Ingrese su apellido: ')
ubicacion=input('Ingrese su ubcación: ')
edad=int(input('Ingrese su edad: '))

if edad<18:
    clasificacion='menor'
elif edad<66:
    clasificacion='joven'
elif edad<80:
    clasificacion='de mediana edad'
elif edad<100:
    clasificacion='anciano'
else:
    clasificacion='anciano longevo'
    

print(f'Sr./Sra. {nombre} {apellido}, su orden de alitas picantes está en camino a {ubicacion}.' 
      f' Además, por ser {clasificacion} con {edad} años recibirá 2 bebidas de cortesía.')



