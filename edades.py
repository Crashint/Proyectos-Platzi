Nombre_1 = str(input("Cual es su nombre?"))
Edad_1 = int(input("Cual es su edad?"))
Nombre_2 = str(input("Cual es su nombre?"))
Edad_2 = int(input("Cual es su edad?"))

if Edad_1 > Edad_2:
    print (Nombre_1,f"{'es mayor que'}". Nombre_2)
elif Edad_1 < Edad_2:
    print (Nombre_2,f"{'es mayor que'}", Nombre_1)
else:
    print('ambos tienen la misma edad')
