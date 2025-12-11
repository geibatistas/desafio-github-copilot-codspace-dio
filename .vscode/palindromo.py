#!/usr/bin/env python3

def verificar_palindromo():
    palavra = input("Digite uma palavra: ")
    return palavra.strip().lower()

def main():
    palavra = verificar_palindromo()
    
    # Inverter a palavra usando slicing
    palavra_invertida = palavra[::-1]
    
    # Comparar com a original
    if palavra == palavra_invertida:
        print(f"'{palavra}' é um PALÍNDROMO! 🎉")
    else:
        print(f"'{palavra}' NÃO é um palíndromo.")
        print(f"A palavra invertida é: '{palavra_invertida}'")

if __name__ == '__main__':
    main()
