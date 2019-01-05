'''This is my seventh assginment'''

# Declaring variables

mySongList = {'song_name':'Swaye shree Ram prabhu aikati','artist_name':'Sudhir Phadake','gener_name':'bhakti-geet','year': 1965,'composed_by':'G.D.Madgulkar','no_of_copies': 100000}

 

print('My favorite song and its information is as below..')

print('-----------------------------------------------')

for key in mySongList:

                print(key,'-->',mySongList[key])

 

 

print('Let’s play a guessing game..')

 

try:

                key = input('Can you guess name of any item in my album: ')

                value = input('Can you guess value of that item you guessed: ')

 

                if(mySongList[key]):

                                if(mySongList[key] == value):

                                                print('Your guess about item ',key,' and its value ',value,'is correct')

                                else:

                                                print('Your guess about item ',key,' is correct but it\'s value ',value,'is incorrect')

                else:

                                print('Your guess about item ',key,' is incorrect')

except KeyError:

                print('Your guess about item ',key,' is incorrect')