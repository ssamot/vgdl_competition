current_dir=`pwd`
echo $current_dir

cd ../../vgdl_competition/src/clients/java/
zip -r $current_dir/working_java.zip .
cd $current_dir

#examples.gridphysics.frogs, frog_level

USER_NAME="ssamot"
GAME="/home/ssamot/projects/vgdl/java-vgdl/examples/gridphysics/frogs.txt"
LEVEL="/home/ssamot/projects/vgdl/java-vgdl/examples/gridphysics/frogs_lvl0.txt"
VGDL_JAR="/home/ssamot/projects/vgdl/java-vgdl/build/dist/vgdl.jar"

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
                         --n_times 1 --zip_name working_java.zip --agent_id 2 --run_id 200 --user_name $USER_NAME \
                         --tmp_dir /tmp --db_properties ../runtime/system.properties \
                         --vgdl_jar $VGDL_JAR

#python ../../vgdl_competition/src/server/game_executor.py  \
#                         --game_levels examples.gridphysics.frogs,frog_level \
#                         --n_times 1 --zip_name working_python.zip --agent_id 2 --run_id 1 --user_name test_user \
#                         --tmp_dir /tmp --db_properties==../runtime/db.properties


#python ../../vgdl_competition/src/server/game_executor.py  \
#                         --game_levels 1,1 \
#                         --n_times 1 --zip_name working_python.zip --agent_id 2 --run_id 100 --user_name ssamot \
#                         --tmp_dir /tmp --db_properties ../runtime/system.properties --upload