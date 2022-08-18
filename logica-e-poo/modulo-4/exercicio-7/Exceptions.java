public class Exceptions {
	public static void main (String[] args) {

		try {
			
		     String frase=null;
		     frase = frase.toUpperCase();
		     System.out.println(frase);

		} catch (Exception e) {

		     System.out.println("Ocorreu o erro: " + e.getMessage());

		}

	System.out.println("Fim");

	}
}
