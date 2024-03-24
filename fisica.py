import matplotlib.pyplot as plt
import math
import sys
def calcular_trajetoria(v0, theta, gravidade):
    theta_rad = math.radians(theta)

    t_total = (2 * v0 * math.sin(theta_rad)) / gravidade

    d = v0 * math.cos(theta_rad) * t_total

    h_max = (v0**2 * (math.sin(theta_rad)**2)) / (2 * gravidade)

    return d, h_max   

def velocidade_carro (distancia, tempo):
    velocidade = distancia / tempo
    print(velocidade," M/S.");
    return distancia, tempo

def lei_ohl (volt, amperes):
    resistencia = volt / amperes

    print(resistencia, " ohms.")

    return resistencia

def conversao_f (celsius1):
    fhn = (9/5 * celsius1 + 32)

    print(fhn, " F°.")
    return celsius1

def conversao_k (celsius2):
    kelvin = celsius2 + 273.15
    print(kelvin, " K°.")

def conversao_celsius_fahrenheit (fh):
    celsiusfinal1 = 5/9*(fh - 32)
    print(celsiusfinal1, " C°.")

def conversao_celsius_kelvin (klv):
    celsiusfinal2 = klv - 273.15
    print(celsiusfinal2, " C°.")



while True:
    print('''
Bem-vindo ao aplicativo de fisica
Escolha sua opção:
1 - Medir velocidade em KM.
2 - Medir distancia de um lançamento obliquo em m.
3 - Medir resistencia.
4 - Transformar celsius para Fahrenheit.
5 - Transformar celsius para Kelvin.
6 - Transformar Fahrenheit para celsius.
7 - Transformar Kelvin para celsius.
8 - sair.
    ''')
    escolha = int(input())
    match escolha:
        case 1:
            distancia = float(input("Corrida do carro em quilometros(0.00KM):"))
            tempo = float(input("Tempo percorrido em horas(acrescente o minutos em 0.00):"))
            velocidade_carro(distancia, tempo)
        case 2:
            theta = float(input("Digite o ângulo de lançamento em graus (em float: 0.00):"))
            v0 = float(input("Digite a velocidade inicial em m/s (metros por segundo: 0.00):"))
            gravidade = 9.81
            distancia, altura_maxima = calcular_trajetoria(v0, theta, gravidade)
            print(f"Distancia percorrida: {distancia:.2f} metros.")
            print(f"Altura máxima atingida de: {altura_maxima:.2f} metros.")  
            
        case 3:
            volt = float(input("Voltagem:"))
            amperes = float(input("Corrente em amperes:"))
            lei_ohl(volt, amperes)
        case 4:
            celsius1 = float(input("temperatura(em celsius):"))
            conversao_f(celsius1)
        case 5:
            celsius2 = float(input("temperatura(em celsius):"))
            conversao_k(celsius2)
        case 6:
            fh = float(input("temperatura (em fahrenheit):"))
            conversao_celsius_fahrenheit(fh)
        case 7:
            klv = float(input("temperatura (em kelvin):"))
            conversao_celsius_kelvin(klv)
        case 8:
            print("DESLIGANDO")
            sys.exit()