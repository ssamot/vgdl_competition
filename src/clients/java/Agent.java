

/**
 * Created by IntelliJ IDEA.
 * User: togelius
 * Date: //130912
 * Time: 17:13 PM
 */
public interface Agent {

    public abstract void initNewGame (Game game);

    public abstract Action takeAction (Game game);

}
