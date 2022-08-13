import Pessoa.Pessoa;

public class Main {
    public static void main(String[] args) {
        Pessoa ian = new Pessoa("ian");
        Pessoa marcos = new Pessoa("marcos");
        Pessoa gustavo = new Pessoa("gustavo");
        System.out.println(Pessoa.totalPessoas);
        System.out.println(ian.totalPessoas);
        System.out.println(ian.nome);
    }
}
