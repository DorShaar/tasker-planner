# tasker-planner

## About
As part of my real work, I noticed that I need some small process that will ask me particular questions in order to have better plan for that task I'm going to work on. This is the reason for that project.

## How to run
You should have docker in order to run it without problems.\
Clone that repo into your computer and run the `docker-build.bat` (If you are a linux user just follow the commands inside, I build it for personal use so no need to handle all cases..). It will create docker image called tasker-planner with the your input version.\
After that you can run `docker-run.bat`, insert the version you would like to run and enjoy:\

## Usage
Main Menu:\
![alt text](https://github.com/DorShaar/tasker-planner/blob/main/images/main_menu.PNG "Main Menu")

Create new plan:\
![alt text](https://github.com/DorShaar/tasker-planner/blob/main/images/create_new_plan.PNG "Create new plan")

Show all plans:\
![alt text](https://github.com/DorShaar/tasker-planner/blob/main/images/show_all_plans.PNG "Show all plans")

With chosen plan:\
![alt text](https://github.com/DorShaar/tasker-planner/blob/main/images/with_chosen_plan.PNG "With chosen plan")

View plan information:\
![alt text](https://github.com/DorShaar/tasker-planner/blob/main/images/view_plan_information.PNG "View plan information")

## Development things I learned or used 
UTs - mock user's input and test according to it, used class mock.\
Exceptions - Catch exception and print it.\
Docker - Multi-stage builds, mount.\
OOO - Used private methods in python.\
