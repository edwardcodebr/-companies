package Universidade;

public class Emprestimo {
    private Estudante estudante;
    private Livro livro;

    public Emprestimo(Estudante estudante, Livro livro) {
        this.estudante = estudante;
        this.livro = livro;
        livro.setDisponivel(false);
    }

    public void exibirInfo() {
        System.out.println("Estudante: " + estudante.getNome());
        System.out.println("Livro: " + livro.getTitulo());
    }
}
