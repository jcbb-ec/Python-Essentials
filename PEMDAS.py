
resultado=2+4*5/2
print(resultado)

resultado=(8/2)*(2+2)
print(resultado)

resultado=7-3*2**2
print(resultado)

resultado=(5+3)*2-6/3
print(resultado)

resultado=6*2%5
print(resultado)

resultado=2**2**3
print(resultado)

resultado=(((1+1)-1)*1)/1
print(resultado)

resultado=3 * 4 + 2 / 8 - 2
print(resultado)

resultado=(2 + 3) ** 2
print(resultado)

resultado=((4 - 2) * (3 + 1) / 2)
print(resultado)


############################################################################

num_rebanadas_persona=2
num__refrescos_persona=1
num_personas=4
num_pizzas=5
num_pack_refrescos=2


num_rebanadas_disponibles=num_pizzas*8
num_refrescos_disponibles=num_pack_refrescos*6
num_rebanadas_consumidas=num_personas*num_rebanadas_persona
num_rebanadas_sobran=num_rebanadas_disponibles-num_rebanadas_consumidas


print(f"Rebanadas de pizza sobrantes: {num_rebanadas_sobran}")

##########################################################################

numero_camisas=8
precio_camisa=20
descuento=20
cantidad_compra_cliente=4

costo=cantidad_compra_cliente*precio_camisa*(1-descuento/100)
print(f'Precio total con descuento: ${costo}')

########################################################################

horas_viaje=4
distancia=800

velocidad=distancia/horas_viaje
distancia_hora=velocidad*1

print(f"Velocidad en Km/h: {distancia_hora}")


####################################################################

precio_camiseta=15
precio_chaqueta=50
descuento=10
num_camisetas=2
num_chaquetas=1

costo=(num_camisetas*precio_camiseta+num_chaquetas*precio_chaqueta)*(1-descuento/100)
print(f'Precio con descuento: ${costo}')

###################################################################

num_paginas_libro=500
num_dias=5
paginas_dia=num_paginas_libro/num_dias
print(f'Número de páginas por día: {paginas_dia} ')


################################################################
precio_celular=250
meses=12
interes=0
pago_mes=precio_celular/meses
print(f"Precio mensual: ${pago_mes}")

#################################################################

costo_viaje_bus=50
descuento_estusiantes=15
num_estudiantes=3

precio_estudiante=costo_viaje_bus*(1-descuento_estusiantes/100)
precio_total=num_estudiantes*precio_estudiante
print(f"Precio total para {num_estudiantes} estudiantes: ${precio_total}")


#################################################################
gramos_pack_fideo=500
num_porciones_pack=5
num_gramos_porcion=gramos_pack_fideo/num_porciones_pack
num_porciones=3

num_gramos_cocinar=num_gramos_porcion*num_porciones
print(f"Gramos de fideos para {num_porciones} porciones: {num_gramos_cocinar}")

###########################################################
unidades_pack=24
num_personas=6

galletas_persona=unidades_pack/num_personas
print(f'Número de galletas por persona: {galletas_persona}')


#################################################################
dinero_cuenta=200
deposito_mes=50
tiempo=12

dinero_cuenta = dinero_cuenta + tiempo*deposito_mes
print(f'Saldo despúes de 1 año: ${dinero_cuenta}')

























