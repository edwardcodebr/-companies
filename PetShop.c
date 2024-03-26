#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

FILE *arquivo;
FILE *arquivo2;

int opcao, quantidade = 0;

typedef struct cliente CLIENTE;

struct cliente { // Definição da estrutura Cliente
    char nomeResponsavel[50];
    char nomePet[50];
    char numeroContato[20];
    char tipoAnimal[50];
    char raca[50];
    int idade;
    char genero;
    char tipoServico[50];
    float custo;
    char data[11];
    char hora[6];
};
// declarando funções de ilustração
void logo();
void gatocaixa();
void gatobye();
void pikashuerro();



void cadastrarCliente(CLIENTE *clientes, int *quantidade){ // Função para cadastrar um novo cliente
    printf("Carregando... \n");
    printf("\n*** CADASTRAR CLIENTE ***\n");
    printf("Insira o nome do responsável do Pet: ");
    scanf("%s", clientes[*quantidade].nomePet);
    printf("Insira o nome do Pet: ");
    scanf("%s", clientes[*quantidade].nomeResponsavel);
    printf("Insira um número para contato: ");
    scanf("%s", clientes[*quantidade].numeroContato);
    printf("Insira o tipo de animal: ");
    scanf("%s", clientes[*quantidade].tipoAnimal);
    printf("Insira a raça do Pet: ");
    scanf("%s", clientes[*quantidade].raca);
    printf("Insira a idade do Pet: ");
    scanf("%d", &clientes[*quantidade].idade);
    printf("Informe o gênero do Pet (M/F): ");
    scanf(" %c", &clientes[*quantidade].genero);
    printf("Informe o tipo de serviço realizado: ");
    scanf("%s", clientes[*quantidade].tipoServico);
    printf("Informe o custo do serviço: ");
    scanf("%f", &clientes[*quantidade].custo);

    time_t t = time(NULL); // Obter data e hora atual
    struct tm tm = *localtime(&t);
    sprintf(clientes[*quantidade].data, "%02d/%02d/%d", tm.tm_mday, tm.tm_mon + 1, tm.tm_year + 1900);
    sprintf(clientes[*quantidade].hora, "%02d:%02d", tm.tm_hour, tm.tm_min);

    (*quantidade)++; // Incrementa o contador de clientes
}

void salvarClientes(CLIENTE *clientes, int quantidade) { // Função para salvar os clientes cadastrados em um arquivo
    arquivo = fopen("clientes.txt", "w");

    if (arquivo == NULL){
        printf("ERRO: A conexão com o banco de dados falhou!");
        return;
    }

    for (int i = 0; i < quantidade; i++) {
        fprintf(arquivo, "%s,%s,%s,%s,%s,%d,%c,%s,%.2f,%s,%s\n",
                clientes[i].nomeResponsavel, clientes[i].nomePet, clientes[i].numeroContato,
                clientes[i].tipoAnimal, clientes[i].raca, clientes[i].idade, clientes[i].genero,
                clientes[i].tipoServico, clientes[i].custo, clientes[i].data, clientes[i].hora);
    }

    fclose(arquivo);
    printf("Clientes salvos com sucesso!\n");
}

void listarClientes(CLIENTE *clientes, int quantidade) { // Função para listar os clientes para salvar no cadastrados
    printf("Listando... \n");
    printf("\n*** CLIENTES ***\n");
    for (int i = 0; i < quantidade; i++) {
        printf("Cliente %d:\n", i + 1);
        printf("Nome do Pet: %s\n", clientes[i].nomeResponsavel);
        printf("Nome do Responsável: %s\n", clientes[i].nomePet);
        printf("Número para Contato: %s\n", clientes[i].numeroContato);
        printf("Tipo de Animal: %s\n", clientes[i].tipoAnimal);
        printf("Raça: %s\n", clientes[i].raca);
        printf("Idade: %d\n", clientes[i].idade);
        printf("Gênero: %c\n", clientes[i].genero);
        printf("Tipo de Serviço: %s\n", clientes[i].tipoServico);
        printf("Custo: %.2f\n", clientes[i].custo);
        printf("Data: %s\n", clientes[i].data);
        printf("Hora: %s\n", clientes[i].hora);
        printf("\n");
    }
}

