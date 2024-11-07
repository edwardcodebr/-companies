#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Escola {
    char nome[100];
    int matricula;
    float coeficiente;
    struct Escola* proximo; 
} Escola;

typedef struct Mensagens {
    const char* menu;
    const char* cadastrarAluno;
    const char* listarAlunos;
    const char* sair;
    const char* erroAlocarMemoria;
    const char* alunoCadastrado;
    const char* alunoVazio;
    const char* nomePrompt;
    const char* matriculaPrompt;
    const char* coeficientePrompt;
    const char* escolhaInvalida;
} Mensagens;

Mensagens mensagensPt() {
    Mensagens msg = {
        "MENU:\n1. Cadastrar aluno\n2. Listar alunos\n3. Sair\nEscolha uma opção: ",
        "Digite o nome do aluno: ",
        "Digite a matrícula do aluno: ",
        "Digite o coeficiente do aluno: ",
        "Erro ao alocar memória.\n",
        "Aluno cadastrado com sucesso!\n",
        "Nenhum aluno cadastrado.\n",
        "Digite o nome do aluno: ",
        "Digite a matrícula do aluno: ",
        "Digite o coeficiente do aluno: ",
        "Opção inválida! Tente novamente.\n"
    };
    return msg;
}

Mensagens mensagensEn() {
    Mensagens msg = {
        "MENU:\n1. Register student\n2. List students\n3. Exit\nChoose an option: ",
        "Enter student's name: ",
        "Enter student's registration number: ",
        "Enter student's coefficient: ",
        "Memory allocation error.\n",
        "Student successfully registered!\n",
        "No students registered.\n",
        "Enter student's name: ",
        "Enter student's registration number: ",
        "Enter student's coefficient: ",
        "Invalid option! Try again.\n"
    };
    return msg;
}

Escola* insere(Escola* fila, char* nome, int matricula, float coeficiente) {
    
    Escola* novoAluno = (Escola*) malloc(sizeof(Escola));
    if (novoAluno == NULL) {
        return fila; 
    }

    // Preenche os dados do novo aluno
    strcpy(novoAluno->nome, nome);
    novoAluno->matricula = matricula;
    novoAluno->coeficiente = coeficiente;
    novoAluno->proximo = NULL; 

    if (fila == NULL) {
        return novoAluno;
    }

    Escola* temp = fila;
    while (temp->proximo != NULL) {
        temp = temp->proximo;
    }
    temp->proximo = novoAluno;

    return fila;
}

void imprimeAlunos(Escola* fila, Mensagens msg) {
    if (fila == NULL) {
        printf("%s", msg.alunoVazio);
        return;
    }

    Escola* temp = fila;
    while (temp != NULL) {
        printf("Nome: %s, Matricula: %d, Coeficiente: %.2f\n", temp->nome, temp->matricula, temp->coeficiente);
        temp = temp->proximo;
    }
}

// Função para cadastrar um aluno
void cadastrarAluno(Escola** fila, Mensagens msg) {
    char nome[100];
    int matricula;
    float coeficiente;

    printf("%s", msg.nomePrompt);
    fgets(nome, sizeof(nome), stdin);  
    nome[strcspn(nome, "\n")] = 0;  

    printf("%s", msg.matriculaPrompt);
    scanf("%d", &matricula);

    printf("%s", msg.coeficientePrompt);
    scanf("%f", &coeficiente);


    *fila = insere(*fila, nome, matricula, coeficiente);
    printf("%s", msg.alunoCadastrado);
}


void menu(Mensagens msg) {
    Escola* fila = NULL;
    int opcao;

    do {
        printf("%s", msg.menu);
        scanf("%d", &opcao);
        getchar();  

        switch (opcao) {
            case 1:
                cadastrarAluno(&fila, msg);
                break;
            case 2:
                imprimeAlunos(fila, msg);
                break;
            case 3:
                printf("Saindo do programa...\n");
                break;
            default:
                printf("%s", msg.escolhaInvalida);
        }
    } while (opcao != 3);
}


void escolherIdioma() {
    int idioma;
    printf("Escolha o idioma:\n1. Português\n2. English\nEscolha: ");
    scanf("%d", &idioma);
    getchar();  

    if (idioma == 1) {
        menu(mensagensPt());  
    } else if (idioma == 2) {
        menu(mensagensEn());  
    } else {
        printf("Opção inválida. Saindo...\n");
    }
}

int main() {
    escolherIdioma();  
    return 0;
}
