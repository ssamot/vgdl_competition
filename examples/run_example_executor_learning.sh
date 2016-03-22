current_dir=`pwd`
echo $current_dir

cd ../../vgdl_competition/src/clients/python_learning/
zip -r $current_dir/dummy_python_learning.zip .
cd $current_dir

#examples.gridphysics.frogs, frog_level

USER_NAME="ssamot"
GAME="frogs.txt"
LEVEL="frogs_lvl0.txt"
VGDL_JAR="/home/ssamot/projects/vgdl/gvgai/dist/gvgai.jar"
GAMES_DIR="/home/ssamot/projects/vgdl/gvgai/examples/gridphysics/"

#GAME="examples.gridphysics.chase"
#LEVEL="chase_level"


#GAME="examples.gridphysics.pacman"
#LEVEL="pacman_level"

echo $LEVEL

#kernprof.py -l -v ../../vgdl_competition/src/server/game_executor.py  \
#                         --game_levels $GAME,$LEVEL \
#                         --n_times 1 --zip_name working_python.zip --agent_id 2 --run_id 100 --user_name ssamot \
#                         --tmp_dir /tmp --db_properties ../runtime/system.properties

python ../../vgdl_competition/src/server/game_executor_learning.py  \
                         --game_levels $GAME,$LEVEL \
                         --n_times 1 --zip_name dummy_python_learning.zip --agent_id 2 --run_id 300 --user_name $USER_NAME \
                         --tmp_dir /tmp --db_properties ../runtime/system.properties \
                         --vgdl_jar $VGDL_JAR --game_dir $GAMES_DIR

#python ../../vgdl_competition/src/server/game_executor.py  \
#                         --game_levels examples.gridphysics.frogs,frog_level \
#                         --n_times 1 --zip_name working_python.zip --agent_id 2 --run_id 1 --user_name test_user \
#                         --tmp_dir /tmp --db_properties==../runtime/db.properties


#python ../../vgdl_competition/src/server/game_executor.py  \
#                         --game_levels 1,1 \
#                         --n_times 1 --zip_name working_python.zip --agent_id 2 --run_id 100 --user_name ssamot \
#                         --tmp_dir /tmp --db_properties ../runtime/system.properties --upload