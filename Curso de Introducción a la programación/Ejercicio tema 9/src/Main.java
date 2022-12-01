public class Main {
    public static void main(String[] args) {
        Cliente cliente = new Cliente();
        cliente.setEdad(40);
        cliente.setNombre("BEnjami");
        cliente.setTelefono("666555777");
        cliente.setCredito(2500);
        System.out.println("Cliente > Nombre: " + cliente.getNombre());
        System.out.println("Cliente > Edad: " + cliente.getEdad());
        System.out.println("Cliente > Telefono: " + cliente.getTelefono());
        System.out.println("Cliente > Credito: " + cliente.getCredito());

        Trabajador trabajador = new Trabajador();
        trabajador.setEdad(41);
        trabajador.setNombre("Benji");
        trabajador.setTelefono("777555666");
        trabajador.setSalario(1500.50);
        System.out.println("Trabajador > Nombre: " + trabajador.getNombre());
        System.out.println("Trabajador > Edad: " + trabajador.getEdad());
        System.out.println("Trabajador > Telefono: " + trabajador.getTelefono());
        System.out.println("Trabajador > Salario: " + trabajador.getSalario());

    }
}

class Persona {
    int edad;
    String nombre;
    String telefono;

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
}

class Cliente extends Persona{
    double credito;

    public double getCredito() {
        return credito;
    }

    public void setCredito(double credito) {
        this.credito = credito;
    }
}

class Trabajador extends Persona{
    double salario;

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }
}