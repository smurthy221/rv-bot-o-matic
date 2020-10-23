"""Python script for Bot-O-Matic Program"""
import time
import json

#Specifying Robot types in 'Type' set. Will be used frequently
Type = {
    'Unipedal', 'Bipedal', 'Quadrupedal', 'Arachnid',  'Radial', 'Aeronautical'
}

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
            print("TypeError, please check spelling on type input")
            exit(1)

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

def main():
    #taking in input for robot creation
    #will exit(1) if an issue with an illegal name
    robot_name = input("Enter your robots name: ")
    robot_type = input("Enter your robots type (enter 'help' for list of robot types): ")
    if robot_type == "help" or robot_type == "Help":
        print("Robot Types = Unipedal, Bipedal, Quadrupedal, Arachnid,  Radial, Aeronautical")
        robot_type = input("Enter your robots type: ")

    #construct your robot object
    robot = Robot(robot_name,False,robot_type)

    #instantiate data list to hold json data
    data = []
    #open tasks.json and load into data array
    with open("tasks.json") as t:
        data = json.load(t);

    #assign first 5 tasks to you robot to complete
    while len(data)!=0 and robot.tasks_done < 5:
        robot.giveTask(data[0]["description"],data[0]["eta"])
        data.pop(0)

    #once all robots 5 tasks are complete
    print(robot_name + " finished doing their tasks!")

main()