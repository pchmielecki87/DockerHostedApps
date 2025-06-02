public class HelloWorld {

    public static void main(final String[] args)
    {
        while (true) {
            try {
                System.out.println("Hello World");
                Thread.sleep(2000);
            }
            catch (Exception e) {
                break;
            }
        }
    }
}