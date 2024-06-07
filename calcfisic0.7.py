import numpy as np
import matplotlib.pyplot as plt
import math
import sys
def calcular_trajetoria(v0, theta, gravidade):
    theta_rad = math.radians(theta)

    t_total = (2 * v0 * math.sin(theta_rad)) / gravidade

    d = v0 * math.cos(theta_rad) * t_total

    h_max = (v0**2 * (math.sin(theta_rad)**2)) / (2 * gravidade)

    return d, h_max   

def plotar_trajetoria(tempos, alturas):
    plt.plot(tempos, alturas)
    plt.title('trajetoria do objeto')
    plt.xlabel('Tempo(s)')
    plt.ylabel('altura(m)')
    plt.grid(True)
    plt.show()

def velocidade_carro (distancia, tempo):
    velocidade = distancia / tempo
    print(velocidade," M/S.")
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

def calcular_energia_cinetica(massa, velocidade):
    # Calcula a energia cinética usando a fórmula EC = 1/2 * m * v^2
    energia_cinetica = 0.5 * massa * (velocidade ** 2)
    return energia_cinetica

def calcular_forca_atrito(coeficiente_atrito, forca_normal):
    # Calcula a força de atrito usando a fórmula Fₐ = μ * N
    forca_atrito = coeficiente_atrito * forca_normal
    return forca_atrito

def calc_forc(massa, aceleracao):
    forca = massa * aceleracao
    return forca

def calcular_velocidade_onda(frequencia, comprimento_onda):
    # Calcula a velocidade da onda usando a fórmula v = f * λ
    velocidade = frequencia * comprimento_onda
    return velocidade
def onda_senoidal(x, t, A=1, k=2, omega=3, phi=0):
    """
    Calcula a onda senoidal em um ponto (x, t) com os parâmetros dados.

    Args:
    x (float): Posição na direção da propagação da onda.
    t (float): Tempo.
    A (float, optional): Amplitude máxima da onda. Default é 1.
    k (float, optional): Número de onda. Default é 2.
    omega (float, optional): Frequência angular. Default é 3.
    phi (float, optional): Fase inicial da onda. Default é 0.

    Returns:
    float: Amplitude da onda no ponto (x, t).
    """
    return A * np.sin(k * x - omega * t + phi)
def onda_eletromagnetica_1d(x, t, A=1, lambda_=1, omega=2*np.pi, phi=0):
    """
    Calcula a amplitude da onda eletromagnética em uma dimensão.

    Args:
    x (float): Posição na direção da propagação da onda.
    t (float): Tempo.
    A (float, optional): Amplitude máxima da onda. Default é 1.
    lambda_ (float, optional): Comprimento de onda. Default é 1.
    omega (float, optional): Frequência angular. Default é 2*pi.
    phi (float, optional): Fase inicial da onda. Default é 0.

    Returns:
    float: Amplitude da onda no ponto (x, t).
    """
    k = 2 * np.pi / lambda_  # Número de onda
    Ex = A * np.sin(k * x - omega * t + phi)  # Campo elétrico
    By = A * np.sin(k * x - omega * t + phi)  # Campo magnético
    return Ex, By
def forca_gravitacional(m1, m2, r, G=6.67430e-11):
    """
    Calcula a força gravitacional entre dois corpos.

    Args:
    m1 (float): Massa do primeiro corpo em kg.
    m2 (float): Massa do segundo corpo em kg.
    r (float): Distância entre os centros dos corpos em metros.
    G (float, optional): Constante gravitacional universal em N*m²/kg². Default é 6.67430e-11.

    Returns:
    float: Força gravitacional entre os corpos em Newtons.
    """
    return G * abs(m1 * m2) / r**2
def equacao_bernoulli(P, rho, v, h, g=9.81):
    """
    Calcula a constante da equação de Bernoulli.

    Args:
    P (float): Pressão do fluido em pascals (Pa).
    rho (float): Densidade do fluido em quilogramas por metro cúbico (kg/m³).
    v (float): Velocidade do fluido em metros por segundo (m/s).
    h (float): Altura em metros em relação a uma referência escolhida.
    g (float, optional): Aceleração devido à gravidade em metros por segundo ao quadrado (m/s²). Default é 9.81.

    Returns:
    float: Constante da equação de Bernoulli.
    """
    return P + 0.5 * rho * v**2 + rho * g * h

