#list
#list creation
age_list=[15,16,17,18,19]
name_list=["Manju","Goku","Amal","Radha","Anakha"]
#list operations and modifications
name_list.append("Yazhini")#add a string
age_list.insert(2,30)#insert age 30
name_list.remove("Yazhini")#remove string
age_list.pop()
age_list.extend([29,30,26])
age_list.sort()
age_list.reverse()
#accessing list elements
print("maximum age is:",max(age_list))
print("minimum age is:",min(age_list))
print("sum of agelist is:",sum(age_list))
print("first element in the namelist:",name_list[0])
print("last element in the namelist:",name_list[4])
print(" element from index 2 to 4in the namelist:",name_list[2:5])
name_list.reverse()
print("name list in reverse order:",name_list)

#dictionary
student_marks={"Gokul":60,"Manju":95,"Malu":69,"Amal":89,"Sheethal":92}
print(student_marks)
print(student_marks["Manju"])
print("mark of manju",student_marks["Manju"])
student_marks.update({"Janani":80})
print(student_marks)
student_marks["Gokul"]=65
print(student_marks)
print(student_marks.keys())
print(student_marks.values())
print(student_marks.items())

#set
my_set={"a","e","i","o","u","a","a","i"}
#a
print(my_set)#it only prints 5 values , because set won't allow duplicate values
#b
#once the set is created you cannot change an item , u can add new values and remove but cannot change existing value
set1={1,3,5,7,9}
print("set1:",set1)
set2={2,3,5,8,10}
print("set2",set2)
#union
print("set1 union set2",set1.union(set2))
#intersection
print("set1 intersection set2",set1.intersection(set2))
#operations and conditional statements
#1
score=int(input("enter your score"))
if  score<0 or score>10:
    print("score is not in the allowed range(0-10)")

#2
if score>7:
    print("above average:congratulations!")
elif 3<score<=7:
        print("average:good effort!keep practicing")
elif score<4:
        print("Your score is below average ;but good news is,consistent practice will lead to better results")
else:
    print("not categorised")
             
