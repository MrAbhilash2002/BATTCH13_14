marks1=94.4
marks2=87.5
marks3=95.5
marks4=66.5
marks5=45.5

marks=[94.4,87.5,66.5,45.5]
print (marks)
print(type(marks))
print(marks[1])
print(marks[0])
print(len(marks))

student=["abhi",95.5,20,"odisha"]
print(student)



student=["abhi",95.5,20,"odisha"]
print(student[0])
student[0]="hulk"
print(student)

#list slicing
marks=[50,90,60,46]
print(marks[1:4])
print(marks[-3:-1])

#list methods
list=[2,3,4,5,6,7]
list.append(9)
print(list)
 
#list sort
#ascending
list=[2,3,4,5,9,7]
print(list.sort())    #we can also add a append
print(list)

#reverse=true
list=[1,5,9]
print(list.sort(reverse=True)) #it works descending order, it also work on strings
print(list)

#reverse method
list=[1,22,33,7,]
list.reverse()
print(list) 

#list insert
list=[1,2,6]
list.insert(1,0)
print(list)

#list remove
list=[1,2,6,2,1]
list.remove(2)
print(list)

#list.pop
list=[1,2,3]
list.pop(2)
print(list)

#list.clear()
list=[10,20,30,40]
list.clear()
print(list)

#list.count()
list=[10,20,30,40,50,20,30,10,10,10,10]
list.count(10)
print(list.count(10))

#list.copy()
list=[0,10,20,10,10,30,40,50]
list2 =list.copy()
print(list2)

#list.reverse()
list=[10,20,30,40]
list.reverse()
print(list)

