package Pessoa;

public class Pessoa {
        public static int totalPessoas;
        public String nome;

    public Pessoa(String nome) {
        this.nome=nome;
        totalPessoas++;
    }
}

