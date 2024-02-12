from tqdm import tqdm
import time
import os
print('carregando sistema.')
for i in tqdm(range(100)):
    time.sleep(0.03) 
print('''
Seja bem vindo ao sistema de passageiro.
Escolha a opção...
1 - prosseguir com o sistema de passageiro.
2 - sair''')
esc = int(input())
os.system("cls")

match esc:
    case 1:
        print("Carregando.")
        for i in tqdm(range(100)):
            time.sleep(0.03)
        while True:
            print(''' 
Menu do funcionario:
1 - continuar com o trabalho.
2 - Desligar o sistema''')
            cont = int(input())
            if cont == 2:
                SystemExit()

            assentos = [['0' for i in range(4)]for i in range(10)]

            def print_assento(assentos):
                for linha in assentos:
                    print(''.join(linha))

                        
            print("Quantos passageiros precisam embarcar?")
            people = int(input())
            for i in range(people):
                print(f"Assentos disponiveis para pessoa {people}:")
                print_assento(assentos)
                linha = int(input("Digite a linha (0 à 9):"))
                coluna = int(input("Digite a coluna (0 à 3):"))

                if linha < 0 or linha > 9 or coluna < 0 or coluna > 3:
                    print("Assento invalido, tente novamente...")
                else:
                    assentos[linha][coluna] = 'X'
                    print("Assento ocupado com X:")
                    print_assento(assentos)
    case 2:
        print("Desligando...")
        for i in tqdm(range(100)):
            time.sleep(0.03)
        
        SystemExit()    