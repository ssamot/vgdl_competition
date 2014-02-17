package ssamot;

import core.game.StateObservation;
import core.player.AbstractPlayer;
import ontology.Types;
import tools.Vector2d;

import java.util.ArrayList;
import java.util.Random;

/**
 * Created with IntelliJ IDEA.
 * User: ssamot
 * Date: 14/11/13
 * Time: 21:45
 * This is a Java port from Tom Schaul's VGDL - https://github.com/schaul/py-vgdl
 */
public class Agent extends AbstractPlayer {

    /**
     * Random generator for the agent.
     */
    private Random randomGenerator;


    /**
     * Public constructor with state observation and time due.
     */
    public Agent(StateObservation so, long timeDue)
    {
        randomGenerator = new Random();
    }


    /**
     * Picks an action. This function is called every game step to request an
     * action from the player.
     * @param stateObs Observation of the current state.
     * @param timeDue Time the action returned is due.
     * @return An action for the current state
     */
    public Types.ACTIONS act(StateObservation stateObs, long timeDue) {

        ArrayList<Vector2d>[] npcPositions = stateObs.getNPCPositions();
        ArrayList<Vector2d>[] fixedPositions = stateObs.getImmovablePositions();
        ArrayList<Vector2d>[] movingPositions = stateObs.getMovablePositions();
        ArrayList<Vector2d>[] resourcesPositions = stateObs.getResourcesPositions();
        ArrayList<Vector2d>[] portalPositions = stateObs.getPortalsPositions();

        long remaining = timeDue - System.currentTimeMillis();
        Types.ACTIONS action = null;
        StateObservation stCopy = stateObs.copy();

        int whenToFinish = 5;
        /*if(stateObs.getGameTick() == 30)
        {
            System.out.println(stateObs.getGameTick() + ": let's take a nap.");
            whenToFinish = -50;
        } */     //To force a disqualification.

        while(remaining > whenToFinish)
        {
            ArrayList<Types.ACTIONS> actions = stateObs.getAvailableActions();
            int index = randomGenerator.nextInt(actions.size());
            action = actions.get(index);

            stCopy.advance(action);
            if(stCopy.isGameOver())
            {
                //copying
                //System.out.println("copying");
                stCopy = stateObs.copy();
            }

            remaining = timeDue - System.currentTimeMillis();
            //if(remaining<5)
            //System.out.println(remaining);
        }

        //System.out.println("Action to execute: " + action);
        return action;
    }
}
