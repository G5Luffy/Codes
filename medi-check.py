medical_cause=input("did you have a medical cause Y or N: ")
atten=int(input("enter the attendance of student: "))
if medical_cause == 'Y': #checking condition 1
    print ("you are allowed")
else:
   if atten>=75:
     print("allowed")
   else:
    print ("not allowed")