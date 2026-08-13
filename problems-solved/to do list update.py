tasks=["enroll for hackathon","update KYC","finish assignment","recharge mobile"]

completed_tasks=input("Enter complted tasks: ")

if completed_tasks in tasks:
    
    tasks[tasks.index(completed_tasks)]= completed_tasks + "-completed"

else:
    print("task not found")
print(tasks)    
    
