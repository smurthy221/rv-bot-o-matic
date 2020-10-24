"""Python script for Bot-O-Matic Program"""
from os import truncate
import time
import json

#Specifying Robot types in 'Type' set. Will be used frequently
Type = {
    'Unipedal', 'Bipedal', 'Quadrupedal', 'Arachnid',  'Radial', 'Aeronautical'
}

def TypeError():
    print("TypeError, please check spelling on input")
    exit(1)

class Robot:
    """Robot object Class"""
    def __init__(self, name, hasTask, rob_type):
        """Robot Constructor"""
        self.name = name
        self.hasTask = hasTask
        self.tasks_done = 0
        #if type passed in is not in the Type set, exit(1)
        if rob_type in Type:
            self.type = rob_type
        else:
            TypeError()

    #if given a task, the robot will do it in this time
    def giveTask(self,task_name, eta):
        """Assigning robot a task"""
        #if not already assigned a task
        if not self.hasTask:
            #assign the robot the task and print when it finishes
            self.hasTask = True
            print (self.name + " doing " + task_name)
            print ("...") 
            time.sleep(eta*.001) #gives the delay until the task is finished
            print (self.name + " finished " + task_name + "\n")

            #increment number of tasks completed and free up opportunity to do task
            self.tasks_done = self.tasks_done + 1
            self.hasTask = False

def addTask(task_description, task_eta):
    """Adding task to the existing JSON"""
    #first read in existing json
    json_file = []
    with open("tasks.json") as existing_json:
        json_file = json.load(existing_json)

    #define the task we want to accomplish
    task = {
        "description":str(task_description),
        "eta": int(task_eta)
    }
    #add to the new task
    json_file.append(task)

    #write the new json object with appended taks to the tasks.json file
    new_json = open("tasks.json", "w")
    json.dump(json_file, new_json, indent=4)

def robot_adding_loop(robot_name, robot_array):
    """For adding robot functionality"""
    #entering name
    robot_type = input("Enter " + robot_name + " type (enter 'help' for list of robot types): ")
    #if user does not enter 'help', create Robot object and add to passed in array
    if robot_type != "help" and robot_type != "Help":
        robot = Robot(robot_name,False,robot_type)
        robot_array.append(robot)
        return robot_array #returing array to ensure passed in array is edited
    #otherwise print out robot types and recursively call robot_adding_loop
    else:
        print("Robot Types = Unipedal, Bipedal, Quadrupedal, Arachnid,  Radial, Aeronautical")
        robot_adding_loop(robot_name,robot_array) #recursive call helps ensure that 'help' can be called infinite number of times



def main():
    #holds all robots user requests
    robot_array = []

    #indicates if execution has been run
    submitted = False

    #while the simaulation has not been executed
    while not submitted:
        #takes in input for if user would like to add tasks, robots, 'help' option, or exevut simulation
        option = input("Would you like to add tasks, add robots, or run the sim? (enter 'help' for options to press): ")
        #if they press the help option, print out options avaliable for them
        if option == "help":
            print("Options: 'run' to execute tasks, 'add tasks' to add more tasks, 'add robots' to add more robots")
        #if they look to add tasks
        elif option == "add tasks":
            #take in the number of tasks they look to add
            num_tasks = input("How many tasks would you like to add?: ")
            #for each new task they look to add
            count = 0
            while count < int(num_tasks):
                #take in the task name
                task_name = input("enter task " + str(count+1) + " name: ")
                #take in task time in seconds
                task_time = input("enter task " + str(count+1) + " time (in seconds): ")
                #add task to the tasks.json file and increment count
                addTask(task_name, int(task_time))
                count+=1
        #if they look to add robots
        elif option == "add robots":
            #take in the number they look to add
            num_robots = input("How many robots would you like to add?: ")
            #for each new robot they look to add
            count = 0
            while count < int(num_robots):
                #take in robot name
                robot_name = input("Enter robot " + str(count+1) + " name: ")
                #append the new robot created to the robot_array and reassign it
                robot_array = robot_adding_loop(robot_name,robot_array)
                count+=1
        #if they run the simulation
        elif option == "run":
            #instantiate data list to hold json data
            data = []
            #open tasks.json and load into data array
            with open("tasks.json") as t:
                data = json.load(t);

            #assign first 5 tasks each robot in array to complete
            for robot in robot_array:
                while len(data)!=0 and robot.tasks_done < 5:
                    robot.giveTask(data[0]["description"],float(data[0]["eta"]))
                    data.pop(0)
                #once all robots 5 tasks are complete
                print(robot.name + " finished doing their tasks!\n")
            #helps end the loop
            submitted = True
        #if error to the input
        else:
            TypeError()

if "__main__":
    main()