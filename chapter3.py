'''This program demonstrates use of function and if statement'''

 

# Function to accept three values and compare them

def compareVals(val1,val2,val3):

                cmp = False

                if round(int(val1)) == round(int(val2)):

                                print('value of parameters 1 and 2 are equal')

                                cmp = True

                                return cmp

                elif round(int(val1)) == round(int(val3)):

                                print (round(int(val1)))

                                print (round(int(val3)))

                                print('value of parameters 1 and 3 are equal')

                                cmp = True

                                return cmp

                elif round(int(val2)) == round(int(val3)):

                                print('value of parameters 2 and 3 are equal')

                                cmp = True

                                return cmp

                else:

                                print('None of the parameters are equal')

                                cmp = False

                                return cmp

                               

 

print('\nLets compare three values...')

result = compareVals(1,2,3)

print('The result of comparison is: ',result)

print('\n')

result = compareVals(1,2,2)

print('The result of comparison is: ',result)

print('\n')

result = compareVals(1,2,1)

print('The result of comparison is: ',result)

print('\n')

result = compareVals(1,2,'1')

print('The result of comparison is: ',result)

print('\n')

result = compareVals('1',2,'1')

print('The result of comparison is: ',result)

print('\n')

result = compareVals('2',2,'1')

print('The result of comparison is: ',result)

print('\n')

result = compareVals('-1',2,'1')

print('The result of comparison is: ',result)

print('\n')

result = compareVals(0.01,2,0.6)

print('The result of comparison is: ',result)

print('\n')