#!/usr/bin/env python3

def solicitar_numeros():
    while True:
        try:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            return num1, num2
        except ValueError:
            print("Entrada inválida. Informe números válidos.")

def main():
    num1, num2 = solicitar_numeros()
    
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2 if num2 != 0 else "Indefinida (divisão por zero)"
    
    print(f"\nOperações com {num1} e {num2}:")
    print(f"Adição: {num1} + {num2} = {soma}")
    print(f"Subtração: {num1} - {num2} = {subtracao}")
    print(f"Multiplicação: {num1} × {num2} = {multiplicacao}")
    print(f"Divisão: {num1} ÷ {num2} = {divisao}")

if __name__ == '__main__':
    main()
