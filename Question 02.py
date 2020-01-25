# Take a user input 'n' as an integer value
n = eval(input("Enter number of elements to display: "))

# initiate 'sum' variable to 0
sum = 0

# display output
if n < 1:                                          # check for valid input
    print("error: Enter number greater than 1")    # if user asks for less than 1 digit
else:                                              # display error
    for i in range(1,n+1):                         # from 1 to user input 'n'
        sum = sum + i                              # increase the sum by that value
        print(sum, end=" ")                        # display the sum and a " " space after it