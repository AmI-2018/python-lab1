print("ciao")

numTask = 0;
tasks = []
n = 0

while n < 4:
    print("Inserire il codice corrispondente: ")
    print("""
    \n1. insert a new task (a string of text);\n
    2. remove a task (by typing its content, exactly);\n
    3. show all existing tasks;\n
    4. close the program.
    """)
    n = int(input())

    if n == 1:
        print("\n\nInserire una nuova task:", end=" ")

        tasks.append(input())

    elif n == 2:
        print("Inserire il nome della task da eliminare: ", end=" ")
        taskToDelete = input()
        i = 0
        for task in tasks:
            if task == taskToDelete:
                tasks.pop(i)
            i += 1



    elif n == 3:
        print("Ecco tutte le tasks: ")
        for task in tasks:
            print(task, "\n")


    elif n == 4:
        exit()


#modifica da casa