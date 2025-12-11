#!/usr/bin/env python3

def verificar_paridade():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Entrada inválida. Informe um número inteiro.")
    return numero

def main():
    numero = verificar_paridade()
    
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")

if __name__ == '__main__':
    main()
