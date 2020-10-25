"""Python script for Bot-O-Matic Program"""
<<<<<<< HEAD
from os import truncate
=======
>>>>>>> cl-interface
import time
import json

#Specifying Robot types in 'Type' set. Will be used frequently
Type = {
    'Unipedal', 'Bipedal', 'Quadrupedal', 'Arachnid',  'Radial', 'Aeronautical'
}

<<<<<<< HEAD
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
=======
#the master data structure for the robots in the simulation
robot_array = []

def CanComplete(robot_type, eta):
    """Defining task criteria for each type of Robot"""
    #Unipedal can only do a task if eta = (0,inifinity)
    if robot_type == "Unipedal":
        if eta > 0:
            return True
        else:
            return False
    #Bipedal can only do a task if eta = (1200,20000)
    elif robot_type == "Bipedal": 
        if eta > 1200 and eta < 20000:
            return True
        else:
            return False
    #Quadrupedal can only do a task if eta = (500,25000)
    elif robot_type == "Quadrupedal": 
        if eta > 500 and eta < 25000:
            return True
        else:
            return False 
    #Arachnid can only do a task if eta = (0,10000)
    elif robot_type == "Arachnid": 
        if eta > 0 and eta < 10000:
            return True
        else:
            return False
    #Radial can only do a task if eta = (1200,20000)
    elif robot_type == "Radial": 
        if eta > 1000 and eta < 30000:
            return True
        else:
            return False
    #Aeronautical can only do a task if eta = (5000,100000)
    elif robot_type == "Aeronautical": 
        if eta > 5000 and eta < 100000:
            return True
        else:
            return False

class Robot:
    """Robot object Class"""
    def __init__(self, name, rob_type, ID):
        """Robot Constructor"""
        #if type passed in is in the Type set, initialize the object
        if rob_type in Type:
            self.uniqID = ID
            self.type = rob_type
            self.name = name
            self.tasks_done = 0
        #if type passed in is not in the Type set, dont initialize the object
        else:
            print("Please check spelling on input")

    def giveTask(self,task_name, eta):
        """Assigning robot a task"""
        #assign the robot the task and print when it finishes
        print (self.name + " doing " + task_name)
        print ("...") 
        time.sleep(eta*.001) #gives the delay until the task is finished
        print (self.name + " finished " + task_name + "\n")

        #increment number of tasks completed and free up opportunity to do task
        self.tasks_done = self.tasks_done + 1
>>>>>>> cl-interface

def addTask(task_description, task_eta):
    """Adding task to the existing JSON"""
    #first read in existing json
    json_file = []
    with open("tasks.json") as existing_json:
        json_file = json.load(existing_json)

    #define the task we want to accomplish
    task = {
        "description":str(task_description),
<<<<<<< HEAD
        "eta": int(task_eta)
=======
        "eta": int(task_eta*1000)
>>>>>>> cl-interface
    }
    #add to the new task
    json_file.append(task)

    #write the new json object with appended taks to the tasks.json file
    new_json = open("tasks.json", "w")
    json.dump(json_file, new_json, indent=4)

<<<<<<< HEAD
def robot_adding_loop(robot_name, robot_array):
=======
def robot_adding_loop(robot_name):
>>>>>>> cl-interface
    """For adding robot functionality"""
    #entering name
    robot_type = input("Enter " + robot_name + " type (enter 'help' for list of robot types): ")
    #if user does not enter 'help', create Robot object and add to passed in array
    if robot_type != "help" and robot_type != "Help":
<<<<<<< HEAD
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
=======
        if len(robot_array) > 0:
            robot = Robot(robot_name,robot_type, (robot_array[len(robot_array)-1].uniqID + 1))
            robot_array.append(robot)
        else:
            robot = Robot(robot_name,robot_type, 0)
            robot_array.append(robot)
    #otherwise print out robot types and recursively call robot_adding_loop
    else:
        print("Robot Types = Unipedal, Bipedal, Quadrupedal, Arachnid,  Radial, Aeronautical")
        robot_adding_loop(robot_name) #recursive call helps ensure that 'help' can be called infinite number of times

def main_loop():
    """Program Driver"""
    #takes in input for what user would like to do
    option = input(">> ")

    #for exiting cl interface
    if option == "exit":
        exit(0)
    #for user needing help at the command line
    elif option == "help":
        print("\tOptions:")
        print("\t-'run' to execute tasks")
        print("\t-'add tasks' to add any amount of tasks")
        print("\t-'add robots' to add more robots")
        print("\t-'view tasks' to view remaining tasks to be completed")
        print("\t-'view robots' to view robots you've created")
        print("\t-'delete robots' to delete robots you've created")
        print("\t-'leaderboard' to view the leaderboard")
        print("\t-'exit' to exit module")   
    #if they look to add tasks
    elif option == "add tasks":
        #take in the number of tasks they look to add
        num_tasks = input("How many tasks would you like to add?: ")
        if num_tasks.isnumeric():
