import Pessoa.Pessoa;

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        File arq = new File("arq");
        Object pessoa = new Pessoa("ian", 25);

        ObjectOutputStream objOutput = new ObjectOutputStream(new FileOutputStream(arq));
        objOutput.writeObject(pessoa);
        objOutput.close();

        ObjectInputStream objInput = new ObjectInputStream(new FileInputStream(arq));
        pessoa = objInput.readObject();
        objInput.close();

    }
}
