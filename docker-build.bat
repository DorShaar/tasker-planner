@echo off

echo last version:
docker images | grep tasker-planner | awk '{print $2}' | sort | tail -1

set /p id="Enter next version: "
docker build . -t tasker-planner:%id%