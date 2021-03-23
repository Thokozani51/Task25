from datetime import date #importing of an automatic setting of the current date
import datetime#importing of an automatic setting of the date and time

user_name = "" #variable used for the user_name input
user_name = input("Enter your user_name: ") #user_name input
user_password = input("Enter your user_password: ") #user_password input

while True:#using the while loop for the process of noting messages of when the user enters the wrong or right user_name/user_password inputs
    user =  open("user.txt", "r") #open the user.txt file
    flag = False #if the credentials are false the programme will request the correct credentials 
    for user_read in user: #reading of lines from the file
        new_user = user_read.split(", ") #splitting the coma and the spacing inbetween the user_name and the user_password 
        
        if user_name == new_user[0]: #if the user_name is the same with the new_user to be entered by the new_user                
            if user_password == new_user[1].strip("\n"): #displaying the stripping of the new line(\n)
                print("Correct credentials!") #printing out of the outcome message when the user_name == new_user
                flag = True #if the credentials are true,the programme will move forward to the menu
                break #breaking of the process 
    if flag: 
        break
    
    print("You've entered the wrong password or user name") # the error message will be displayed when the user has entered the wrong password or user_name
    user_name = input("Enter your user_name: ") #user_name input
    user_password = input("Enter your user_password: ") #user_password input
    user.close()#closing of the file
def reg_user():  #defining the reg_user function
    output_file = open("user.txt","a") #open the user.txt file with the append mode for inserting the input of logging in details
    user_name = input("Please enter a new username") #input of the new user_name from the user
    user_password = input("Please enter a new password") #input of the new password from the user
    confirmed_user_password = input("Please confirm password") #confirmation of the password
    if user_password == confirmed_user_password :#if user_passwords own
        output_file.write(f"\n{user_name}, {user_password}") #code for writing the user_name and user_password into the user.txt file
    else: #else if the user does not insert the correct password
        print("Passwords not the same")#printing the message that should be displayed on the programme if the user enters the wrong password
        

def add_task():#defining the add_task function
    output_file = open("tasks.txt","a") #opening the tasks.txt file with the append mode
    user_name = input("Enter your username")#user to enter their username after choosing the add_task option
    user_task = input("Enter title of task")#user to enter the title task 
    task_description = input("Enter description of task")#user to enter the description of task
    task_completion = "No"#user to note that the tasks have not been completed 
    date_assigned = date.today().__format__("%d %b %Y")#imported format on how the date has to be displayed on the file
    due_date = input("Enter due date of task")#user to enter the due date of the tasks
    print("write in tasks.txt")#write the data in the tasks.txt file 
    output_file.write(f"\n{user_name}, {user_task}, {task_description}, {date_assigned}, {due_date}, {task_completion} ")#add the code that will open task.txt and write the data to the file
    output_file.close()#close the output_file
    #if selection == 'va': # if the user's input is 'va' from the options provided above

def view_all_tasks():    
    f = open("tasks.txt", "r") #opening the tasks.txt file with the read only mode
    text = f.readline() #reading of every line
    for text in f:
        
        taskList = text.split(", ") #creating a space inbetween the comma and the word in the task list in the file
        print(f"Task: {taskList[2]}")#print 'Task' in index [2] in the taskList  
        print(f"Assigned to: {taskList[0]}")#print 'Assigned to' in index [0] in the taskList
        print(f"Date assigned: {taskList[3]}")#print 'Date assigned' in index [3] in the taskList 
        print(f"Due date: {taskList[4]}")#print 'Due date' in index [4] in the taskList
        print(f"Task complete: {taskList[5]}")#print 'Task complete' in index [5] in the taskList
    f.close()#closing of task.txt file
