#Case 4: Write a program for the given tuple of elements add into list and Read Elements from list.
#Solution:
def assign_elements(tupleobject):
    list=[]
    for item in tupleobject:
        list.append(item)
    print(list)
 
# Execute Execution
tup_elements=(40,60,"Mango","Lotus",12.75,True)
assign_elements(tup_elements)