#Case 1: Declare an Integer array , Read Elements from Integer Array.
import array
 
arr=array.array("i", [20,10,30,50,40])
print(arr)
# Read Elements
for element in arr:
    print(element, end=" ")