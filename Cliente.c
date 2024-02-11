#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Definição da estrutura Cliente
typedef struct {
    char nomePet[50];
    char nomeResponsavel[50];
    char numeroContato[20];
    char tipoAnimal[50];
    char raca[50];
    int idade;
    char genero;
    char tipoServico[50];
    float custo;
    char data[11];
    char hora[6];
} Cliente;

// Função para cadastrar um novo cliente
void cadastrarCliente(Cliente *clientes, int *quantidade) {
    printf("Cadastro de Cliente:\n");
    printf("Nome do Pet: ");
    scanf("%s", clientes[*quantidade].nomePet);
    printf("Nome do Responsavel: ");
    scanf("%s", clientes[*quantidade].nomeResponsavel);
    printf("Numero para Contato: ");
    scanf("%s", clientes[*quantidade].numeroContato);
    printf("Tipo de Animal: ");
    scanf("%s", clientes[*quantidade].tipoAnimal);
    printf("Raca: ");
    scanf("%s", clientes[*quantidade].raca);
    printf("Idade: ");
    scanf("%d", &clientes[*quantidade].idade);
    printf("Genero (M/F): ");
    scanf(" %c", &clientes[*quantidade].genero);
    printf("Tipo de Servico: ");
    scanf("%s", clientes[*quantidade].tipoServico);
    printf("Custo: ");
    scanf("%f", &clientes[*quantidade].custo);

    // Obter data e hora atual
    time_t t = time(NULL);
    struct tm tm = *localtime(&t);
    sprintf(clientes[*quantidade].data, "%02d/%02d/%d", tm.tm_mday, tm.tm_mon + 1, tm.tm_year + 1900);
    sprintf(clientes[*quantidade].hora, "%02d:%02d", tm.tm_hour, tm.tm_min);

    (*quantidade)++; // Incrementa o contador de clientes
}

// Função para salvar os clientes cadastrados em um arquivo
void salvarClientes(Cliente *clientes, int quantidade) {
    FILE *arquivo = fopen("clientes.txt", "w");
    if (arquivo == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return;
    }

    for (int i = 0; i < quantidade; i++) {
        fprintf(arquivo, "%s,%s,%s,%s,%s,%d,%c,%s,%.2f,%s,%s\n",
                clientes[i].nomePet, clientes[i].nomeResponsavel, clientes[i].numeroContato,
                clientes[i].tipoAnimal, clientes[i].raca, clientes[i].idade, clientes[i].genero,
                clientes[i].tipoServico, clientes[i].custo, clientes[i].data, clientes[i].hora);
    }

    fclose(arquivo);
    printf("Clientes salvos com sucesso!\n");
}

// Função para listar os clientes cadastrados
void listarClientes(Cliente *clientes, int quantidade) {
    printf("Lista de Clientes:\n");
    for (int i = 0; i < quantidade; i++) {
        printf("Cliente %d:\n", i + 1);
        printf("Nome do Pet: %s\n", clientes[i].nomePet);
        printf("Nome do Responsavel: %s\n", clientes[i].nomeResponsavel);
        printf("Numero para Contato: %s\n", clientes[i].numeroContato);
        printf("Tipo de Animal: %s\n", clientes[i].tipoAnimal);
        printf("Raca: %s\n", clientes[i].raca);
        printf("Idade: %d\n", clientes[i].idade);
        printf("Genero: %c\n", clientes[i].genero);
        printf("Tipo de Servico: %s\n", clientes[i].tipoServico);
        printf("Custo: %.2f\n", clientes[i].custo);
        printf("Data: %s\n", clientes[i].data);
        printf("Hora: %s\n", clientes[i].hora);
        printf("\n");
    }
}

int main() {
    Cliente clientes[100]; // Capacidade para até 100 clientes
    int opcao, quantidade = 0;

    while (1) {
        printf("Menu:\n");
        printf("1. Cadastrar Cliente\n");
        printf("2. Listar Clientes\n");
        printf("3. Salvar Clientes em Arquivo\n");
        printf("4. Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                if (quantidade < 100) {
                    cadastrarCliente(clientes, &quantidade);
                } else {
                    printf("Limite de clientes atingido!\n");
                }
                break;
            case 2:
                listarClientes(clientes, quantidade);
                break;
            case 3:
                salvarClientes(clientes, quantidade);
                break;
            case 4:
                printf("Encerrando o programa...\n");
                return 0;
            default:
                printf("Opcao invalida. Tente novamente.\n");
        }
    }

    return 0;
}