>>>>>>> cl-interface
            #for each new task they look to add
            count = 0
            while count < int(num_tasks):
                #take in the task name
<<<<<<< HEAD
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
=======
                task_name = input("Enter task " + str(count+1) + " name: ")
                #take in task time in seconds
                task_time = input("Enter task " + str(count+1) + " time (in seconds): ")
                #add task to the tasks.json file and increment count
                addTask(task_name, int(task_time))
                count+=1
        else:
            print("ERROR: unidentified input")
    #if they look to add robots
    elif option == "add robots":
        #take in the number they look to add
        num_robots = input("How many robots would you like to add?: ")
        if num_robots.isnumeric():
>>>>>>> cl-interface
            #for each new robot they look to add
            count = 0
            while count < int(num_robots):
                #take in robot name
                robot_name = input("Enter robot " + str(count+1) + " name: ")
                #append the new robot created to the robot_array and reassign it
<<<<<<< HEAD
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
=======
                robot_adding_loop(robot_name)
                count+=1
        else:
            print("ERROR: unidentified input")
    #if they choose to view existing tasks
    elif option == "view tasks":
        #instantiate data list to hold json data
        data = []
        #open tasks.json and load into data array
        with open("tasks.json") as t:
            data = json.load(t);
        #prints out each task to the console
        for item in data:
            print("\t"+str(item))
    #if they choose to view the existing robots
    elif option == "view robots":
        if len(robot_array) > 0:
            print ("------------------------------------------------")
            #for each robot in the robot_array
            for robot in robot_array:
                print ("Robot Name: " + str(robot.name))
                print ("Robot ID: " + str(robot.uniqID))
                print ("Robot Type: " + str(robot.type))
                print ("Robot Tasks Completed: " + str(robot.tasks_done))
                print ("------------------------------------------------")            
    #if they choose to delete existing robots
    elif option == "delete robots":
        #takes in user input for what robot they want to delete
        index = input("What robot would you like to delete? (please enter their ID): ")
        if index.isnumeric():
            #if the object with the input ID is in the robot array 
            inArr = any(obj.uniqID == int(index) for obj in robot_array)
            if inArr:
                #pop from the robot array
                robot_array.pop(int(index))
                print("Deleted Robot #" + str(index))
            else:
                print("invalid index")
        else:
            print("invalid index")
    #if they choose to view the leaderboard
    elif option == "leaderboard":
        #copies over original array to temp leaderboard array to maintain original order
        leader_list = robot_array
        #sorts by tasks done in descending order with lambda fucntion
        leader_list.sort(key=lambda robot: robot.tasks_done, reverse=True)
        #printing leaderboard
        print("LEADERBOARD:")
        rank = 1
        for item in leader_list:
            print("Rank " + str(rank) + ": " + str(item.name) + " with " + str(item.tasks_done) + " tasks done!")
            rank+=1
    #if they run the simulation
    elif option == "run":
        #instantiate data list to hold json data
        data = []
        #open tasks.json and load into data array
        with open("tasks.json") as t:
            data = json.load(t);

        #assign tasks for robots to complete
        count = 0
        deleted_indices = []
        while count < len(data): #for each task
            for robot in robot_array: 
                #if a robot can complete the task, give task and add to deleted indices
                if CanComplete(robot.type,float(data[count]["eta"])):
                    robot.giveTask(data[count]["description"],float(data[count]["eta"]))
                    deleted_indices.append(count)
                    break
            count+=1

        #delete tasks completed
        num_del = 0
        for index in deleted_indices:
            data.pop(index+num_del)
            num_del-=1
        
        #now write back to the tasks.json file to persist the tasks completed
        with open("tasks.json", "w") as t:
            json.dump(data,t, indent=4)

        #POTENTIAL OPTIMIZATION: running the simulation takes roughly O(mn) time, 
        #where m is number of robots and n is number of tasks.
        #We could shorten this to O(n) if we stored the robots in a map or set,
        #where we would be able to access in O(1) time. The only reason I didn't implement 
        #this is due to the leaderboard, where it would be easier to sort an array for implement 
        #leaderboard functionality as opposed to a map. If this becomes too slow for 
        # larger datasets though, it is definitiely something that I can re-design.  
    #if error to the input
    else:
        print("ERROR: unidentified input")
    #return back to top of loop
    main_loop()


def main():
    #execution handler
    main_loop()


if "__main__":
    main()
>>>>>>> cl-interface
