GPA=int(input("Enter Your GPA:"))
extracurricular=input("participated in extracurricular (yes/no): ")
if GPA >= 3.5:
     if extracurricular== "yes":
        hours=int(input("Hours spent in community service: "))
        if hours>=30:
            print("award full scholarship")
        else:    
           print("Award Partial scholarship")

     else:
        print("No scholarship")

else:
    print("No Scholarship")
    
