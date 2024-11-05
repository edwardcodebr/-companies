package sistema;


public class Professor {
	 private String nome;
	    private String senha;

	    public Professor(String nome, String senha) {
	        this.nome = nome;
	        this.senha = senha;
	    }

	    public String getNome() {
	        return nome;
	    }

	    public String getSenha() {
	        return senha;
	    }

	    public void obterInformacoes() {
	        System.out.println("Nome do Professor: " + nome);
	    }
}

