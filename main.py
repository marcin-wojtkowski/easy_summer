'''
    Stage 1
        Prompt user to input a number
    Stage 2
        Continuous summation

        2a
            Fix the bug where a string input will cause a compiler error.
        FIXED


'''

print('Easy Summer')

sum = 0
list = []

while(True):
    variable = input()

    if variable.isdigit():
        if len(list) == 0:
            list.append(variable)
        else:
            list.append(' + ' + variable)

        for x in list:
            print(x, end = '')

        sum += int(variable)

        print('\nSum: ' + str(sum))
    elif variable == 'quit':
        break
    else:
        print('Invalid input detected')
