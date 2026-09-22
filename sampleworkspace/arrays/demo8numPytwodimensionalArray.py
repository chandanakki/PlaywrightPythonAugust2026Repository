#Case 1: Declare Two Dimensional array and Find the Rows and Columns Size.
 
import numpy as np
 
a=np.array([
    [1,2,3],
    [4,5,6]
])
# Number of Rows
print(len(a))
# Number of Columns 
print(a[0].size)
 
# Read Elements
for i in range(0,len(a)):
    for j in range(0,a[0].size):
        print(a[i][j], end=" ")
    print()