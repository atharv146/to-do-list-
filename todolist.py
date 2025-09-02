def main_menu():
    while True:
        choose = input("Would you like to view tasks, mark tasks, add tasks, or exit?: ").lower()
        if choose == "view tasks":
            view_tasks()
        elif choose == "mark tasks":
            mark_tasks()
        elif choose == "add tasks":
            add_tasks()
        elif choose =="exit":
            print("This is your final list:")
            print(', '.join(tasks))
            break
        else:
            print("Please select one of the options exactly as written. ")
            




def add_tasks():
    to_add = input("What task would you like to add?: ")
    tasks.append(to_add)
    return
    
def mark_tasks():
    if not tasks:
        print("No tasks to print")
        return
    
    print(', '.join(tasks))
    descision = input("Which tasks would you like to mark? Type the task one by one and exactly as written in the list: ").lower()
    if descision in tasks:
        tasks.remove(descision)
        print("The task",descision,"has been removed")
    else: 
        print("Task not found. Please select the task as written in the list.")
        return
    

def view_tasks():
    if tasks:
        print(', '.join(tasks))
    else: 
        print("No tasks available")
        return
    


tasks = []
main_menu()

