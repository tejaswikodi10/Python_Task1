#Dictionaries Declaring 
my_dict={"1":"Black","2":"Pink"}
print(my_dict)
#Add a key-value pair to the dictionary 
my_dict[3]="White"
print(my_dict)
#Remove a value with  its corresponding key from the dictionary 
my_dict.pop("1") 
print(my_dict)
#Length of the Dictionary 
print(len(my_dict))

#Creating a List
my_list=["Chocolate","Blackcurrent","Orange"]
print(my_list)
#Accessing elements in the list by index Value
print(my_list[1])
#Append an element at the end of the List
my_list.append("Butterscotch")
print(my_list)
#Insert an element at any given position in the List
my_list.insert(0,"Pista")
print(my_list)
#Remove an element from the List using its index
del my_list[2]
print(my_list)

#Declaring Set
my_set={"Moblie","Laptop","TV","WashingMachine"}
print(my_set)
#Append an element to the Set
my_set.add("AC")
print(my_set)
#Remove an element from the Set
my_set.remove("WashingMachine")
print(my_set)
#Length Of the Set
print(len(my_set))