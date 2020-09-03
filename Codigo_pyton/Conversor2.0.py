pesos = input('¿Cuántos pesos mexicanos tienes? :')
pesos = int(pesos)
valor_dolares = 21.70
dolares = pesos / valor_dolares 
dolares = round(dolares,2)
dolares = str(dolares)
print ('Tienes $' + dolares + ' dolares')