def main():
    choice = 0
    taskls = []

    while choice != 4:
        print("What would you like to do")
        print("1) Add a new task")
        print("2) Update a task status")
        print("3) Print the task list")
        print("4) Exit")

        choice = int(input("Please enter your choice : "))

        if choice == 1:
            task = input("Task Name : ")
            Current_status = "to do"
            taskls.append([task, Current_status])
            print("-----------------")
            print(f"Task Added with id {len(taskls)-1}")
            print(f"Task Name = {task}")
            print(f"Task Status = {Current_status}")
            print("-----------------")



        elif choice == 2:
            task_id = int(input("Please enter the task ID You wanna update : "))
            print(f"Task Name : {taskls[task_id][0]}")
            print(f"Current status : {taskls[task_id][1]}")
            print("-----------------")

            print("Please select the status")
            print("1) to-do")
            print("2) in progress")
            print("3) completed")

            status_id = int(input("Please select the status : "))

            if status_id == 1:
                taskls[task_id][1] = "to-do"
            elif status_id == 2:
                taskls[task_id][1] = "in progress"
            else:
                taskls[task_id][1] = "Completed"

            print("-----------------")
            print(f"Task Name = {taskls[task_id][0]}")
            print(f"Task Status = {taskls[task_id][1]}")
            print("-----------------")

        elif choice == 3:
            for entries in taskls:
                print(f"Task : {entries[0]} | Status : {entries[1]}")

        else:
            return 
            
if __name__ == "__main__":
    main()
