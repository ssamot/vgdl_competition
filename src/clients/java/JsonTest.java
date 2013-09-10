import com.eclipsesource.json.*;

import java.util.Iterator;

/**
 * Created by IntelliJ IDEA.
 * User: togelius
 * Date: //130910
 * Time: 17:47 PM
 */


public class JsonTest {


    public static String stateExample = "[\n" +
            "{\"type\":\"bomb\", \"x\":\"3\", \"y\":\"13\"}\n" +
            "]";

    public static void main(String[] args) {
        System.out.println(stateExample);
        JsonArray array = JsonArray.readFrom(stateExample);
        Iterator it = array.iterator();
        while (it.hasNext()) {
            JsonObject o = (JsonObject) it.next();

            System.out.println(o.names());
        }

    }

}
