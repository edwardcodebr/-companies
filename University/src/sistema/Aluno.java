package sistema;

import java.util.ArrayList;
import java.util.List;

public class Aluno {
	private String nome;
    private String senha;
    private List<Disciplina> disciplinasMatriculadas;
    private Curso curso;

    public Aluno(String nome, String senha, Curso curso) {
        this.nome = nome;
        this.senha = senha;
        this.curso = curso;
        this.disciplinasMatriculadas = new ArrayList<>();
    }

    public String getNome() {
        return nome;
    }

    public String getSenha() {
        return senha;
    }

    public Curso getCurso() {
        return curso;
    }

    public void matricularDisciplina(Disciplina disciplina) {
        disciplinasMatriculadas.add(disciplina);
    }

    public void obterInformacoes() {
        System.out.println("Nome: " + nome);
        System.out.println("Curso: " + (curso != null ? curso.getNome() : "Nenhum curso matriculado"));
        System.out.println("Disciplinas Matriculadas:");
        for (Disciplina d : disciplinasMatriculadas) {
            System.out.println("- " + d.getNome());
        }
    }
}
