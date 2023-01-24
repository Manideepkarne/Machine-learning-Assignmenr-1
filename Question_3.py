sisters=('puppy','chinni','bunny') # sisters tuple
brothers=('deepu','manoj') # brothers tuple
siblings=brothers+sisters  # adding sisters and brothers tuple
print(siblings) # printing siblings tuple
length = len(siblings)
print('no of siblings are: ', length)
new_list = list(siblings)
new_list.append('lokesh') # adding father name to the list
new_list.append ('renuka') # adding mother name to the list
new_tuple = tuple(new_list) # created new tuple to convert the list to tuple
family_members = new_tuple # assigning value in tuple to family_member varibale
print(family_members) #printing family members