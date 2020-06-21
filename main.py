'''
    Stage 1
        Prompt user to input a number
    Stage 2
        Continuous summation

        2a
            Fix the bug where a string input will cause a compiler error.
        FIXED
    Stage 3
        Add subtraction
            #converting user input into float made working with numbers much easier
            instead of converting back and forth from string to int.
'''

print('Easy Summer')

sum = 0
list = []

while(True):

    variable = input()

    try:
        if variable == 'quit':
            break
        f = float(variable)

        if len(list) == 0:
            list.append(f)
        elif f < 0:
            list.append(' - ' + str(abs(f)))
            #elif exists to properly format summation history
        else:
            list.append(' + ' + str(f))

        for x in list:
            print(x, end = '')

        sum += f

        print('\nSum: ', sum)


    except ValueError:
        print('Invalid input')
