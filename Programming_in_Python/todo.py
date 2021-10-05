# This is a to-do list

done = []
notdone = []

while True:
    command = input("Add-(addtask), Set Done-(setdone), Set Undone-(setundone), List Finished-(listdone), List Unfinished-(listnotdone): ") # Keep taking commands
    if command.startswith("addtask"): # Add a task
        notdone.append(command.replace("addtask ", ""))
    elif command.startswith("setdone"): # Set a task with some index to done
        taskID = int(command.replace("setdone ", ""))
        value_removed = notdone.pop(taskID) 
        done.append(value_removed)
    elif command.startswith("setundone"): # Set a task with some index to undone
        taskID = int(command.replace("setundone", ""))
        value_removed = done.pop(taskID)
        notdone.append(value_removed)
    elif command.startswith("listdone"): # List all elements in the 'done' list
        print(done)
    elif command.startswith("listnotdone"): # List all elements in the 'notdone' list
        print(notdone)
