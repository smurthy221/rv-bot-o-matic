"""Python script for Bot-O-Matic Program"""
import time
import json

#Specifying Robot types in 'Type' set. Will be used frequently
Type = {
    'Unipedal', 'Bipedal', 'Quadrupedal', 'Arachnid',  'Radial', 'Aeronautical'
}

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

def addTask(task_description, task_eta):
    """Adding task to the existing JSON"""
    #first read in existing json
    json_file = []
    with open("tasks.json") as existing_json:
        json_file = json.load(existing_json)

    #define the task we want to accomplish
    task = {
        "description":str(task_description),
        "eta": int(task_eta*1000)
    }
    #add to the new task
    json_file.append(task)

    #write the new json object with appended taks to the tasks.json file
    new_json = open("tasks.json", "w")
    json.dump(json_file, new_json, indent=4)

def robot_adding_loop(robot_name):
    """For adding robot functionality"""
    #entering name
    robot_type = input("Enter " + robot_name + " type (enter 'help' for list of robot types): ")
    #if user does not enter 'help', create Robot object and add to passed in array
    if robot_type != "help" and robot_type != "Help":
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

    #if they press the help option, print out options avaliable for them
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
        else:
            print("ERROR: unidentified input")
    #if they look to add robots
    elif option == "add robots":
        #take in the number they look to add
        num_robots = input("How many robots would you like to add?: ")
        if num_robots.isnumeric():
            #for each new robot they look to add
            count = 0
            while count < int(num_robots):
                #take in robot name
                robot_name = input("Enter robot " + str(count+1) + " name: ")
                #append the new robot created to the robot_array and reassign it
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
                    print(count)
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