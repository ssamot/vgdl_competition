package ssamot;

import core.game.StateObservation;
import core.player.AbstractPlayer;
import ontology.Types;

import java.util.Random;

/**
 * Created with IntelliJ IDEA.
 * User: ssamot
 * Date: 14/11/13
 * Time: 21:45
 * This is a Java port from Tom Schaul's VGDL - https://github.com/schaul/py-vgdl
 */
public class Agent extends AbstractPlayer {
    private Random randomGenerator = new Random();



    public Types.ACTIONS act(StateObservation stateObs, long timeDue) {

        long remaining = timeDue - System.currentTimeMillis();
        Types.ACTIONS action = null;
        StateObservation stCopy = stateObs.copy();

        while(remaining > 1)
        {
            int index = randomGenerator.nextInt(actions.size());
            action = actions.get(index);

            stCopy.advance(action);
            if(stCopy.isEnded)
                stCopy = stateObs.copy();

            remaining = timeDue - System.currentTimeMillis();
        }

        return action;
    }
}