def eletricidade(r, i):
    "u flaot, em volts, resistenc float ohml, corrente em amprere float"
    u = r*i
    return u

def capacitor(cargae, difpot):
    "dada uma carga eletrica em float divido pela diferença potencial em float é dada a capacitância"
    capacitancia = cargae*difpot
    return capacitancia

def gravidade(g, m, r):
    gravity = g*m/r**2
    return gravity

def dilatlinear(compriin, material, tempod):
    compri = compriin*material*(tempod)
    return compri

def dilatvol(volin, material1, tempod1):
    dilvol = volin * material1 * tempod1
    return dilvol

while True:
    print('''
Bem-vindo ao aplicativo de fisica
versão: 0.7.24
Escolha sua opção:
1 - Medir velocidade em KM.
2 - Medir distancia de um lançamento obliquo em m.
3 - Medir resistencia.
4 - Transformar celsius para Fahrenheit.
5 - Transformar celsius para Kelvin.
6 - Transformar Fahrenheit para celsius.
7 - Transformar Kelvin para celsius.
8 - Calcular energia cinética.
9 - Calcular força de atrito.
10 - Calcular força.
11 - calcular velocidade da onda.
12 - calcular onda senodial.
13 - calcular onda eletromagnetica.
14 - mostrar força gravitacional
15 - equação de Bernoulli.
16 - medir eletricidade.
17 - medir capacitor.
18 - ver explicação do calculo da gravidade da terra.
19 - ver explicação do valor de PI na física.
20 - medir dilatação linear.
21 - medir dilatação volumetrica.
22 - lista de materiais para dilatação em notação cientifica.
23 - Materiais para engenharia(densidade, modulo, resistencia e coeficiente).
24 - Sair.''')
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
            print(f"Distância total: {distancia:.2f} metros") 
            print(f"Altura máxima: {altura_maxima:.2f} Metros")
    
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
            massa = float(input("Digite a massa do objeto em kg (em float: 0.00): "))
            velocidade = float(input("Digite a velocidade do objeto em m/s (em float: 0.00): "))

            # Calcula a energia cinética
            energia = calcular_energia_cinetica(massa, velocidade)

           # Exibe o resultado
            print(f"A energia cinética do objeto é: {energia:.2f} joules")
        case 9:
            coeficiente_atrito = float(input("digite o coeficiente de atrito (em float: 0.00):"))
            forca_normal = float(input("Digite a força normal em Newtons(em float: 0.00):"))
            
            forca_atrito = calcular_forca_atrito(coeficiente_atrito, forca_normal)
            
            print(f"A força de atrito é: {forca_atrito:.2f} Newtons.") 
        case 10:
            massa = float(input("Digite a massa do objeto em quilogramas(em float: 0.00):"))
            aceleracao = float(input("digite a aceleração em metros por segundo ao quadrado(em float: 0.00)"))
            
            forca = calc_forc(massa, aceleracao)
            print(f"A força resultante é: {forca:.2f} Newtons")
        case 11:
            frequencia = float(input("digite a frquencia em heartz (Hz):"))
            comprimento_onda = float(input("Digite o comprimento de onda em metros(em float: 0.00):"))
            
            velocidade_onda = calcular_velocidade_onda(frequencia, comprimento_onda)
            print(f"A velocidade da onda é: {velocidade_onda:.2f} metros por segundo.")
        case 12:
            x = np.linspace(0, 4*np.pi, 100)  # De 0 a 4*pi    
            t = np.linspace(0, 4*np.pi, 100)  # De 0 a 4*pi

# Criando uma malha de x e t
            x, t = np.meshgrid(x, t)

