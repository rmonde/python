'''Assignment demonstrating use of functions'''

def getArtist():
    print('Artist name is Sudhir Phadake')

def getGener():
    print('The gener name is Bhakti Geete')

def getYrofPublish():
    print('The year of publishing is 1965')


print('\nHere is some information about my favorite song...')
getArtist()
getGener()
getYrofPublish()

print('Some more examples of function...')
oddEven = ''
def evenNumber(num):
    flag = True
    if num % 2 == 0:
        print('Number is even')
        return flag
    else:
        print('Number is odd')
        flag = False
        return flag

print('Let\'s test boolean return type for a function...')
print('The return flag is: ',evenNumber(2))
myFavNum = 7
print('The return flag is: ',evenNumber(myFavNum))
print('The return flag is: ',evenNumber(myFavNum+1))
print('The return flag is: ',evenNumber((myFavNum+1)/2))