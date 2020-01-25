'''
n – number of lines for the pattern, integer (int)
 * summary   : This method prints number pattern of integers using recursion
 * For example n = 5 will display the output as:
 * 54321
 * 4321
 * 321
 * 21
 * 1
 * returns      : N/A
 * return type  : void
 '''

n = 7

for i in range(n,0,-1):
    print(i, end=" ")
    n = n - 1
    for