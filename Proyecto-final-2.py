# Paso 1: Solicitar las medidas de la pieza del mueble en cms

medidas_cm = float(input("Por favor, ingresar la medida de la pieza del mueble en cms: "))

# Paso 2: Convertirlas de cm a pulgadas

medidas_pulgadas = medidas_cm / 2.54

# Paso 3: Mostrar medidas al usuario.
print("Las medidas en pulgadas de la pieza ingresada son: ", medidas_pulgadas)