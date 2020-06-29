import csv
from datetime import datetime

# Task         : Task Manager
# Author       : Tlangelani Hlungwani
# Description  : Program for a small business that helps to manage tasks assigned to each member of the team


print("######################################")
print("#   Welcome to Task Management App  #")
print("######################################")
print("")


# Register user 
def reg_user():
    user_reg = True
    while user_reg == True:
        new_user_name = input("Enter user name: ")
        # Check if user name already exist
        files = open("user.txt", "r")
        users = csv.reader(files)
        for lines in users :
            if lines[0] == new_user_name:
                print(f"username '{new_user_name}' already exist")
                break

        # if user doesn't exist then continue and create new password 
            new_user_password = input("Enter password: ")
            confirm_password = input("Confirm password: ")
            
        # if password matches then continue and save the user details to user.txt file 
            if new_user_password == confirm_password:
                new_user = new_user_name + "," + new_user_password
                user_names_file = open("user.txt", "a")
                user_names_file.write(new_user)
                user_names_file.close()   
                user_reg = False
                print("User Created!")
                break   
            else:
                print("The passwords did not match. Please try again.")

 # add new task
def add_task(user,title,description,date,due_date,completed):
    complete_task = (user + ", " + title + ", " + description + ", " + date + ", " + due_date + ", "+ completed) 
    
    # Write task information to the file task.txt 
    task_file = open("tasks.txt", "a")
    task_file.write(f"\n{complete_task}")
    task_file.close()
    print("Task Created!")
    return complete_task

# view all task task
def view_all():
    task_file = open("tasks.txt", "r+")
    # Iterate through the open file
    for lines in task_file:
        count = 0
        tasks = ""
        tasks = tasks + lines
        tasks = tasks.split(",")

        # Format and print out
        print("Username: " + tasks[0] + "\nTitle: " + tasks[1] + "\nDescription: " + tasks[2] + "\nDate Assigned: " + tasks[3] + "\nDue Date: " + tasks[4] + "\nCompleted: " + tasks[5] + "\n")
    task_file.close()


def view_mine():
   #username = input("Please enter the username which you want to view the tasks for?\n")
   num_task = 0
   view_mine = open("tasks.txt", "r+")
   for lines in view_mine:
        tasks = ""
        tasks = tasks + lines
        tasks = tasks.split(",")
        num_task += 1
        if username == tasks[0]:
            print("Task Number: " + str(num_task) + "\nUsername: " + tasks[0] + "\nTitle: " + tasks[1] + "\nDescription: " + tasks[2] + "\nDate Assigned: " + tasks[3] + "\nDue Date: " + tasks[4] + "\nCompleted: " + tasks[5] + "\n")

   editTask = input("Would you like to edit a task? (Edit) or return to the menu? (-1) :").title()

   def _edit_file(taskComplete):
       userTask = taskFile[taskNum].strip().split(",")
       new_state = taskFile[taskNum].strip().replace(userTask[5], taskComplete)
       print(new_state)
       updated_string = view_mine.read().replace(taskFile[taskNum].strip(), new_state)
       with open('tasks.txt', 'w+') as f:
           f.writelines(updated_string)

   # Selects a specific task
   if editTask == "Edit":
       taskNum = int(input("Please enter the Task number? : "))
       taskNum = taskNum - 1
       with open('tasks.txt', 'r+') as file:
           taskFile = file.readlines()
       for line in taskFile:
           print(taskFile[taskNum] + "\n")
           break

    # Update the task status if its complete 
       taskComplete = input("Has this task been completed? :").title()
       if taskComplete == "Yes":
           _edit_file(taskComplete)

       elif taskComplete == "No":
           _edit_file(taskComplete)

    #return to the main menu if -1 is selected .
   elif editTask == "-1":
       successfull_login()


