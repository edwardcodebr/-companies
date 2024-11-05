package sistema;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    private static Scanner scanner = new Scanner(System.in);
    private static String idioma = "pt"; 

    private static Map<String, Curso> cursos = new HashMap<>();
    private static Map<String, Disciplina> disciplinas = new HashMap<>();
    private static Map<String, Professor> professores = new HashMap<>();
    private static Map<String, Aluno> alunos = new HashMap<>();

    public static void main(String[] args) {
        escolherIdioma();
        inicializarDados();
        exibirMenu();
    }
    
    public static void inicializarDados() {
        // Adicionando cursos
        Curso curso1 = new Curso("Computação");
        Curso curso2 = new Curso("Produção");
        Curso curso3 = new Curso("Elétrica");
        Curso curso4 = new Curso("Eletrônica");
        Curso curso5 = new Curso("Química");
        Curso curso6 = new Curso("Naval");
        Curso curso7 = new Curso("Mecânica");

        Curso curso8 = new Curso("Computer Science");
        Curso curso9 = new Curso("Production Engineering");
        Curso curso10 = new Curso("Electrical Engineering");
        Curso curso11 = new Curso("Electronics");
        Curso curso12 = new Curso("Chemistry");
        Curso curso13 = new Curso("Naval Engineering");
        Curso curso14 = new Curso("Mechanical Engineering");

        Curso curso15 = new Curso("Computación");
        Curso curso16 = new Curso("Producción");
        Curso curso17 = new Curso("Eléctrica");
        Curso curso18 = new Curso("Electrónica");
        Curso curso19 = new Curso("Química");
        Curso curso20 = new Curso("Naval");
        Curso curso21 = new Curso("Mecánica");

        Curso curso22 = new Curso("Informatique");
        Curso curso23 = new Curso("Production");
        Curso curso24 = new Curso("Électrique");
        Curso curso25 = new Curso("Électronique");
        Curso curso26 = new Curso("Chimie");
        Curso curso27 = new Curso("Naval");
        Curso curso28 = new Curso("Mécanique");

        // Adicionando os cursos ao mapa
        cursos.put(curso1.getNome(), curso1);
        cursos.put(curso2.getNome(), curso2);
        cursos.put(curso3.getNome(), curso3);
        cursos.put(curso4.getNome(), curso4);
        cursos.put(curso5.getNome(), curso5);
        cursos.put(curso6.getNome(), curso6);
        cursos.put(curso7.getNome(), curso7);
        cursos.put(curso8.getNome(), curso8);
        cursos.put(curso9.getNome(), curso9);
        cursos.put(curso10.getNome(), curso10);
        cursos.put(curso11.getNome(), curso11);
        cursos.put(curso12.getNome(), curso12);
        cursos.put(curso13.getNome(), curso13);
        cursos.put(curso14.getNome(), curso14);
        cursos.put(curso15.getNome(), curso15);
        cursos.put(curso16.getNome(), curso16);
        cursos.put(curso17.getNome(), curso17);
        cursos.put(curso18.getNome(), curso18);
        cursos.put(curso19.getNome(), curso19);
        cursos.put(curso20.getNome(), curso20);
        cursos.put(curso21.getNome(), curso21);
        cursos.put(curso22.getNome(), curso22);
        cursos.put(curso23.getNome(), curso23);
        cursos.put(curso24.getNome(), curso24);
        cursos.put(curso25.getNome(), curso25);
        cursos.put(curso26.getNome(), curso26);
        cursos.put(curso27.getNome(), curso27);
        cursos.put(curso28.getNome(), curso28);

        Disciplina disciplina1 = new Disciplina("Programação I");
        Disciplina disciplina2 = new Disciplina("Estruturas de Dados");
        Disciplina disciplina3 = new Disciplina("Física");
        Disciplina disciplina4 = new Disciplina("Álgebra");
        Disciplina disciplina5 = new Disciplina("Administração");
        Disciplina disciplina6 = new Disciplina("Economia");
        Disciplina disciplina7 = new Disciplina("Meio Ambiente");
        Disciplina disciplina8 = new Disciplina("Cálculo");
        Disciplina disciplina9 = new Disciplina("Circuitos");
        Disciplina disciplina10 = new Disciplina("Eletrônica");
        Disciplina disciplina11 = new Disciplina("Sistemas");
        Disciplina disciplina12 = new Disciplina("Desenho Técnico");
        Disciplina disciplina13 = new Disciplina("Química");
        Disciplina disciplina14 = new Disciplina("Matemática Discreta");

        // Disciplinas em inglês
        Disciplina disciplina15 = new Disciplina("Programming I");
        Disciplina disciplina16 = new Disciplina("Data Structures");
        Disciplina disciplina17 = new Disciplina("Physics");
        Disciplina disciplina18 = new Disciplina("Algebra");
        Disciplina disciplina19 = new Disciplina("Management");
        Disciplina disciplina20 = new Disciplina("Economics");
        Disciplina disciplina21 = new Disciplina("Environmental Science");
        Disciplina disciplina22 = new Disciplina("Calculus");
        Disciplina disciplina23 = new Disciplina("Circuits");
        Disciplina disciplina24 = new Disciplina("Electronics");
        Disciplina disciplina25 = new Disciplina("Systems");
        Disciplina disciplina26 = new Disciplina("Technical Drawing");
        Disciplina disciplina27 = new Disciplina("Chemistry");
        Disciplina disciplina28 = new Disciplina("Discrete Mathematics");

        // Disciplinas em espanhol
        Disciplina disciplina29 = new Disciplina("Programación I");
        Disciplina disciplina30 = new Disciplina("Estructuras de Datos");
        Disciplina disciplina31 = new Disciplina("Física");
        Disciplina disciplina32 = new Disciplina("Álgebra");
        Disciplina disciplina33 = new Disciplina("Administración");
        Disciplina disciplina34 = new Disciplina("Economía");
        Disciplina disciplina35 = new Disciplina("Medio Ambiente");
        Disciplina disciplina36 = new Disciplina("Cálculo");
        Disciplina disciplina37 = new Disciplina("Circuitos");
        Disciplina disciplina38 = new Disciplina("Electrónica");
        Disciplina disciplina39 = new Disciplina("Sistemas");
        Disciplina disciplina40 = new Disciplina("Dibujo Técnico");
        Disciplina disciplina41 = new Disciplina("Química");
        Disciplina disciplina42 = new Disciplina("Matemática Discreta");

        // Disciplinas em francês
        Disciplina disciplina43 = new Disciplina("Programmation I");
        Disciplina disciplina44 = new Disciplina("Structures de Données");
        Disciplina disciplina45 = new Disciplina("Physique");
        Disciplina disciplina46 = new Disciplina("Algèbre");
        Disciplina disciplina47 = new Disciplina("Gestion");
        Disciplina disciplina48 = new Disciplina("Économie");
        Disciplina disciplina49 = new Disciplina("Environnement");
        Disciplina disciplina50 = new Disciplina("Calcul");
        Disciplina disciplina51 = new Disciplina("Circuits");
        Disciplina disciplina52 = new Disciplina("Électronique");
        Disciplina disciplina53 = new Disciplina("Systèmes");
        Disciplina disciplina54 = new Disciplina("Dessin Technique");
        Disciplina disciplina55 = new Disciplina("Chimie");
        Disciplina disciplina56 = new Disciplina("Mathématiques Discrètes");

        // Adicionando as disciplinas ao mapa
        disciplinas.put(disciplina1.getNome(), disciplina1);
        disciplinas.put(disciplina2.getNome(), disciplina2);
        disciplinas.put(disciplina3.getNome(), disciplina3);
        disciplinas.put(disciplina4.getNome(), disciplina4);
        disciplinas.put(disciplina5.getNome(), disciplina5);
        disciplinas.put(disciplina6.getNome(), disciplina6);
        disciplinas.put(disciplina7.getNome(), disciplina7);
        disciplinas.put(disciplina8.getNome(), disciplina8);
        disciplinas.put(disciplina9.getNome(), disciplina9);
        disciplinas.put(disciplina10.getNome(), disciplina10);
        disciplinas.put(disciplina11.getNome(), disciplina11);
        disciplinas.put(disciplina12.getNome(), disciplina12);
        disciplinas.put(disciplina13.getNome(), disciplina13);
        disciplinas.put(disciplina14.getNome(), disciplina14);

        // Disciplinas em inglês
        disciplinas.put(disciplina15.getNome(), disciplina15);
        disciplinas.put(disciplina16.getNome(), disciplina16);
        disciplinas.put(disciplina17.getNome(), disciplina17);
        disciplinas.put(disciplina18.getNome(), disciplina18);
        disciplinas.put(disciplina19.getNome(), disciplina19);
        disciplinas.put(disciplina20.getNome(), disciplina20);
        disciplinas.put(disciplina21.getNome(), disciplina21);
        disciplinas.put(disciplina22.getNome(), disciplina22);
        disciplinas.put(disciplina23.getNome(), disciplina23);
        disciplinas.put(disciplina24.getNome(), disciplina24);
        disciplinas.put(disciplina25.getNome(), disciplina25);
        disciplinas.put(disciplina26.getNome(), disciplina26);
        disciplinas.put(disciplina27.getNome(), disciplina27);
        disciplinas.put(disciplina28.getNome(), disciplina28);

        // Disciplinas em espanhol
        disciplinas.put(disciplina29.getNome(), disciplina29);
        disciplinas.put(disciplina30.getNome(), disciplina30);
        disciplinas.put(disciplina31.getNome(), disciplina31);
        disciplinas.put(disciplina32.getNome(), disciplina32);
        disciplinas.put(disciplina33.getNome(), disciplina33);
        disciplinas.put(disciplina34.getNome(), disciplina34);
        disciplinas.put(disciplina35.getNome(), disciplina35);
        disciplinas.put(disciplina36.getNome(), disciplina36);
        disciplinas.put(disciplina37.getNome(), disciplina37);
        disciplinas.put(disciplina38.getNome(), disciplina38);
        disciplinas.put(disciplina39.getNome(), disciplina39);
        disciplinas.put(disciplina40.getNome(), disciplina40);
        disciplinas.put(disciplina41.getNome(), disciplina41);
        disciplinas.put(disciplina42.getNome(), disciplina42);

        // Disciplinas em francês
        disciplinas.put(disciplina43.getNome(), disciplina43);
        disciplinas.put(disciplina44.getNome(), disciplina44);
        disciplinas.put(disciplina45.getNome(), disciplina45);
        disciplinas.put(disciplina46.getNome(), disciplina46);
        disciplinas.put(disciplina47.getNome(), disciplina47);
        disciplinas.put(disciplina48.getNome(), disciplina48);
        disciplinas.put(disciplina49.getNome(), disciplina49);
        disciplinas.put(disciplina50.getNome(), disciplina50);
        disciplinas.put(disciplina51.getNome(), disciplina51);
        disciplinas.put(disciplina52.getNome(), disciplina52);
        disciplinas.put(disciplina53.getNome(), disciplina53);
        disciplinas.put(disciplina54.getNome(), disciplina54);
        disciplinas.put(disciplina55.getNome(), disciplina55);
        disciplinas.put(disciplina56.getNome(), disciplina56);
    }

    public static void escolherIdioma() {
    	System.out.println("created by Eduardo Correa and Lucas Fernando.");
        System.out.println("Escolha o idioma / Choose the language:");
        System.out.println("1. Português");
        System.out.println("2. English");
        System.out.println("3. Español");
        System.out.println("4. Français");

        int escolhaIdioma = scanner.nextInt();
        scanner.nextLine(); 

        switch (escolhaIdioma) {
            case 1:
                idioma = "pt";
                break;
            case 2:
                idioma = "en";
                break;
            case 3:
                idioma = "es";
                break;
            case 4:
                idioma = "fr";
                break;
            default:
                System.out.println("Idioma inválido, usando Português.");
                idioma = "pt";
        }
    }

    public static void exibirMenu() {
        boolean sair = false;

        while (!sair) {
            switch (idioma) {
                case "pt":
                    System.out.println("Menu Principal:");
                    System.out.println("1. Cadastrar Curso");
                    System.out.println("2. Cadastrar Disciplina");
                    System.out.println("3. Cadastrar Professor");
                    System.out.println("4. Cadastrar Aluno");
                    System.out.println("5. Matricular Aluno em Disciplina");
                    System.out.println("6. Exibir Informações de Curso");
                    System.out.println("7. Exibir Informações de Disciplina");
                    System.out.println("8. Exibir Informações de Professor");
                    System.out.println("9. Exibir Informações de Aluno");
                    System.out.println("10. Sair");
                    break;
                case "en":
                    System.out.println("Main Menu:");
                    System.out.println("1. Register Course");
                    System.out.println("2. Register Subject");
                    System.out.println("3. Register Teacher");
                    System.out.println("4. Register Student");
                    System.out.println("5. Enroll Student in Subject");
                    System.out.println("6. Display Course Information");
                    System.out.println("7. Display Subject Information");
                    System.out.println("8. Display Teacher Information");
                    System.out.println("9. Display Student Information");
                    System.out.println("10. Exit");
                    break;
                case "es":
                    System.out.println("Menú Principal:");
                    System.out.println("1. Registrar Curso");
                    System.out.println("2. Registrar Asignatura");
                    System.out.println("3. Registrar Profesor");
                    System.out.println("4. Registrar Alumno");
                    System.out.println("5. Inscribir Alumno en Asignatura");
                    System.out.println("6. Mostrar Información del Curso");
                    System.out.println("7. Mostrar Información de la Asignatura");
                    System.out.println("8. Mostrar Información del Profesor");
                    System.out.println("9. Mostrar Información del Alumno");
                    System.out.println("10. Salir");
                    break;
                case "fr":
                    System.out.println("Menu Principal:");
                    System.out.println("1. Enregistrer un Cours");
                    System.out.println("2. Enregistrer une Discipline");
                    System.out.println("3. Enregistrer un Professeur");
                    System.out.println("4. Enregistrer un Élève");
                    System.out.println("5. Inscrire un Élève à une Discipline");
                    System.out.println("6. Afficher les Informations du Cours");
                    System.out.println("7. Afficher les Informations de la Discipline");
                    System.out.println("8. Afficher les Informations du Professeur");
                    System.out.println("9. Afficher les Informations de l'Élève");
                    System.out.println("10. Quitter");
                    break;
            }

            System.out.print(getMensagem("escolhaOpcao"));
            int escolha = scanner.nextInt();
            scanner.nextLine(); 

            switch (escolha) {
                case 1:
                    cadastrarCurso();
                    break;
                case 2:
                    cadastrarDisciplina();
                    break;
                case 3:
                    cadastrarProfessor();
                    break;
                case 4:
                    cadastrarAluno();
                    break;
                case 5:
                    matricularAlunoEmDisciplina();
                    break;
                case 6:
                    exibirInformacoesCurso();
                    break;
                case 7:
                    exibirInformacoesDisciplina();
                    break;
                case 8:
                    exibirInformacoesProfessor();
                    break;
                case 9:
                    exibirInformacoesAluno();
                    break;
                case 10:
                    sair = true;
                    System.out.println(getMensagem("saindo"));
                    break;
                default:
                    System.out.println(getMensagem("opcaoInvalida"));
            }
        }
    }

   
    public static void cadastrarCurso() {
        System.out.print(getMensagem("nomeCurso"));
        String nomeCurso = scanner.nextLine();
        cursos.put(nomeCurso, new Curso(nomeCurso));
        System.out.println(getMensagem("cursoCadastrado"));
    }

    public static void cadastrarDisciplina() {
        System.out.print(getMensagem("nomeDisciplina"));
        String nomeDisciplina = scanner.nextLine();
        disciplinas.put(nomeDisciplina, new Disciplina(nomeDisciplina));
        System.out.println(getMensagem("disciplinaCadastrada"));
    }

    public static void cadastrarProfessor() {
        System.out.print(getMensagem("nomeProfessor"));
        String nomeProfessor = scanner.nextLine();
        System.out.print(getMensagem("senhaProfessor"));
        String senhaProfessor = scanner.nextLine();
        professores.put(nomeProfessor, new Professor(nomeProfessor, senhaProfessor));
        System.out.println(getMensagem("professorCadastrado"));
    }

    public static void cadastrarAluno() {
        System.out.print(getMensagem("nomeAluno"));
        String nomeAluno = scanner.nextLine();
        System.out.print(getMensagem("senhaAluno"));
        String senhaAluno = scanner.nextLine();
        System.out.print(getMensagem("confirmarSenhaAluno"));
        String confirmarSenha = scanner.nextLine();
        
        if (!senhaAluno.equals(confirmarSenha)) {
            System.out.println(getMensagem("senhasNaoCorrespondem"));
            return;
        }
        
        System.out.print(getMensagem("nomeCursoAluno"));
        String nomeCurso = scanner.nextLine();
        Curso curso = cursos.get(nomeCurso);
        
        if (curso == null) {
            System.out.println(getMensagem("cursoNaoEncontrado"));
            return;
        }

        alunos.put(nomeAluno, new Aluno(nomeAluno, senhaAluno, curso));
        System.out.println(getMensagem("alunoCadastrado"));
    }

    public static void matricularAlunoEmDisciplina() {
        System.out.print(getMensagem("nomeAluno"));
        String nomeAluno = scanner.nextLine();
        System.out.print(getMensagem("nomeDisciplina"));
        String nomeDisciplina = scanner.nextLine();

        Aluno aluno = alunos.get(nomeAluno);
        Disciplina disciplina = disciplinas.get(nomeDisciplina);

        if (aluno != null && disciplina != null) {
            aluno.matricularDisciplina(disciplina);
            disciplina.adicionarAluno(aluno);
            System.out.println(getMensagem("alunoMatriculado"));
        } else {
            System.out.println(getMensagem("erroMatricula"));
        }
    }
 
    public static void exibirInformacoesCurso() {
        System.out.print(getMensagem("nomeCurso"));
        String nomeCurso = scanner.nextLine();
        Curso curso = cursos.get(nomeCurso);

        if (curso != null) {
            curso.listarDisciplinas();
        } else {
            System.out.println(getMensagem("cursoNaoEncontrado"));
        }
    }

    public static void exibirInformacoesDisciplina() {
        System.out.print(getMensagem("nomeDisciplina"));
        String nomeDisciplina = scanner.nextLine();
        Disciplina disciplina = disciplinas.get(nomeDisciplina);

        if (disciplina != null) {
            disciplina.obterInformacoes();
        } else {
            System.out.println(getMensagem("disciplinaNaoEncontrada"));
        }
    }

    public static void exibirInformacoesProfessor() {
        System.out.print(getMensagem("nomeProfessor"));
        String nomeProfessor = scanner.nextLine();
        Professor professor = professores.get(nomeProfessor);

        if (professor != null) {
            professor.obterInformacoes();
        } else {
            System.out.println(getMensagem("professorNaoEncontrado"));
        }
    }

    public static void exibirInformacoesAluno() {
        System.out.print(getMensagem("nomeAluno"));
        String nomeAluno = scanner.nextLine();
        Aluno aluno = alunos.get(nomeAluno);

        if (aluno != null) {
            aluno.obterInformacoes();
        } else {
            System.out.println(getMensagem("alunoNaoEncontrado"));
        }
    }

    public static String getMensagem(String chave) {
        switch (idioma) {
            case "pt":
                return switch (chave) {
                    case "escolhaOpcao" -> "Escolha uma opção: ";
                    case "nomeCurso" -> "Nome do curso: ";
                    case "cursoCadastrado" -> "Curso cadastrado com sucesso!";
                    case "nomeDisciplina" -> "Nome da disciplina: ";
                    case "disciplinaCadastrada" -> "Disciplina cadastrada com sucesso!";
                    case "nomeProfessor" -> "Nome do professor: ";
                    case "senhaProfessor" -> "Senha do professor: ";
                    case "professorCadastrado" -> "Professor cadastrado com sucesso!";
                    case "nomeAluno" -> "Nome do aluno: ";
                    case "senhaAluno" -> "Senha do aluno: ";
                    case "confirmarSenhaAluno" -> "Confirme a senha do aluno: ";
                    case "senhasNaoCorrespondem" -> "As senhas não correspondem!";
                    case "nomeCursoAluno" -> "Nome do curso do aluno: ";
                    case "cursoNaoEncontrado" -> "Curso não encontrado!";
                    case "alunoCadastrado" -> "Aluno cadastrado com sucesso!";
                    case "alunoMatriculado" -> "Aluno matriculado com sucesso!";
                    case "erroMatricula" -> "Erro ao matricular o aluno!";
                    case "disciplinaNaoEncontrada" -> "Disciplina não encontrada!";
                    case "saindo" -> "Saindo do sistema...";
                    case "opcaoInvalida" -> "Opção inválida!";
                    default -> "";
                };
            case "en":
                return switch (chave) {
                    case "escolhaOpcao" -> "Choose an option: ";
                    case "nomeCurso" -> "Course name: ";
                    case "cursoCadastrado" -> "Course registered successfully!";
                    case "nomeDisciplina" -> "Subject name: ";
                    case "disciplinaCadastrada" -> "Subject registered successfully!";
                    case "nomeProfessor" -> "Teacher name: ";
                    case "senhaProfessor" -> "Teacher password: ";
                    case "professorCadastrado" -> "Teacher registered successfully!";
                    case "nomeAluno" -> "Student name: ";
                    case "senhaAluno" -> "Student password: ";
                    case "confirmarSenhaAluno" -> "Confirm student password: ";
                    case "senhasNaoCorrespondem" -> "Passwords do not match!";
                    case "nomeCursoAluno" -> "Student's course name: ";
                    case "cursoNaoEncontrado" -> "Course not found!";
                    case "alunoCadastrado" -> "Student registered successfully!";
                    case "alunoMatriculado" -> "Student enrolled successfully!";
                    case "erroMatricula" -> "Error enrolling the student!";
                    case "disciplinaNaoEncontrada" -> "Subject not found!";
                    case "saindo" -> "Exiting the system...";
                    case "opcaoInvalida" -> "Invalid option!";
                    default -> "";
                };
            case "es":
                return switch (chave) {
                    case "escolhaOpcao" -> "Elige una opción: ";
                    case "nomeCurso" -> "Nombre del curso: ";
                    case "cursoCadastrado" -> "¡Curso registrado con éxito!";
                    case "nomeDisciplina" -> "Nombre de la asignatura: ";
                    case "disciplinaCadastrada" -> "¡Asignatura registrada con éxito!";
                    case "nomeProfessor" -> "Nombre del profesor: ";
                    case "senhaProfessor" -> "Contraseña del profesor: ";
                    case "professorCadastrado" -> "¡Profesor registrado con éxito!";
                    case "nomeAluno" -> "Nombre del alumno: ";
                    case "senhaAluno" -> "Contraseña del alumno: ";
                    case "confirmarSenhaAluno" -> "Confirme la contraseña del alumno: ";
                    case "senhasNaoCorrespondem" -> "¡Las contraseñas no coinciden!";
                    case "nomeCursoAluno" -> "Nombre del curso del alumno: ";
                    case "cursoNaoEncontrado" -> "¡Curso no encontrado!";
                    case "alunoCadastrado" -> "¡Alumno registrado con éxito!";
                    case "alunoMatriculado" -> "¡Alumno inscrito con éxito!";
                    case "erroMatricula" -> "¡Error al inscribir al alumno!";
                    case "disciplinaNaoEncontrada" -> "¡Asignatura no encontrada!";
                    case "saindo" -> "Saliendo del sistema...";
                    case "opcaoInvalida" -> "¡Opción inválida!";
                    default -> "";
                };
            case "fr":
                return switch (chave) {
                    case "escolhaOpcao" -> "Choisissez une option : ";
                    case "nomeCurso" -> "Nom du cours : ";
                    case "cursoCadastrado" -> "Cours enregistré avec succès !";
                    case "nomeDisciplina" -> "Nom de la discipline : ";
                    case "disciplinaCadastrada" -> "Discipline enregistrée avec succès !";
                    case "nomeProfessor" -> "Nom du professeur : ";
                    case "senhaProfessor" -> "Mot de passe du professeur : ";
                    case "professorCadastrado" -> "Professeur enregistré avec succès !";
                    case "nomeAluno" -> "Nom de l'élève : ";
                    case "senhaAluno" -> "Mot de passe de l'élève : ";
                    case "confirmarSenhaAluno" -> "Confirmez le mot de passe de l'élève : ";
                    case "senhasNaoCorrespondem" -> "Les mots de passe ne correspondent pas !";
                    case "nomeCursoAluno" -> "Nom du cours de l'élève : ";
                    case "cursoNaoEncontrado" -> "Cours non trouvé !";
                    case "alunoCadastrado" -> "Élève enregistré avec succès !";
                    case "alunoMatriculado" -> "Élève inscrit avec succès !";
                    case "erroMatricula" -> "Erreur lors de l'inscription de l'élève !";
                    case "disciplinaNaoEncontrada" -> "Discipline non trouvée !";
                    case "saindo" -> "Sortie du système...";
                    case "opcaoInvalida" -> "Option invalide !";
                    default -> "";
                };
            default:
                return "";
        }
    }

}
