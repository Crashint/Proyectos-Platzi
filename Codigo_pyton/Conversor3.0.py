menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """
def informacion(moneda, valor_dolar):
    pesos = input('¿Cuántos Pesos ' + moneda + ' tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dólares')

opcion = int (input(menu))
if opcion == 1:
    informacion("colombianos",3875)
elif opcion == 2:
    informacion('argentinos', 65)
elif opcion == 3:
    informacion('mexicanos', 21.70)
else: print('Elige una opcion correcta')
