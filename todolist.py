task_list=[]
while True:
 print("welcome to do task list")
 print("\n1.add task,\n2.view task,\n3.remove task")
 choice=int(input("enter the task(1:3)"))

 if choice==1:
    task=input("enter your task")
    task_list.append(task)
    print("new task is added successfully")
 elif choice==2:
   print(task_list)
 elif choice==3:
   task=input("remove your task")
   task_list.remove(task)
   print("task is removed successfully")
   break
 else:
  print("invalid choice")

     