def view_my_tasks (): #if the user's input is 'vm' from the options above
    f = open("tasks.txt", "r") #opening the tasks.txt file with the read only mode
    task_dict = {}#using the dictionary to number the tasks for the user to be able to select the task they wish to edit using numbers instead of having to type in the task 
    task_id_numb = 1#increment of the task_id_numb i.e the number the task is noted in when the user selects a specific one.
    for text in f: #reading a line from the text file
        taskList = text.split(", ") #separate the string when ever we come across a commer and a space
        task_dict[task_id_numb] = text.strip("\n")#stripping the new line 
        
        if taskList[0] == user_name:#if the user_name is indexed at [0]
            print(f"Task number {task_id_numb}")#print 'task number' will be the one noted as 'task_id_numb'
            print(f"Task: {taskList[1]}") #Displaying task title to the console
            print(f"Assigned to: {taskList[0]}")#Displaying the user name of the person assigned that task 
            print(f"Date assigned: {taskList[3]}")# Displaying the date the was assigned to the user to con6sole 
            print(f"Due date: {taskList[4]}")#Displaying the due date of the task to the console 
            print(f"Task complete: {taskList[5]}")#Displaying the Yes/No idicating whether a task is completed of not
            print(f"Task Description: {taskList[2]}")#Displaying the description of the task    
        task_id_numb += 1#count of task_id_numb
    
    f.close()#closing of file
    while True:
        
        task_numb = int(input("Enter a task number or -1 to exit: "))#variable asking the user to select the task numb they want to be displayed from the task.txt file
        if task_numb != -1:#if the task_numb is not equal to -1
            t = task_dict[task_numb]#
            
            task_completion = input("Pleas enteter e- to edit the task or m- to mark task as complete: ")#user's input of whether they have completed the task or not and whether they want to edit the selected task
            
            if task_completion == 'm':#if the user selects yes from the question or input then the programme should print out 'yes' on the console 
                t = t.split(", ")#splitting of the string between the comma and space in order to create a list items from task
                t[-1] = "yes"#changing the contents of the last index
                t = ", ".join(t)#the List is being joined again to become a string
            elif task_completion == 'e':#elif the user chooses to edit the string
                menu = input("Enter a - to change user name or d - to change due date: ")#menu option where the user will select which part of the string they wish to edit/mend 
                if menu == "d":#if the user selects the 'd' option from the menu of which will be the changing of the due date in the string
                    due_date = input("Please enter the due date")#user to state the due date after editing the file for changing the due date noted in the file
                    t = t.split(", ")#splitting the string between the comma and the space which will create the string to being a list
                    t[-2] = due_date#index position of where the user will edit for mending in the string 
                    t = ", ".join(t)#joining the file data from being list back to being a string
                elif menu == 'a':#if the user selects 'a' for changing the user name in the file 
                    new_username = input("Please enter the new user name")#user being asked to note the new user name
                    t = t.split(", ")#splitting the string between the comma and the space which will create the string to being a list
                    t[0] = new_username#index position of where the user will edit for mending in the string     
                    t = ", ".join(t)#joining the file data from being a list back to being a string
            
            task_dict[task_numb] = t #returning the file back to the dictionary
        else:
            break #stop the processing 
    
    f = open("tasks.txt", "w")#open the task file with w only access mode
    alltask = ""#variable for the input of all tasks
    for v in task_dict.values():#create the for loop that will iterate on all dictianary values
        alltask += v + "\n"
    
    alltask = alltask.strip("\n")#stripping the new line in the tasks file
    f.write(alltask)#write alltask in the task.txt file


def task_overview():#defining function
    f = open("tasks.txt", "r") #opening the tasks.txt file with the read only mode
    incompleted = 0#count the number of incomplete tasks
    num_tasks = 0 #count number of tasks in the file
    completed = 0#count the number of completed tasks
    overdue = 0 #count of the number of tasks that are overdue
    percentage_task_incomplete = 0#count the percentage of the incomplete tasks in the tasks file
    
    
    for line in f:#reading a line from the text file
        num_tasks += 1 #incrementing number of tasks in the task file.
        tasklist = line.strip("\n").split(", ")#splitting the space and the comma in the list
        if tasklist[-1].lower() == "no":#if the task indexed at -1 on a string is noted as 'no'
            incompleted += 1#increment of the incompleted tasks
            strDate = tasklist[-2]#strDate indexed at -2 on the taskList
            dateObject = datetime.datetime.strptime(strDate, "%d %b %Y")#formula for setting the date,month,and year in a specific sequence
            currentdate =  datetime.datetime.now()#variable used to create the current time, date,month,and year
            if dateObject < currentdate:#if the variable 'dateObject' is less than the current date,then the task will be noted as being overdue 
                overdue += 1#count for the overdue tasks   
        if tasklist[-1].lower() == "yes":#if the task indexed at -1 on a string is noted as 'yes'
            completed += 1#increment of completed tasks
    percentage_task_incomplete = (incompleted/num_tasks) * 100#percentage formula for finding the percentage of incomplete tasks
    percentage_task_incomplete_overdue = (overdue/num_tasks) * 100#percentage formula for finding the overdue tasks
    
    f = open("task_overview.txt","w")#opening the task_overview using the write only mode
    f.write(f"The percentage of tasks that are overdue {percentage_task_incomplete_overdue}\n")#writing the 'percentage_task_incomplete_overdue' with a new line character 
    f.write(f"The total number of tasks that have'nt been completed and overdue is {overdue}\n")#writing the 'overdue tasks' with the new line character
    f.write(f"The total number of tasks is {num_tasks}\n")#writing the 'num_tasks' with a new line character
    f.write(f"the total number of incomplete tasks is {incompleted}\n")#writing the 'incompleted' tasks with a new line character
    f.write(f"The total numer of completed tasks is {completed}\n")#writing the 'completed' tasks with the new line character
    f.write(f"The total percentage of incomplete tasks is {percentage_task_incomplete}\n")#writing the 'percentage_task_incomplete' with the new line character
    
    f.close() #close file
    
    #print(f"The total number of incomplete and overdue tasks is {overdue_incompleted}")
