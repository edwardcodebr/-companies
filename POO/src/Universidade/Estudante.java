package Universidade;

import java.util.ArrayList;
import java.util.Scanner;
public class Estudante extends Pessoa {
    private String matricula;
    private ArrayList<String> disciplinas;

    public Estudante(String nome, String cpf, String dataNascimento, String matricula) {
        super(nome, cpf, dataNascimento);
        this.matricula = matricula;
        this.disciplinas = new ArrayList<>();
    }

    public void adicionarDisciplina(String disciplina) {
        disciplinas.add(disciplina);
    }

    public void exibirInfo() {
        super.exibirInfo();
        System.out.println("Matrícula: " + matricula);
        System.out.println("Disciplinas: " + String.join(", ", disciplinas));
    }
}