void filtrarClientes(CLIENTE *clientes) {  // Função para filtrar os dados dos clientes

    int i = 0;
    char *word;
    char c;
    char pesquisa[50];
    char linha[130];

    arquivo = fopen("clientes.txt", "r");
    arquivo2 = fopen("pesquisa.txt", "w");

    if (arquivo == NULL || arquivo2 == NULL){
        printf("ERRO: A conexão com o banco de dados falhou!");
        pikashuerro();
        return;
    }

    printf("Digite a palavra que deseja filtrar: ");
    scanf("%s", pesquisa);

    while ((c = fgetc(arquivo) != EOF)){

        fgets(linha, 100, arquivo);
        word = strtok(linha, ",");

        int j = 0;
        while (word != NULL){

            switch (j){
                case 0:
                case 1:
                case 2:
                case 3:
                case 4:
                case 5:
                case 6:
                case 7:
                    if (strcmp(word, pesquisa) == 0){
                        printf("Resultado encontrado!\n");
                        fprintf(arquivo2, "%s,%s,%s,%s,%s,%d,%c,%s,%.2f,%s,%s\n",
                                clientes[i].nomeResponsavel, clientes[i].nomePet, clientes[i].numeroContato,
                                clientes[i].tipoAnimal, clientes[i].raca, clientes[i].idade, clientes[i].genero,
                                clientes[i].tipoServico, clientes[i].custo, clientes[i].data, clientes[i].hora);}
                    break;
            }
            word = strtok(NULL, ",");
            j++;
        }
        i++;
    }
    fclose(arquivo2);
    fclose(arquivo);
}

void deletarClientes() { // Função para deletar clientes
    FILE *arquivo3 = fopen("clientes2.txt", "w");
    arquivo = fopen("clientes.txt", "r");

    int i = 0;
    int j = 0;
    char pesquisa[10];
    char linha[100];

    if (arquivo == NULL || arquivo3 == NULL){
        printf("ERRO: A conexão com o banco de dados falhou!");
        return;
    }

    printf("Digite o nome do cliente cujos dados se deseja excluir: ");
    scanf("%s", pesquisa);

    while (fgets(linha, sizeof(linha), arquivo) != NULL){
        i++;
        if (strstr(linha, pesquisa) != NULL){
            break;
        }
    }

    while (fgets(linha, sizeof(linha), arquivo) !=NULL){
        if (j!= i){
            fputs(linha, arquivo3);
        } else {
            printf("Cliente excluído com sucesso! \n");
        }
        j++;
    }

    fclose(arquivo3);
    fclose(arquivo);

    remove("clientes.txt");
    rename("clientes2.txt", "clientes.txt");
}

void menu_inicial() {
    printf("\n===============================================");
    printf("\nEscolha o que deseja fazer: \n");
    printf("1 - Cadastrar Cliente\n");
    printf("2 - Confirmar Clientes para cadastro\n");
    printf("3 - Salvar Clientes em Arquivo\n");
    printf("4 - Filtrar Clientes\n");
    printf("5 - Deletar Cliente\n");
    printf("6 - Sair\n");
    printf("\n===============================================\n");
    printf("\nDigite o numero da opcao que deseja: ");
    scanf("%d", &opcao);
}

int main(){
    char C;
    CLIENTE clientes[100]; // Capacidade para até 100 clientes
    logo();
    printf("\n*** Seja bem-vindo(a) ao sistema do Pet Shop! ***\n");
    while (1) {
        menu_inicial();
        switch (opcao) {
            case 1:
                if (quantidade < 100){
                    cadastrarCliente(clientes, &quantidade);
                }else{
                    printf("ERRO: O limite de clientes foi atingido!\n");
                }
                break;
            case 2:
                listarClientes(clientes, quantidade);
                break;
            case 3:
                salvarClientes(clientes, quantidade);
                break;
            case 4:
                filtrarClientes(clientes);
                gatocaixa();
                break;
            case 5:
                deletarClientes();
                break;
            case 6:
                gatobye();
                printf("digite bye: ");
                scanf(" %C ", &C);
                printf("\nSaindo... \n");
                exit(0);
                break;
            default:
                printf("Digite uma opcao valida! \n");
                break;
        }
    }
    return 0;
}

//ilustrações
void gatocaixa(void){
      printf("  ,-.       _,---._ __  / \\\n");
    printf(" /  )    .-'       `./ /   \\\n");
    printf("(  (   ,'            `/    /|\n");
    printf(" \  `-'              \\'\\   / |\n");  
    printf("  `.                , \\\\ /  |\n");
    printf("   /`.          ,'-`----Y   |\n");    
    printf("  (            ;        |   '\n");
    printf("  |  ,-.    ,-'         |  /\n");
    printf("  |  | (   |        arq | /\n");
    printf("  )  |  \  `.____________|/\n");
    printf("  `--'   `--'\n");
    printf("\n");
}