#def per_user(user_name = "admin", numb_task = 8): 
def per_user(user_name, numb_task):#function with the users data that will help with the working out of the users details    
    f = open("tasks.txt", "r") #opening the tasks.txt file with the read only mode
    user_tasks_assigned = 0 #count for the user_task_assigned
    incomplete_usertask_assigned = 0 #count for the incomplete_usertask_assigned
    complete_task_assigned = 0 #count for the complete_task_assigned
    overdue = 0 
    for text in f: #reading a line from the text file
        taskList = text.strip("\n").split(", ") #separate the string when ever we come across a comma and a space
        if taskList[0] == user_name:#if the user_name noted by the user is the same as the user_name on the file
            #user_tasks_assigned = 0
            user_tasks_assigned += 1 #increment of the user_tasks_assigned
            if taskList[-1].lower() == "no": #if the task indexed at -1 on a string is noted as 'no' the task is incomplte
             
                incomplete_usertask_assigned += 1#increment of the incomplete_usertask_asigned
                strDate = taskList[-2]#the strDate is indexed on -2 on the taskList
                dateObject = datetime.datetime.strptime(strDate, "%d %b %Y") #formula for setting the date,month,and year in a specific sequence
                currentdate =  datetime.datetime.now()#variable used to create the current time, date,month,and year
                if dateObject < currentdate:#if the dateObject is less than the currentdate
                    overdue += 1   #count for the overdue tasks
            if  taskList[-1].lower() == "yes":#if the task indexed at -1 on the string is noted as 'yes' the task is completed
                complete_task_assigned += 1#increment of the completed_task_assigned
            
      
    percentage_task = (user_tasks_assigned/numb_task) * 100#percentage formula for finding the percentage of incomplete tasks            
    percentage_task_complete = 0.0
    percentage_task_incomplete = 0.0
    percentage_task_incomplete_overdue = 0.0
    if user_tasks_assigned > 0:#if the user_tasks_assigned are greater than 0
        percentage_task_complete = (complete_task_assigned/user_tasks_assigned)*100#percentage formula for finding the percentage of complete tasks
        percentage_task_incomplete = (incomplete_usertask_assigned/user_tasks_assigned)*100#percentage formula for finding the percentage of incompleted user tasks 
        percentage_task_incomplete_overdue = (overdue/user_tasks_assigned)*100#percentage formula for finding the percentage of incompleted and overdue tasks assigned to the user
    
    us_o =(f"the percentage of tasks assigned to the user that are incomplete and overdue is {percentage_task_incomplete_overdue}")#calling out the percentage formula for finding the percentage of incompleted and overdue tasks assigned to the user
    us_o +=(f"\nthe percentage of tasks assigned to the user that still need to be completed is {percentage_task_incomplete}")#calling out the user assigned tasks that are incomplete
    us_o +=(f"\nthe total number of user's completed tasks is {complete_task_assigned}")#calling out of the function for the complete_task_assigned               
    us_o +=(f"\nthe total number of incompleted tasks is {incomplete_usertask_assigned}")#calling out of the function for the incomplete_usertask_assigned        
    us_o +=(f"\nthe total number of tasks assigned to {user_name} is {user_tasks_assigned}")#calling out of the functions used to calculate the total tasks assigned to the specific user
    
    #percentage_task_complete = (user_tasks_assigned/numb_task) * 100#percentage formula for finding the percentage of incomplete tasks
    us_o +=(f"\npercentage of the total number of user tasks have been completed is {percentage_task_complete}")#calling out the function of finding the percentage of the complete tasks in the tasks text file
    us_o +=(f"\npercentage of the total number of tasks have been assigned to admin {percentage_task}")#calling out the function of finding the percentage of the incomplete tasks in the tasks text file    
    return us_o #return the results to the user overview(us_o)
    

    
   # completed_task_percentage = 0
   # completed_task_percentage += 1
   # print(f"")
    
      

