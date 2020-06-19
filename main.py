'''
    Stage 1
        Prompt user to input a number
    Stage 2
        Continuous summation

        2a
            Fix the bug where a string input will cause a compiler error.

'''

print('Easy Summer')

sum = 0
list = []

while(True):
    variable = input()



    if variable == 'quit':
        break
    else:
        list.append(variable + ' + ')
        for x in list:
            print(x, end = '')

        variable = int(variable)

    sum += variable


    print(sum)
