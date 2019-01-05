''' This is assignment 5 to test basic of loops '''
 

for num in range(1,10):
                prime = False
                if num%3 == 0 and num%5 == 0:
                                print('FizzBuzz')
                                print(num)
                elif num%5 == 0:
                                print('Buzz')
                                print(num)
                elif num%3 == 0:
                                print('Fizz')
                                print(num)
                elif num>1:
                                for i in range(2,num):
                                                if num%i == 0:
                                                                print('Prime flag is ',prime)
                                                                print(num)
                                                                break
                                                elif (num%i != 0) and (num%num == 0):
                                                                prime = True
                                if prime == True:
                                                print(num)
                                                print(num,' is Prime')