# Calculando a onda senoidal
            y = onda_senoidal(x, t)

            # Plotando a onda
            plt.figure(figsize=(10, 6))
            plt.imshow(y, cmap='viridis', extent=[0, 4*np.pi, 0, 4*np.pi], aspect='auto')
            plt.colorbar(label='Amplitude')
            plt.title('Onda Senoidal')
            plt.xlabel('x')
            plt.ylabel('t')
            plt.show()
        case 13:
            x = np.linspace(0, 10, 1000)  # Espaço
            t = np.linspace(0, 10, 1000)  # Tempo

# Criando uma malha de x e t
            x, t = np.meshgrid(x, t)

# Calculando o campo elétrico e magnético em função de x e t
            Ex, By = onda_eletromagnetica_1d(x, t)

# Plotando o campo elétrico
            plt.figure(figsize=(12, 6))
            plt.subplot(2, 1, 1)
            plt.imshow(Ex, cmap='viridis', extent=[0, 10, 0, 10], aspect='auto')
            plt.colorbar(label='Campo Elétrico (Ex)')
            plt.title('Simulação de Onda Eletromagnética - Campo Elétrico')
            plt.xlabel('Espaço')
            plt.ylabel('Tempo')

# Plotando o campo magnético
            plt.subplot(2, 1, 2)
            plt.imshow(By, cmap='viridis', extent=[0, 10, 0, 10], aspect='auto')
            plt.colorbar(label='Campo Magnético (By)')
            plt.title('Simulação de Onda Eletromagnética - Campo Magnético')
            plt.xlabel('Espaço')
            plt.ylabel('Tempo')

            plt.tight_layout()
            plt.show()
        case 14:
            m1 = 5.972e24  # Massa da Terra em kg
            m2 = 7.348e22  # Massa da Lua em kg
            r = 3.844e8  # Distância média entre a Terra e a Lua em metros

            forca = forca_gravitacional(m1, m2, r)
            print(f"A força gravitacional entre a Terra e a Lua é {forca} Newtons.")
        case 15:
            P = float(input("Digite a pressão do fluido em pascals (Pa): "))
            rho = float(input("Digite a densidade do fluido em quilogramas por metro cúbico (kg/m³): "))
            v = float(input("Digite a velocidade do fluido em metros por segundo (m/s): "))
            h = float(input("Digite a altura em metros em relação a uma referência escolhida: "))
            g = float(input("Digite a aceleração devido à gravidade em metros por segundo ao quadrado (m/s²): "))

# Cálculo da constante de Bernoulli 
            constante_bernoulli = equacao_bernoulli(P, rho, v, h, g)

