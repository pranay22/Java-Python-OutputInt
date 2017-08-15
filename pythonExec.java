import java.util.Scanner;
import java.io.*;

public class pythonExec {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter Python Arg a: ");
		String var_a = scanner.next();
		System.out.print("Enter Python Arg b: ");
		String var_b = scanner.next();
		System.out.print("Enter Python Arg c: ");
		String var_c = scanner.next();

		System.out.println("Entered variables are:");
		System.out.println("a->" +var_a);
		System.out.println("b->" +var_b);
		System.out.println("c->" +var_c);
		try{
			Process p = Runtime.getRuntime().exec("python test.py -a "+var_a+" -b "+var_b+" -c "+var_c);
			BufferedReader bfr = new BufferedReader(new InputStreamReader(p.getInputStream()));
			String line = "";
			while((line = bfr.readLine()) != null) {
			// display each output line form python script
			System.out.println(line);
			}
		}
		catch(Exception e){
			System.out.println(e);
		}
	}
}
