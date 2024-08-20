info={
    "name":"abhilash",
    "subject":["python","c","java"],
    "topics":("dict","set"),
    "age":35,
    "is adult":True,
    "marks":90.5
    
}
info["name"]="hulk"     #we change the value
info["name"]="smash"
print(info)

#nested dictionary
student={
    "name":"abhi",
    "subjects":{
        "phy":95,
        "chem":81,
        "math":90,
    }
}
print(student["subjects"]["math"])

#dictionary methods
#1.myDict.keys()#returns all keys
student={
    "name":"abhi",
    "subjects":{
        "phy":95,
        "chem":81,
        "math":90,
    }
}

print(student.keys())
print(list(student.keys()))
print(len(student.keys()))

#2 myDict.values()#return all values
info={
    "name":"abhilash",
    "subject":["python","c","java"],
    "topics":("dict","set"),
    "age":35,
    "is adult":True,
    "marks":90.5
    
}
print(student.values())
print(list(student.values()))

#3my.Dict.items()#return all (key,value) pairs as atuple
info={
    "name":"abhilash",
    "subject":["python","c","java"],
    "topics":("dict","set"),
    "age":35,
    "is adult":True,
    "marks":90.5
    
}

print(student.items())
print(list(student.items()))
#if we want to access the tuples individualy
student={
    "name":"abhi",
    "subjects":{
        "phy":95,
        "chem":81,
        "math":90,
    }
}
#print(student.items())
#print(list(student.items()))
pairs=list(student.items())
print(pairs[0])