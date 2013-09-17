zip -j working_python.zip ../../vgdl_competition/src/clients/python/client.py \
                       ../../vgdl_competition/src/clients/python/agent.py
python ../../vgdl_competition/src/server/game_executor.py  \
                         --game_levels examples.gridphysics.frogs,frog_level \
                         --n_times 1 --zip_name working_python.zip --agent_id 1 --run_id 1 --user_name test_user \
                         --tmp_dir /tmp --db_properties==../runtime/db.properties