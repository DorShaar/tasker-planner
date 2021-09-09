@echo off

echo all versions:
docker images | grep tasker-planner | awk '{print $2}' | sort

set /p id="Enter version to run: "
docker run -it -v /c/Dor/Apps/TaskerPlanner:/app/plan/ tasker-planner:%id%