# Output
            print(f"A constante de Bernoulli é: {constante_bernoulli} Pa")
        case 16:
            print("Insira a resistência(em float):")
            r = float(input())
            print("insira a corrente em amperes")
            i = float(input())
            u = eletricidade(r, i)
            print(f"{u} Volts")
        case 17:
            print("Insira a carga elétrica(em float):")
            cargae = float(input())
            print("insira a diferença potencial(em float)")
            difpot = float(input())
            capacitancia = capacitor(cargae, difpot)
            print(f"{capacitancia:.2f} Jaules")
        case 18:
            print('''A gravidade da terra, denotada por "g" na física,
            é a aceleração que um objeto experimenta devido a atração gravitacional da terra.
            O valor padrão da gravidade ao nível do mar é aproximadamente 9,81 m/s**2.
            Este valor pode ser calculado utilizando a fórmula da lei da Gravitação universal de Newton.
            
            g = GM/R**2
            Onde:
            G = é a constante gravitacional(6,674x10**-11)
            M = é a massa da terra(5,972x10**24)
            R = É o raio da terra(6,371x10**6)''')
            g = 6.674*10**-11
            m = 5.972*10**24
            r = 6.371*10**6
            gravity = gravidade(g, m, r)
            print(f"Gravidade da terra igual {gravity:.3}")
            print("-- Bônus --")
            print('''A gravidade igual a 10 m/s**2, é usado na engenharia em seus cálculos no ensino por:
            Simplicidade nos cálculos, aproximação suficiente precisa, facilitação no ensino e margem de segurança.
            Portanto, o uso de 10m/s**2 é uma prática comum devido à conveniência e à pequena margem de erro introduzida pela aproximação.''')
        case 19:
            print("A constante matemática (pi):")
            print('''Tem relação com uma circuferência de um circulo e seu diâmetro,
            desempenha um papel fundamental em muitos campos da física. Sua história na física está ligada com o desenvolvimento
            da mátematica e da ciência em geral.
            Hoje, PI é fundamental em muitos campos da física, incluindo mecânica, termodinâmica, eletricidade e magnetismo.
            É amplamente utilizado em cálculos e formulações teóricas.''')
            print("-- Bônus --")
            print('Refêrencia na biblia:')
            print('''Em 1 Reis 7:23, onde é descrita a construção de um "mar de fundição"
            um grande recipiente circular no templo de Salomão. O versículo afirma que o diâmetro do mar era de 10 côvados e com perímetro de 30 côvados,
            o que implicaria um valor de PI igual a 3. Essa simplificação pode ter sido feita por conveniência prática ou por razões simbólicas,
            e não reflete a precisão matemática atual de PI.''')
        case 20:
            print("digite o comprimento inicial(em float 0.00).")
            compriin = float(input())
            print("digite o material para dilatar (em inteiro 0)")
            print('''1 - aluminio
2 - cobre
3 - vidro
4 - aço
5 - cimento''')
            materilist = int(input())
            match materilist:
                case 1:
                    aluminio = 2.4*pow(10,-5)
                    material = aluminio
                case 2:
                    cobre = 1.7*pow(10,-5)
                    material = cobre
                case 3:
                    vidro = 0.5*pow(10,-5)
                    material = vidro
                case 4:
                    aco = 1.2*pow(10,-5)
                    material = aco
                case 5:
                    cimento = 0.7*pow(10,-5)
                    material = cimento
            print("digite o temperatura final(em float 0.00):")
            tempf = float(input())
            print("digite o temperatura inicial(em float 0.00):")
            tempin = float(input())
            tempod = tempf - tempin
            compri = dilatlinear(compriin, material, tempod)
            print(f"{compri} Metros")
        case 21:
            print("Digite o volume cubico inicial (em float 0.00)")
            volin = float(input())
            print("digite o material para dilatar (em inteiro 0)")
            print('''1 - agua
2 - gelo
3 - cobre
4 - aco
5 - vidro
6 - concreto
7 - vidro prex''')
            materilist1 = int(input())
            match materilist1:
                case 1:
                    agua = 3.3*pow(10,-4)
                    material1 = agua
            
                case 2:
                    gelo = 1.53*pow(10,-4)
                    material1 = gelo
                   
                case 3:
                    cobre = 5.1*pow(10,-5)
                    material1 = cobre
                   
                case 4:
                    aco = 3.3*pow(10,-5)
                    material1 = aco
                  
                case 5:
                    vidro = 2.7*pow(10,-5)
                    material1 = cimento
                  
                case 6:
                    concreto = 3.6* pow(10,-5)
                    material1 = concreto
                  
                case 7:
                    vidroprex = 9.6*pow(10,-6)
                    material1 = vidroprex
                    
            print("digite o temperatura final(em float 0.00):")
            tempf1 = float(input())
            print("digite o temperatura inicial(em float 0.00):")
            tempin1 = float(input())
            tempod1 = tempf1 - tempin1
            dilvol = dilatvol(volin, material1, tempod1)
            print(f"{dilvol} Metros cubicos.")
        case 22:
            print('''A dilatação térmica é um fenômeno físico que descreve a variação das dimensões de um corpo devido à variação de temperatura. Os principais materiais que apresentam dilatação térmica são os sólidos, líquidos e gases. Aqui estão alguns exemplos de materiais e seus coeficientes de dilatação linear em notação científica:

    Alumínio: 2.3×10−5 K−12.3×10−5K−1
    Ferro: 1.2×10−5 K−11.2×10−5K−1
    Cobre: 1.7×10−5 K−11.7×10−5K−1
    Chumbo: 2.9×10−5 K−12.9×10−5K−1
    Aço: 1.1×10−5 K−11.1×10−5K−1
    Vidro: 0.9×10−5 K−10.9×10−5K−1
    Água: 0.21×10−3 K−10.21×10−3K−1
    Mercúrio: 0.18×10−3 K−10.18×10−3K−1
    Ar (ideal): 3.4×10−3 K−13.4×10−3K−1
    Zinco: 3.0×10−5 K−13.0×10−5K−1
    Latão: 1.9×10−5 K−11.9×10−5K−1
    Níquel: 1.3×10−5 K−11.3×10−5K−1
    Prata: 1.9×10−5 K−11.9×10−5K−1
    Ouro: 1.4×10−5 K−11.4×10−5K−1
    Platina: 8.8×10−6 K−18.8×10−6K−1
    Tungstênio: 4.5×10−6 K−14.5×10−6K−1
    Quartzo: 0.55×10−6 K−10.55×10−6K−1
    Gelo: 5.0×10−5 K−15.0×10−5K−1
    Borracha: 2.0×10−4 K−12.0×10−4K−1
    Madeira (média): 5.0×10−6 K−15.0×10−6K−1
    Tijolo: 5.0×10−6 K−15.0×10−6K−1
    Cimento: 5.0×10−6 K−15.0×10−6K−1
    Poliéster: 6.0×10−5 K−16.0×10−5K−1
    Poliestireno: 8.5×10−5 K−18.5×10−5K−1
    Polietileno: 1.1×10−4 K−11.1×10−4K−1
    Acrílico: 7.5×10−5 K−17.5×10−5K−1
    Cristal: 0.55×10−6 K−10.55×10−6K−1
    Concreto: 1.2×10−5 K−11.2×10−5K−1
    Granito: 3.0×10−6 K−13.0×10−6K−1
    Mármore: 5.0×10−6 K−15.0×10−6K−1
    PVC: 5.5×10−5 K−15.5×10−5K−1
    Vidro borossilicato: 3.3×10−6 K−13.3×10−6K−1
    Ferro fundido: 1.0×10−5 K−11.0×10−5K−1
    Aço inoxidável: 1.6×10−5 K−11.6×10−5K−1
    Alumina: 8.0×10−6 K−18.0×10−6K−1
    Carbono (grafite): 8.0×10−6 K−18.0×10−6K−1
    Silício: 2.6×10−6 K−12.6×10−6K−1
    Silício (cristalino): 2.6×10−6 K−12.6×10−6K−1
    Quartzo (fused): 0.55×10−6 K−10.55×10−6K−1
    Teflon: 1.1×10−4 K−11.1×10−4K−1
    Vidro de borosilicato: 3.3×10−6 K−13.3×10−6K−1
    Nitinol: 1.1×10−5 K−11.1×10−5K−1
    Niobato de lítio: 10.0×10−6 K−110.0×10−6K−1
    Zircônia: 10.0×10−6 K−110.0×10−6K−1
    Ametista: 5.0×10−6 K−15.0×10−6K−1
    Safira: 5.0×10−6 K−15.0×10−6K−1
    Rubidium: 8.6×10−6 K−18.6×10−6K−1
    Argônio: 5.3×10−5 K−15.3×10−5K−1
    Enxofre: 2.0×10−5 K−12.0×10−5K−1
    Ferro (gama): 4.6×10−5 K−14.6×10−5K−1
    
Esses valores representam a variação percentual de comprimento por grau Celsius de temperatura.''')
        case 23:
            print('''Materiais para engenharia são importantes na fisica, pois sua densidade, resistencia, cedencia, modulo e coefinciente correspondem com a fisica:
Aço Carbono:

    Densidade: ~7850 kg/m³
    Resistência: ~250-500 MPa
    Módulo de Elasticidade: ~200 GPa
    Coeficiente de Expansão Térmica: ~12 x 10^-6 /°C

Alumínio:

    Densidade: ~2700 kg/m³
    Resistência: ~300 MPa
    Módulo de Elasticidade: ~70 GPa
    Coeficiente de Expansão Térmica: ~23.1 x 10^-6 /°C

Cobre:

    Densidade: ~8900 kg/m³
    Resistência: ~220 MPa
    Módulo de Elasticidade: ~110 GPa
    Coeficiente de Expansão Térmica: ~16.5 x 10^-6 /°C

Titânio:

    Densidade: ~4500 kg/m³
    Resistência: ~1000 MPa
    Módulo de Elasticidade: ~110 GPa
    Coeficiente de Expansão Térmica: ~8.6 x 10^-6 /°C

Aço Inoxidável:

    Densidade: ~7900 kg/m³
    Resistência: ~500-1000 MPa
    Módulo de Elasticidade: ~200 GPa
    Coeficiente de Expansão Térmica: ~10-17 x 10^-6 /°C

Polietileno de Alta Densidade (HDPE):

    Densidade: ~950 kg/m³
    Resistência: ~20-30 MPa
    Módulo de Elasticidade: ~0.8-1.0 GPa
    Coeficiente de Expansão Térmica: ~100-200 x 10^-6 /°C

Ferro Fundido:

    Densidade: ~6800-7800 kg/m³
    Resistência: ~100-700 MPa
    Módulo de Elasticidade: ~100-170 GPa
    Coeficiente de Expansão Térmica: ~10-14 x 10^-6 /°C

Alumina (Cerâmica):

    Densidade: ~3900 kg/m³
    Resistência: ~200-400 MPa
    Módulo de Elasticidade: ~300-400 GPa
    Coeficiente de Expansão Térmica: ~8 x 10^-6 /°C

Concreto:

    Densidade: ~2400 kg/m³
    Resistência: ~20-40 MPa
    Módulo de Elasticidade: ~15-30 GPa
    Coeficiente de Expansão Térmica: ~10-15 x 10^-6 /°C

Madeira (Pinus):

    Densidade: ~500 kg/m³
    Resistência: ~40-80 MPa
    Módulo de Elasticidade: ~5-10 GPa
    Coeficiente de Expansão Térmica: ~5-8 x 10^-6 /°C

Polímeros Reforçados com Fibra de Carbono:

    Densidade: ~1500-2000 kg/m³
    Resistência: ~1000-4000 MPa
    Módulo de Elasticidade: ~150-300 GPa
    Coeficiente de Expansão Térmica: ~0,1-3 x 10^-6 /°C

Vidro:

    Densidade: ~2500 kg/m³
    Resistência: ~20-120 MPa
    Módulo de Elasticidade: ~50-90 GPa
    Coeficiente de Expansão Térmica: ~8-10 x 10^-6 /°C

Cimento Portland:

    Densidade: ~3100 kg/m³
    Resistência: ~10-80 MPa
    Módulo de Elasticidade: ~10-40 GPa
    Coeficiente de Expansão Térmica: ~8-13 x 10^-6 /°C

Tungstênio:

    Densidade: ~19300 kg/m³
    Resistência: ~550-1000 MPa
    Módulo de Elasticidade: ~400-550 GPa
    Coeficiente de Expansão Térmica: ~4.5 x 10^-6 /°C

Zinco:

    Densidade: ~7100 kg/m³
    Resistência: ~100-300 MPa
    Módulo de Elasticidade: ~80-110 GPa
    Coeficiente de Expansão Térmica: ~30-35 x 10^-6 /°C

Nylon:

    Densidade: ~1100 kg/m³
    Resistência: ~40-80 MPa
    Módulo de Elasticidade: ~2-4 GPa
    Coeficiente de Expansão Térmica: ~70-170 x 10^-6 /°C

PVC (Policloreto de Vinila):

    Densidade: ~1400 kg/m³
    Resistência: ~50-80 MPa
    Módulo de Elasticidade: ~2.5-4 GPa
    Coeficiente de Expansão Térmica: ~50-80 x 10^-6 /°C

Latão:

    Densidade: ~8500 kg/m³
    Resistência: ~100-550 MPa
    Módulo de Elasticidade: ~90-130 GPa
    Coeficiente de Expansão Térmica: ~18-20 x 10^-6 /°C

Ferro:

    Densidade: ~7850 kg/m³
    Resistência: ~200-400 MPa
    Módulo de Elasticidade: ~190-210 GPa
    Coeficiente de Expansão Térmica: ~11-13 x 10^-6 /°C

Bronze:

    Densidade: ~8300 kg/m³''')
        case 24:
            print("DESLIGANDO")
            sys.exit()