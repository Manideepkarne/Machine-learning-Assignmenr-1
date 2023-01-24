import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort() # sorting the ages list
minimum_ages = min(ages) # finding the minimum age in the list
print("the minimum age in the list is : ",  minimum_ages)
maximum_ages = max(ages) # finding maximum age in the list
print("the maximum age in the list is :", maximum_ages)
ages.append(minimum_ages) # adding the minimum age to the list
ages.append(maximum_ages) # adding the maximum age to the list
print("the elements after adding the min and max ages:", ages)
# finding the median of ages
median_ages = statistics.median (ages)
print("the median of the ages is :", median_ages)
# finding the average of ages
average = sum(ages)/len(ages)
print("the  average of the ages is :", average) # printing the average of ages list
range = (maximum_ages - minimum_ages) # finding range of ages list
print("the range of the ages :", range)   #printing the rangee of ages