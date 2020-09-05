menu = """ 
Bienvenido al verificador de Palindromos
Por favor escribe una palabra para verificar: """


def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_inversa = palabra[ ::-1]
    if palabra == palabra_inversa:
        return True
    else:
        return False


def run():
    palabra = (input(menu))
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("La palabra que escribiste es palindromo")
    else:
        print ("La palabra que escribiste no es palindromo")

if __name__ == "__main__" :
    run()