# Generate Report
# Report for task
# Report for users
def generate_report():
  
    all_tasks = open("tasks.txt", "r")
    num_task = 0
    completed_task = 0
    uncompleted_task = 0


    for lines in all_tasks:
        tasks = ""
        tasks = tasks + lines
        tasks = tasks.split(",")
        task_check = tasks[5]
        num_task += 1

   
   # Open the file using csv 
   # Get task status and replace any spaces 
   # Calculate completed tasks and uncompleted tasks
    with open('tasks.txt') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            task_check = row[5]
            if task_check == "Yes":
                completed_task += 1
            if task_check == "No":
                uncompleted_task += 1

            # The total number of tasks that haven’t been completed and that are overdue.
            overdue_task = 0
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            date_time = datetime.fromtimestamp(timestamp)
            current_date = date_time.strftime("%d %B %Y")
            due_date = row[4]
            if  current_date > due_date :
                overdue_task += 1

            # The percentage of tasks that are incomplete.
            percentage_incomplete = (uncompleted_task/num_task) * 100
            percentage_complete = (overdue_task/num_task) * 100
          
   
    # Create a file task_overview.txt.txt to write all the details         
    with open("task_overview.txt", "a") as f:
        f.write(f"The total number of tasks that have been generated: {num_task}\n")
        f.write(f"The total number of completed tasks: {completed_task}\n")
        f.write(f"The total number of uncompleted tasks: {uncompleted_task}\n")
        f.write(f"The total number of tasks that haven’t been completed {uncompleted_task} and that are overdue {overdue_task}\n")
        f.write(f"The percentage of tasks that are incomplete : {round(percentage_incomplete)}%\n")
        f.write(f"The percentage of tasks that are overdue. : {round(percentage_incomplete)}%\n")

    # The total number of users registered with task_manager.py
    count_users = 0
    users_file = open("user.txt" ,"r+")
    for users in (users_file):
           count_users += 1
    
    # The total number of tasks that have been generated and tracked using the task_manager.py
    count_task = 0
    tasks_file = open("tasks.txt" ,"r+")
    for tasks in tasks_file:
        count_task += 1

    # Get current user and Current task
    current_user = input("Enter username that you want to generate the task for: ").lower()
    all_tasks = open("tasks.txt", "r")
    current_user_num_task = 0
    current_user_completed_task = 0
    current_user_uncompleted_task =0
    current_user_overdue_task = 0
    
    for lines in all_tasks:
        tasks = ""
        tasks = tasks + lines
        tasks = tasks.split(",")
        
        if current_user == tasks[0]:
             task_check = row[5]
             if task_check == "Yes":
                current_user_completed_task += 1
             if task_check == "No":
                current_user_uncompleted_task += 1
             current_user_num_task += 1 
             current_user_percentage_incomplete = (current_user_completed_task/num_task) * 100
             current_percentage_complete = (current_user_uncompleted_task/num_task) * 100
             
             due_date = row[4]
             if current_date > due_date :
                 current_user_overdue_task += 1
               


     # Create a file user_overview text to write all the details         
    with open("user_overview.txt", "a") as f:
        f.write(f"The total number of users registered: {count_users}\n" + 
        f"The total number of tasks: {count_task}\n" +
        f"The total number of tasks assigned to {current_user} : {current_user_num_task}\n" +
        f"percentage of the tasks assigned to that user have been completed: {round(current_user_percentage_incomplete)}%\n" +
        f"percentage of the tasks assigned to that user must still be completed: {round(current_percentage_complete)}%\n" +
        f"percentage of the tasks assigned to that user have not yet been completed and are overdue: {current_user_overdue_task}%\n"
         )
    

# display Statistics
def display_statistics():
    # User overview
    print("")
    print("#### - User Overview -  ####")
    with open('user_overview.txt') as csv_file:
        csv_reader = csv.reader(csv_file)
        for [users_file_overview] in csv_reader:
            print(users_file_overview)

    print("")
    print("#### - Task Overview -  ####")        
    # Tasks overview
    with open('task_overview.txt') as csv_file:
        csv_reader = csv.reader(csv_file)
        for [task_file_overview] in csv_reader:
            print(task_file_overview)

#Initiate login variable
login = False

# Read the external file 
while login == False:
        # Request user input username and password
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Read the lines
        login_files = open("user.txt", "r")

        # Split method returns ['admin', adm1n\n].
        # So I used csv instead.
        users = csv.reader(login_files)
        for lines in users :
            if lines[0] == username and lines[1]== password:
                login = True
                print("You are logged in successfully as", username )
                break
        else:
            print("Wrong username or password")



# Select option on successful login 
def successfull_login():
    if login == True :
        if username == "admin" :
            print("Please select one of the following options: \n" +
                "r - register user\n" +
                "a - add task\n" +
                "va - view all tasks\n" +
                "vm - view my tasks\n" +
                "gr - generate report\n" +
                "ds - display statistics\n" +
                "e - exit")
            user_select = (input("Which option would you like to select: ")).lower()
        else:
            print("Please select one of the following options: \n" +
                "a - add task\n" +
                "va - view all tasks\n" +
                "vm - view my tasks\n" +
                "e - exit")
            user_select = (input("Which option would you like to select: ")).lower()
        print("")

        # Check Selected option

        if user_select == "r":
            reg_user()

        if user_select == "a":
            print("===# You are about to add a new task. #====")
            task_user = input("Please enter the user name of the person to whom you are assigning the task: ")
            task_title = input("Please enter the task title: ")
            task_description = input("Please describe the task in detail: ")
            task_due = input("Please enter the due date of the task: ").title()
            task_completed = "No"

            # Get Date in date, month , year format
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            date_time = datetime.fromtimestamp(timestamp)
            assign_date = date_time.strftime("%d %B %Y")
            add_task(task_user,task_title,task_description,assign_date,task_due,task_completed)
        
        if user_select == "va":
            print("===# All Tasks . #====")
            view_all()

        if user_select == "vm":
            print("===# Your Tasks . #====")
            view_mine()

        if user_select == "gr":
            generate_report()
            print("===# Generated report . #====")
            print("File saved!", username.title())
          
        if user_select == "ds":
            print("===# statistics . #====")
            display_statistics()

        if user_select == "e":
            print("Bye", username.title())
            exit()

successfull_login()


