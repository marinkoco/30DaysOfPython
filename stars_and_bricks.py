for i in range(3):
    for j in range(3):
        print('#', end='')
    print()
# In this code, the end parameter of the print() function is set to a space character instead of the default newline character. 
# This means that each # symbol will be followed by a space instead of a newline. 
# After each inner loop has completed, the outer loop then prints a newline character to move to the next row. 
# This will output the # symbols in a 3x3 grid pattern, like this:
###
###
###
for i in range(3,0,-1):
    for j in range(i):
        print('#', end='')
    print()
###
##
#
n=4
for i in range(0,n,1):
    for j in range(i):
        print('#', end='')
    print()
#
##
### 
n=5
for i in range(0,5):
	for j in range(0,5-i-1):
		print(end=' ')
	for j in  range(0, i+1):
		print('*', end=' ')
	print()
#    * 
#   * * 
#  * * * 
# * * * * 
#* * * * * 

n = 5
k = 8
for i in range(0, n):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 

rows = 5
for i in range (0, rows):
    for j in range(0, i + 1):
        print("* ", end='')
    print("\r")
for i in range (rows, 0, -1):
    for j in range(0, i -1):
        print("* ", end='')
    print("\r")
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 