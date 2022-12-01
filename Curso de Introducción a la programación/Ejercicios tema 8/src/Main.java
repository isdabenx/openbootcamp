public class Main {
    public static void main(String[] args) {

        Persona persona = new Persona();
        persona.setEdad(40);
        persona.setNombre("Benjami");
        persona.setTelefono("666555666");

        System.out.println("Nombre: " + persona.getNombre());
        System.out.println("Edad: " + persona.getEdad());
        System.out.println("Telefono: " + persona.getTelefono());
    }
}

