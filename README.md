# RV-Bot-O-Matic

## I. Introduction
This program simulates robots finishing up household tasks with a task description and estimated time until finish. It keeps track of tasks through the tasks.json file, which will update as users complete and add different tasks to do.

## II. Running the Bot-O-Matic
### Prerequesites:
All users will need to install python3 package. More information about installation [here](https://realpython.com/installing-python/)
### Command Line Usage:
```
python3 robot.py
```

## III. Bot-O-Matic Details
### Program Format
The Bot-O-Matic script runs similar to a Python command line interface. There is a command line which will take in input and user commands that we will detail below. Below is an example command line that will be used to take in user input.
```
>>
```

### Commands
The master list of commands is listed below:<br/>
- 'run' : will execute simulation of robots completing tasks
- 'add tasks' : will add extra tasks for the robots to complete
- 'add robots' : will add extra robots to the running program
- 'view tasks' : will list all tasks remaining for robots to complete
- 'view robots' : will display all existing robots created
- 'delete robots' : will delete any robots running in the program
- 'leaderboard' : will display the robots who have completed the most tasks in descending order
- 'exit' : will exit the module

More information about each command is listed below.

### run
By entering this command, the program will execute the simulation and remove tasks from the list (as indentified in tasks.json). These tasks will take a variable amount of time defined in the tasks.json file in 'eta'.<br/>
```
>> run
(robot name here) doing (task here)
...
```
When removing tasks from the list, it will also update the tasks.json file and remove tasks that have been completed.

### add tasks
The add tasks command will take in user input and append the respective tasks the user supplies to the tasks.json file.
```
>> add tasks
How many tasks would you like to add?: (user input here)
enter task 1 name: (user input here)
enter task 1 time (in seconds): (user input here)
...
```
### add robots
The add robots command will take in user input and add the robots to a master list kept during each interface session. <br/>
Each robot has a specific type and eahc type can do a limited amount of tasks, depending on eta.
The types are: 'Unipedal', 'Bipedal', 'Quadrupedal', 'Arachnid',  'Radial', 'Aeronautical'
```
>> add robots
How many robots would you like to add?: (user input here)
Enter robot 1 name: (robot 1 name)
Enter (robot 1 name) type  (enter 'help' for list of robot types): (robot 1 type)
...
```
If you press the 'help' option:
```
>> add robots
...
Enter (robot 1 name) type  (enter 'help' for list of robot types): help
Robot Types = Unipedal, Bipedal, Quadrupedal, Arachnid,  Radial, Aeronautical
Enter (robot 1 name) type  (enter 'help' for list of robot types):
```

### view tasks
This command will print all of the pending tasks from the tasks.json file.
```
>> view tasks
        {'description': 'mow the lawn', 'eta': 20000}
        {'description': 'rake the leaves', 'eta': 18000}
        ...
```

### view robots
This command will display all created robots in order of when they were created.
```
>> view robots
------------------------------------------------
Robot Name: (name here)
Robot ID: 0
Robot Type: (type here)
Robot Tasks Completed: 0
------------------------------------------------
...
```

### delete robots
'delete robots will delete robots by ID number. You can find the ID number easily with the 'view robots' command.
```
>> delete robots
What robot would you like to delete? (please enter their ID): [index]
Deleted Robot #[index]
```

### leaderboard
The leaderboard command will show the robots leaderboard, with the robot completing the most tasks at the top and descending from there.
```
>> leaderboard
LEADERBOARD:
Rank 1: [Robot x] with 3 tasks done!
Rank 2: [Robot z] with 2 tasks done!
Rank 3: [Robot w] with 2 tasks done!
...
```

### exit
Will exit the command line interface
```
>> exit
$
```


