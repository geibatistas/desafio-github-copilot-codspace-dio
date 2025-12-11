#!/usr/bin/env python3

def solicitar_notas():
    while True:
        try:
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            nota3 = float(input("Digite a terceira nota: "))
            
            if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or nota3 < 0 or nota3 > 10:
                print("As notas devem estar entre 0 e 10.")
                continue
            
            return nota1, nota2, nota3
        except ValueError:
            print("Entrada inválida. Informe números válidos.")

def main():
    nota1, nota2, nota3 = solicitar_notas()
    
    media = (nota1 + nota2 + nota3) / 3
    
    print(f"\nNotas fornecidas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    
    if media >= 7:
        print("Situação: APROVADO")
    elif media >= 5:
        print("Situação: EM RECUPERAÇÃO")
    else:
        print("Situação: REPROVADO")

if __name__ == '__main__':
    main()
