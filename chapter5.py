''' This is assignment 5 to test basic of loops '''
 

for num in range(1,101):
                prime = False
                if num%3 == 0 and num%5 == 0:
                    print('FizzBuzz')
                elif num%5 == 0:
                    print('Buzz')
                elif num%3 == 0:
                    print('Fizz')
                elif num>1:
                    for i in range(2,num):
                        if num%i == 0:
                            prime = False
                            break
                        else:
                            prime = True
                    if prime:
                        print(num,' is Prime')
                    