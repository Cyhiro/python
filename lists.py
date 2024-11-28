#this is an empty list
my_list=[]
#appending the list by adding values
new_list=[10,20,30,40]
my_list.append(new_list)
my_list=new_list
#inserting the value '15'at the second position
my_list.insert(1,15)
#extending my_list
new_list.extend([50,60,70])
#removing last element from list
my_list.pop()
#sorting the list
my_list.sort()
#finds and prints index of value
print(f'The index of 30 is',my_list.index(30))
#my_list()

