No_of_students = int(input("enter number of students: "))
weight_lbs = []
weight_kgs = []
print("enter weight of each students")
for t in range(No_of_students):
    student_weight = int(input(str(t+1)+". student weight:")) #assining student weight value to the list
    weight_lbs.append(student_weight)
    weight_kgs.append(float("{: .2f}" . format (student_weight * 0.453))) # converting weight from lbs to kgs
print ("weight of student in lbs :", weight_lbs)
print("weight of student in kgs :", weight_kgs)
