import numpy as np

# Matriz de coeficientes A e vetor de constantes b (Exemplo)
A = np.array([
    [1, -2, 3, 4],
    [2, 1, -4, 2],
    [3, 4, 1, -2],
    [-4, 1, 2, 3]
], dtype=float)

b = np.array([5, -3, 6, -2], dtype=float)

tolerancia = 0.01
max_iteracoes = 100

x_atual = np.zeros(len(b))

for iteracao in range(max_iteracoes):
    x_novo = np.zeros(len(b))
    
    for i in range(len(b)):
        soma = b[i]
        for j in range(len(b)):
            if i != j:
                soma -= A[i][j] * x_atual[j]
        x_novo[i] = soma / A[i][i]
    
    erro_max = np.max(np.abs(x_novo - x_atual))
    if erro_max < tolerancia:
        print(f"Convergido na iteração {iteracao + 1}")
        break
    
    x_atual = x_novo
else:
    print("Número máximo de iterações alcançado sem convergência.")

print("Solução:", x_novo)
