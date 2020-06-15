def get_names():
    newlist=[]
    while len(newlist) <5 :
        name = input("Enter the name of an element: ")
        if name == "":
            print("empty strings are not allowed")
        elif name not in newlist:
            newlist.append(name)
        else:
            print(name+ " was already entered")
    return newlist

elementen_file = open("elements1_20.csv","r+")
element=elementen_file.readline()
elementen=[]
while element !="":
    elementen.append(element.strip().lower())
    element=elementen_file.readline()
correct_responses=[]
false_responses=[]
responses=get_names()
for response in responses:
    if response in elementen:
        correct_responses.append(response)
    else:
        false_responses.append(response)


print(len(correct_responses)*20, end="") 
print(" % correct")
print("Found: " + " ".join([ word.title() for word in correct_responses]))
print("Not found:  " + " ".join([word.title() for word in false_responses]))






