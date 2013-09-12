/**
 * Created by IntelliJ IDEA.
 * User: togelius
 * Date: //130912
 * Time: 18:00 PM
 */
public class RandomAgent implements Agent {


    public void initNewGame(Game game) {
        // do nothing
    }

    public Action takeAction(Game game) {
        Action.Movement move = Action.Movement.values()[(int) (Math.random() * Action.Movement.values().length)];
        return new Action(move, Math.random() < 0.5);
    }
}
