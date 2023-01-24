it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
length_of_companies = len (it_companies) # finding length of the companies set
print(length_of_companies) # printing length of companies
it_companies.add("Twitter") # adding twitter to companies set
print(it_companies) # printing it companies
new_it_companies ={"Dell" , "netflix", "TCS"} # new companies that has to be added to set
it_companies.update(new_it_companies) # updating new it companies to the set
print("list after adding new companies" , it_companies) # printing new companies
it_companies.remove("Apple") # removing one company from it companies
print("after removing one company from the list", it_companies)
# joining A and B
A_join_B = A.union(B)
print("union of A and B:", A_join_B)
#intersection of the A and B
A_intersection_of_B = A.intersection(B)
print("intersection of A and B:", A_intersection_of_B)
# finding is A is subset of B
print("A is subset of B:", A.issubset(B))
#is A is a disjoin of B
print ("A is a disjoin st of B:" , A.isdisjoint(B))
# joining A and B
print("joining A with B ", A.union(B))
#joining B with A
print("joining B with A ", B.union(A))
# symetric difference of A and B
print("symmetric difference between A and B :", A.symmetric_difference(B))
#clearing A and B
A.clear
B.clear
# converting age to the set
newageset=set(age)
print("length of age list is:",len(age))
print("age set is:",newageset)