def user_overview() :#text file containing details about on the user txt file
    num_tasks = 0 #count number of tasks in the file
    f = open("tasks.txt","r")#opening and reading the task txt file using the reading mode
    for line in f: #reading a line from the text file
        num_tasks += 1 #incrementin2g number of tasks in the task file.
    f.close()
   
    user = open("user.txt", "r") #opening the user.txt file with the read only mode
    usData = ""
    num_users = 0 #count number of users in the file
    for line in user: #reading a line from the text file
        num_users += 1#increment of the num_users
        us_name, passw = line.split(", ")
        usData += f"for user {us_name}:\n------------------\n"+per_user(us_name, num_tasks) + "\n"#underlining the different user_names and data assigned to them
    user.close()

    print(usData)
     
    f = open("user_overview.txt","w")#opening the task overview file with a write only mode
    f.write(f"the total  number of users is {num_users}\n")#write the total number of users onto the user_overview file under the variable 'num_users' and creating a new line after writing/transfering the data
    f.write(f"the total number of tasks is {num_tasks}\n")#write the total number of tasks onto the user_overview file under the variable 'num_tasks' and creating a new line after writing/transfering the data 
    f.write(usData)#file with the usData written and stored     
    
    f.close() #closing of file  
   
 
    
    
def generate_reports():#defining function
    task_overview()#
    user_overview()
    
def Displaying_statistics():#defining function
    generate_reports()
    
    #open the user overview file
    f = open("user_overview.txt","r")#open and read the user_overview txt file
    print(f.read())#printing the data that was inserted into the user_overview txt file 
    
    #open the task overview file(r)
    f = open("task_overview.txt","r")#opening the task_overview.txt with the read only mode
    print(f.read())#print the file task_overview.txt 
        
                
while True:
    if user_name == "admin": #if the user name is admin then they can view the bottom menu  
        print("r-register user")#printing the register user option registering the user when they log into the menu
        print("a-add task")#printing the add task option for the users to add a task in the task file
        print("va-view all tasks")#printing the view all tasks option for the user to view all the tasks in the task file
        print("vm-view my tasks")#printing the view my tasks option for the user to view tasks assigned to them
        print("gr - generate reports")#printing the generate reports option for the user to generate reports on the tasks file
        print("ds-Displaying statistics")#printing the displaying statistics option for users to view the statistics
        print("e-exit")#print e for exiting the programme
    else:#else the bottom menu will display if the user name is not admin
        print("a-add task")#printing the add task option for the users to add a task in the task file
        print("va-view all tasks")#printing the view all tasks option for the user to view all the tasks in the task file
        print("vm-view my tasks")#printing the view my tasks option for the user to view tasks assigned to them
        print("e-exit")#printing the exit option if the user wants to exit the programme
        
    selection = input('>>  ') #space specified for the users input from the selected option above

    if selection =='r': #if the users selection is 'r'
        reg_user()#calling out the reg_user function
    if selection == 'a': #if the users selection is 'a'
        add_task()#calling out the add_task function
    if selection == 'va': #if the users selection is 'va'
        view_all_tasks()#calling out the view_all_tasks function
    if selection == 'vm':#if the users selection is 'vm' 
        view_my_tasks()#calling out the view_my_tasks function 
    if selection == "gr": #if the users selection is 'gr'
        generate_reports()#calling out the generate_reports function       
    if selection == 'ds': #if the users selection is 'ds'
        Displaying_statistics()#calling out the task_overview function  
    if selection == 'e': #if the users selection is 'e'
        break #if the user selects 'e' the program will stop  