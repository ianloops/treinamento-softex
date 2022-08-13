import Pessoa.Pessoa;

public class Main {
    public static void main(String[] args) {
        Pessoa ian = new Pessoa("ian", 25);
        Pessoa marcos = new Pessoa("marcos", 33);
        Pessoa gustavo = new Pessoa("gustavo", 40);
        System.out.println(Pessoa.getTotalPessoas());
        System.out.println(ian.getIdade());
        System.out.println(ian.getNome());
    }
}
