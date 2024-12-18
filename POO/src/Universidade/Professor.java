package Universidade;

import java.util.ArrayList;

public class Professor extends Pessoa {
    private String especializacao;
    private ArrayList<String> disciplinas;

    public Professor(String nome, String cpf, String dataNascimento, String especializacao) {
        super(nome, cpf, dataNascimento);
        this.especializacao = especializacao;
        this.disciplinas = new ArrayList<>();
    }

    public void adicionarDisciplina(String disciplina) {
        disciplinas.add(disciplina);
    }

    public void exibirInfo() {
        super.exibirInfo();
        System.out.println("Especialização: " + especializacao);
        System.out.println("Disciplinas: " + String.join(", ", disciplinas));
    }
}
