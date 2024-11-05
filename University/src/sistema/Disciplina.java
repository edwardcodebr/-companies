package sistema;

import java.util.ArrayList;
import java.util.List;

public class Disciplina {
	private String nome;
    private List<Aluno> alunosMatriculados;

    public Disciplina(String nome) {
        this.nome = nome;
        this.alunosMatriculados = new ArrayList<>();
    }

    public String getNome() {
        return nome;
    }

    public void adicionarAluno(Aluno aluno) {
        alunosMatriculados.add(aluno);
    }

    public void obterInformacoes() {
        System.out.println("Nome da Disciplina: " + nome);
        System.out.println("Alunos Matriculados:");
        for (Aluno a : alunosMatriculados) {
            System.out.println("- " + a.getNome());
        }
    }
}