public class Main {
    public static void main(String[] args) {
        // Primera parte
        int resultado;
        resultado = suma3(1, 2, 3);
        System.out.printf("Resultado de la suma es: %s\n", resultado);

        // Segunda parte
        Coche miCoche = new Coche();
        miCoche.incrementaPuerta();
        System.out.printf("El numero de puertas que tiene el coche es de %s", miCoche.puertas);

    }

    public static int suma3(int a, int b, int c) {
        return a + b + c;
    }
}