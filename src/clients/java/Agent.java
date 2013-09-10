

import javax.xml.stream.util.StreamReaderDelegate;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.Reader;
import java.nio.Buffer;

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
        //for (String in = br.readLine();in!=null;) {
        while(true) {
            String in = br.readLine();
            if(in ==null) {
                break;
            }
            System.out.println("HandfishEND_COMMAND");
            //System.err.println(in  + "test");
            System.err.println("Handfish" + in.charAt(0));
        }
    }

}
