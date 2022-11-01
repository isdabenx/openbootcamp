public class Main {
    public static void main(String[] args) {
        int numeroIf = -1;
        if (numeroIf < 0) {
            System.out.println("Numero negativo");
        } else if (numeroIf > 0) {
            System.out.println("Numero positivo");
        } else {
            System.out.println("Es un 0");
        }

        int numeroWhile = 0;
        while (numeroWhile < 3) {
            numeroWhile++;
            System.out.println("Se ha ejecutado " + numeroWhile + " veces.");
        }

        do {
            numeroWhile++;
            System.out.println("Se ha ejecutado una " + numeroWhile + " vez extra.");
        } while (numeroWhile < 3);

        for (int numeroFor = 0; numeroFor <= 3; numeroFor++) {
            System.out.println("numeroFor = " + numeroFor);
        }

        String estacion = "verano";
        switch (estacion) {
            case "verano" -> System.out.println("Es verano y hace calor");
            case "otoño" -> System.out.println("Es otoño!");
            case "invierno" -> System.out.println("Que frio en invierno!");
            case "primavera" -> System.out.println("No se que tipo de ropa ponerme en primavera, frio o calor");
            default -> System.out.println("No es ninguna estacion");
        }
    }
}