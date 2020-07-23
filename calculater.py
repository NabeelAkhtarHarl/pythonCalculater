#functions
def add(a,b):  
    return a+b
def multi(a,b):
    return a*b
def sub(a,b):
    return a-b
def division(a,b):
    return a/b

#printshow
print("select that operation you perform: \n 1.Add \n 2.multi \n 3.subtraction \n 4.division ")

select=int(input("please select 1,2,3,4 "))
a=int(input("please enter first number "))
b=int(input("please enter second number "))
 
if select==1:
   print( add(a,b) )
elif select==2:
   print( multi(a,b) )
elif select==3:
   print( sub(a,b) )
elif select==4:
   print( division(a,b) )
else:
    print("invalid")
    