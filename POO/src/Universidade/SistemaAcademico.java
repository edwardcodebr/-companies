package Universidade;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.*;
public class SistemaAcademico {
    private ArrayList<Estudante> estudantes;
    private ArrayList<Professor> professores;
    private ArrayList<Curso> cursos;
    private ArrayList<Livro> livros;
    private ArrayList<Emprestimo> emprestimos;

    public SistemaAcademico() {
        estudantes = new ArrayList<>();
        professores = new ArrayList<>();
        cursos = new ArrayList<>();
        livros = new ArrayList<>();
        emprestimos = new ArrayList<>();
    }

    public void cadastrarEstudante(Estudante estudante) {
        estudantes.add(estudante);
    }

    public void cadastrarProfessor(Professor professor) {
        professores.add(professor);
    }

    public void cadastrarCurso(Curso curso) {
        cursos.add(curso);
    }

    public void cadastrarLivro(Livro livro) {
        livros.add(livro);
    }

    public void realizarEmprestimo(Estudante estudante, Livro livro) {
        if (livro.isDisponivel()) {
            Emprestimo emprestimo = new Emprestimo(estudante, livro);
            emprestimos.add(emprestimo);
        } else {
            System.out.println("Livro não disponível para empréstimo.");
        }
    }

    public void exibirRelatorio() {
        System.out.println("\n--- Relatório de Estudantes ---");
        for (Estudante e : estudantes) {
            e.exibirInfo();
            System.out.println();
        }

        System.out.println("\n--- Relatório de Professores ---");
        for (Professor p : professores) {
            p.exibirInfo();
            System.out.println();
        }

        System.out.println("\n--- Relatório de Cursos ---");
        for (Curso c : cursos) {
            c.exibirInfo();
            System.out.println();
        }

        System.out.println("\n--- Relatório de Livros ---");
        for (Livro l : livros) {
            l.exibirInfo();
            System.out.println();
        }

        System.out.println("\n--- Relatório de Empréstimos ---");
        for (Emprestimo em : emprestimos) {
            em.exibirInfo();
            System.out.println();
        }
    }

    public static void main(String[] args) {
        SistemaAcademico sistema = new SistemaAcademico();
        Scanner scanner = new Scanner(System.in);

        boolean continuar = true;

        while (continuar) {
            try {
                System.out.println("\n--- Menu ---");
                System.out.println("1. Cadastrar Estudante");
                System.out.println("2. Cadastrar Professor");
                System.out.println("3. Cadastrar Curso");
                System.out.println("4. Cadastrar Livro");
                System.out.println("5. Realizar Empréstimo");
                System.out.println("6. Exibir Relatório");
                System.out.println("7. Sair");
                System.out.print("Escolha uma opção: ");
                int opcao = scanner.nextInt();
                scanner.nextLine(); // Limpa o buffer

                switch (opcao) {
                    case 1 -> {
                        System.out.print("Nome do Estudante: ");
                        String nome = scanner.nextLine();
                        System.out.print("CPF: ");
                        String cpf = scanner.nextLine();
                        System.out.print("Data de Nascimento: ");
                        String dataNascimento = scanner.nextLine();
                        System.out.print("Matrícula: ");
                        String matricula = scanner.nextLine();
                        Estudante estudante = new Estudante(nome, cpf, dataNascimento, matricula);

                        System.out.println("Adicione disciplinas (digite 'fim' para terminar):");
                        while (true) {
                            System.out.print("Disciplina: ");
                            String disciplina = scanner.nextLine();
                            if (disciplina.equalsIgnoreCase("fim")) break;
                            estudante.adicionarDisciplina(disciplina);
                        }

                        sistema.cadastrarEstudante(estudante);
                        System.out.println("Estudante cadastrado com sucesso!");
                    }
                    case 2 -> {
                        System.out.print("Nome do Professor: ");
                        String nome = scanner.nextLine();
                        System.out.print("CPF: ");
                        String cpf = scanner.nextLine();
                        System.out.print("Data de Nascimento: ");
                        String dataNascimento = scanner.nextLine();
                        System.out.print("Especialização: ");
                        String especializacao = scanner.nextLine();
                        Professor professor = new Professor(nome, cpf, dataNascimento, especializacao);

                        System.out.println("Adicione disciplinas (digite 'fim' para terminar):");
                        while (true) {
                            System.out.print("Disciplina: ");
                            String disciplina = scanner.nextLine();
                            if (disciplina.equalsIgnoreCase("fim")) break;
                            professor.adicionarDisciplina(disciplina);
                        }

                        sistema.cadastrarProfessor(professor);
                        System.out.println("Professor cadastrado com sucesso!");
                    }
                    case 3 -> {
                        System.out.print("Nome do Curso: ");
                        String nome = scanner.nextLine();
                        Curso curso = new Curso(nome);

                        System.out.println("Adicione disciplinas (digite 'fim' para terminar):");
                        while (true) {
                            System.out.print("Disciplina: ");
                            String disciplina = scanner.nextLine();
                            if (disciplina.equalsIgnoreCase("fim")) break;
                            curso.adicionarDisciplina(disciplina);
                        }

                        sistema.cadastrarCurso(curso);
                        System.out.println("Curso cadastrado com sucesso!");
                    }
                    case 4 -> {
                        System.out.print("Título do Livro: ");
                        String titulo = scanner.nextLine();
                        System.out.print("Autor: ");
                        String autor = scanner.nextLine();
                        System.out.print("ISBN: ");
                        String isbn = scanner.nextLine();
                        Livro livro = new Livro(titulo, autor, isbn);
                        sistema.cadastrarLivro(livro);
                        System.out.println("Livro cadastrado com sucesso!");
                    }
                    case 5 -> {
                        System.out.print("Nome do Estudante: ");
                        String nomeEstudante = scanner.nextLine();
                        Estudante estudante = sistema.estudantes.stream()
                                .filter(e -> e.getNome().equalsIgnoreCase(nomeEstudante))
                                .findFirst()
                                .orElse(null);

                        if (estudante == null) {
                            System.out.println("Estudante não encontrado.");
                            break;
                        }

                        System.out.print("Título do Livro: ");
                        String tituloLivro = scanner.nextLine();
                        Livro livro = sistema.livros.stream()
                                .filter(l -> l.getTitulo().equalsIgnoreCase(tituloLivro))
                                .findFirst()
                                .orElse(null);

                        if (livro == null) {
                            System.out.println("Livro não encontrado.");
                            break;
                        }

                        sistema.realizarEmprestimo(estudante, livro);
                        System.out.println("Empréstimo realizado com sucesso!");
                    }
                    case 6 -> sistema.exibirRelatorio();
                    case 7 -> {
                        continuar = false;
                        System.out.println("Saindo...");
                    }
                    default -> System.out.println("Opção inválida.");
                }
            } catch (InputMismatchException e) {
                System.out.println("Entrada inválida. Tente novamente.");
                scanner.nextLine(); // Limpa o buffer
            }
        }
        scanner.close();
    }
}