void logo(void){
        printf("\t\t\t\t                                  ,'\\\n");
    printf("\t\t\t\t    _.----.        ____         ,'  _\\   ___    ___     ____\n");
    printf("\t\t\t\t_,-'       `.     |    |  /`.   \\,-'    |   \\  /   |   |    \\  |`.\n");
    printf("\t\t\t\t\\      __    \\    '-.  | /   `.  ___    |    \\/    |   '-.   \\ |  |\n");
    printf("\t\t\t\t \\.    \\ \\   |  __  |  |/    ,','_  `.  |          | __  |    \\|  |\n");
    printf("\t\t\t\t  \\    \\/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |\n");
    printf("\t\t\t\t   \\     ,-'/  /   \\    ,'   | \\/ / ,`.|         /  /   \\  |     |\n");
    printf("\t\t\t\t    \\    \\ |   \\_/  |   `-.  \\    `'  /|  |    ||   \\_/  | |\\    |\n");
    printf("\t\t\t\t     \\    \\ \\      /       `-.`.___,-' |  |\\  /| \\      /  | |   |\n");
    printf("\t\t\t\t      \\    \\ `.__,'|  |`-._    `|      |__| \\/ |  `.__,'|  | |   |\n");
    printf("\t\t\t\t       \\_.-'       |__|    `-._ |              '-.|     '-.| |   |\n");
    printf("\t\t\t\t                               `'                            '-._|\n");
    printf("\t\t\t\t             ___    ___    _____  ___    _   _  _____  ___   \n");
    printf("\t\t\t\t            (  _`\\ (  _`\\ (_   _)(  _`\\ ( ) ( )(  _  )(  _`\\ \n");
    printf("\t\t\t\t            | |_) )| (_(_)  | |  | (_(_)| |_| || ( ) || |_) )\n");
    printf("\t\t\t\t            | ,__/'|  _)_   | |  `\\__ \\ |  _  || | | || ,__/'\n");
    printf("\t\t\t\t            | |    | (_( )  | |  ( )_) || | | || (_) || |    \n");
    printf("\t\t\t\t            (_)    (____/'  (_)  `\\____)(_) (_)(_____)(_)    .-.\n");
}
void gatobye(void){
            printf("                                        .\n");
        printf("                         |              |\n");
        printf("                         |             ,|\n");
        printf("                ,_       |\\            F'   ,.-\"\"`.\n");
        printf("               /  `-._   |`           // ,-\"_,..  |\n");
        printf("              |   ___ `. | \\ ,\"\"\"`-. /.-' ,'    ' |_....._\n");
        printf("              |  /   `-.`.  L......|j j_.'      ` |       `._\n");
        printf("              | |      _,'| |______|' | '-._     ||  ,.-.    `.\n");
        printf("               L|    ,'   | |      | j      `-.  || '    `.    \\\n");
        printf("___            | \\_,'     | |`\"----| |         `.||       |\\    \\\n");
        printf(" \"\"=+...__     `,'   ,.-.   |....._|   _....     Y \\      j_),..+=--\n");
        printf("     `\"-._\"._  .   ,' |  `   \\    /  ,' |   \\     \\ j,..-\"_..+-\"  L\n");
        printf("          `-._-+. j   !   \\   `--'  .   !    \\  ,.-\" _..<._  |    |\n");
        printf("              |-. |   |    L        |   !     |  .-/'      `.|-.,-|\n");
        printf("              |__ '   '    |        '   |    /    /|   `, -. |   j\n");
        printf("        _..--'\"__  `-.___,'          `.___,.'  __/_|_  /   / '   |\n");
        printf("   _.-_..---\"\"_.-\\                            .,...__\"\"--./L/_   |\n");
        printf(" -'\"\"'     ,\"\"  ,-`-.    .___.,...___,    _,.+\"      \"\"\"\"`-+-==++-\n");
        printf("     bye  / /  `.   )\"-.._`v \\|    V/  /-'    \\._,._.'\"-. /    /\n");
        printf("          ` `.  )---.     `\"\"\\\\__  / .'        /    \\    Y\"._.'\n");
        printf("           `\"'`\"     `-.     /|._\"\"_/         |  ,..   _ |  |\n");
        printf("                        `\"\"\"' |  \"'           `. `-'  (_|,-.'\n");
        printf("                               \\               |`       .`-\n");
        printf("                                `.           . j`._    /\n");
        printf("                                 |`.._     _.'|    `\"\"/\n");
        printf("                                 |    /\"\"'\"   |  .\". j\n");
        printf("                                .`.__j         \\ `.' |\n");
        printf("                                j    |          `._.'\n");
        printf("                               /     |\n");
        printf("                              /,  ,  \\\n");
        printf("                              \\|  |   L\n");
        printf("                               `..|_..' mh\n");
}
void pikashuerro(void){
    printf("      ,___          .-;'\n");
    printf("      `'-.`\\_...._/`.`\n");
    printf("   ,      \\        /\n");
    printf(" .-' ',    / ()   ()\\n");
    printf("`'._   \\  /()    .  (|\n");
    printf("    > .' ;,     -'-  /\n");
    printf("   / <   |;,     __.;\n");
    printf("   '-.'-.|  , \\    , \\n");
    printf("      `>.|;, \\_)    \\_)\n");
    printf("       `-;     ,    /\n");
    printf("          \\    /   <\n");
    printf("           '. <`'-,_)\n");
    printf("       erro '._)\n");
    printf("\n");
}