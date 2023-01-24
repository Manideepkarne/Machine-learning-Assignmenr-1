dog= {} # creating an empty dog dictionary
#allocating keys and values to the dog dictionary
dog = {"name": "Lulu","color": "white","breed": "polo", "legs": 4, "age": 5}
print("dog dictionary is :", dog)
#creating a student dictonary and assigning values to the dictonary
student ={"first_name": "Manideep", "last_name": "Karne", "gender":"male", "age":"25", "marital status":"single"
, "skills":["java", "python","C"], "country":"india", "city":"hyderabad","address":"Saroornagar"}
print("student dictionary is :",student)
length_student = len(student)
print("the length of the student dictionary is :", len(student))
# getting skill type in  student dictionary
print("skills and type of skill is :",type(student['skills']))
#adding more values to the skills in student dictionary
student["skills"].append(" Java Scripts ")
print("SKills in student dictionary are: ", student["skills"])
# printing dictionary keys as list
print(student.keys())
# printing dictionary values as list
print(student.values())