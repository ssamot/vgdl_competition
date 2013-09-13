
/**
 * Created by IntelliJ IDEA.
 * User: togelius
 * Date: //130912
 * Time: 17:24 PM
 */
public class Action {

    public enum Movement {up, right, down, left}

    public Movement move;

    public boolean fire;

    public Action (Movement move, boolean fire) {
        this.move = move;
        this.fire = fire;
    }
}
