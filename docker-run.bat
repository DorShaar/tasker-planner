@echo off

echo all versions:
docker images | grep tasker-planner | awk '{print $2}' | sort

set /p id="Enter version to run: "
set /p local_database_path="Enter local database path: "
docker run -it -v "%local_database_path%":/app/data tasker-planner:%id%
