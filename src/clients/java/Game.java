

/**
 * Created by IntelliJ IDEA.
 * User: togelius
 * Date: //130912
 * Time: 17:22 PM
 */
public interface Game {

    public abstract GameState getCurrentState ();

    public GameState simulate (GameState startingState, Action action);

}
