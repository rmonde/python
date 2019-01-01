'''This program illustrates the use of list '''

 

# gloabl variable declaration

myUniqueList = []

myLeftovers = []

 

print('Printing gloabl list for the first time: ',myUniqueList)

 

def elementAdditionToList(element):

                if element in myUniqueList:

                                addRejectedItems(element)

                                return False

                else:

                                print('Addig new element to the list: ',element,' at postion: ',len(myUniqueList)+1)

                                myUniqueList.append(element)

                                return True

                               

                               

def addRejectedItems(element):

                myLeftovers.append(element)

               

 

print('Lets add element to the list')

if elementAdditionToList(1) == True:

                print('New element added to myUniqueList')

else:

                print('New element added to myLeftovers due to non-uniqueness')

               

if elementAdditionToList('two') == True:

                print('New element added to myUniqueList')

else:

                print('New element added to myLeftovers due to non-uniqueness')

 

if elementAdditionToList(55.5) == True:

                print('New element added to myUniqueList')

else:

                print('New element added to myLeftovers due to non-uniqueness')

 

if elementAdditionToList((10+11)) == True:

                print('New element added to myUniqueList')

else:

                print('New element added to myLeftovers due to non-uniqueness')

               

if elementAdditionToList((10-11)) == True:

                print('New element added to myUniqueList')

else:

                print('New element added to myLeftovers due to non-uniqueness')

 

if elementAdditionToList(1) == True:

                print('New element added to myUniqueList')

else:

                print('New element added to myLeftovers due to non-uniqueness')

               

myUniqueList[2] = ['Hello']

 

if elementAdditionToList(['Hello']) == True:

                print('New element added to myUniqueList')

else:

                print('New element added to myLeftovers due to non-uniqueness')

 

print('Listing down myUniqueList list content: ',myUniqueList)

print('Listing down myLeftovers list content: ',myLeftovers)