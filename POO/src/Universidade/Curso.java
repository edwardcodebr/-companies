package Universidade;

import java.util.ArrayList;
import java.util.Scanner;

public class Curso {
    private String nome;
    private ArrayList<String> disciplinas;

    public Curso(String nome) {
        this.nome = nome;
        this.disciplinas = new ArrayList<>();
    }

    public void adicionarDisciplina(String disciplina) {
        disciplinas.add(disciplina);
    }

    public void exibirInfo() {
        System.out.println("Curso: " + nome);
        System.out.println("Disciplinas: " + disciplinas);
    }
}
