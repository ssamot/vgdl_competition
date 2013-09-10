


import java.io.BufferedReader;
import java.io.InputStreamReader;
import com.eclipsesource.json.*;


/**
 * Created by IntelliJ IDEA.
 * User: togelius
 * Date: //130910
 * Time: 14:19 PM
 */
public class Agent {

    public static void main(String[] args) throws Exception {
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        while (true) {
            String in = br.readLine();

            System.out.println("Handfish");
            System.err.println("Handfish" + in.charAt(0));
        }
    }

}
