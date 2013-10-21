zip -j working_python.zip ../../vgdl_competition/src/clients/python/client.py \
                       ../../vgdl_competition/src/clients/python/agent.py \
                       ../../vgdl_competition/src/clients/python/mcts_agent.py

#examples.gridphysics.frogs, frog_level

GAME="examples.gridphysics.frogs"
LEVEL="frog_level"

#GAME="examples.gridphysics.chase"
#LEVEL="chase_level"


#GAME="examples.gridphysics.pacman"
#LEVEL="pacman_level"

echo $LEVEL

#kernprof.py -l -v ../../vgdl_competition/src/server/game_executor.py  \
#                         --game_levels $GAME,$LEVEL \
#                         --n_times 1 --zip_name working_python.zip --agent_id 2 --run_id 100 --user_name ssamot \
#                         --tmp_dir /tmp --db_properties ../runtime/system.properties

python ../../vgdl_competition/src/server/game_executor.py  \
                         --game_levels $GAME,$LEVEL \
                         --n_times 1 --zip_name working_python.zip --agent_id 2 --run_id 100 --user_name ssamot \
                         --tmp_dir /tmp --db_properties ../runtime/system.properties

#python ../../vgdl_competition/src/server/game_executor.py  \
#                         --game_levels examples.gridphysics.frogs,frog_level \
#                         --n_times 1 --zip_name working_python.zip --agent_id 2 --run_id 1 --user_name test_user \
#                         --tmp_dir /tmp --db_properties==../runtime/db.properties


#python ../../vgdl_competition/src/server/game_executor.py  \
#                         --game_levels 1,1 \
#                         --n_times 1 --zip_name working_python.zip --agent_id 2 --run_id 100 --user_name ssamot \
#                         --tmp_dir /tmp --db_properties ../runtime/system.properties --upload