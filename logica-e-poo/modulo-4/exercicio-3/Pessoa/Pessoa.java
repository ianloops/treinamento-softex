package Pessoa;

public class Pessoa {
        public static int totalPessoas;
        public String nome;
        public int idade;

    public static int getTotalPessoas() {
        return totalPessoas;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public Pessoa(String nome, int idade) {
        this.nome=nome;
        this.idade=idade;
        totalPessoas++;
    }
}

