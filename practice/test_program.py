# import keyword

# print (keyword.kwlist)

# a, b = 5, 10

# a, b = b, a

# print(a, b)

# d = float(input("Enter a number: "))
# print(f"Before typecased: {d}, type: {type(d)}")
# d = int(d)
# print(f"After typecased: {d}, type: {type(d)}")

# num = str(input("Enter a number: "))
# print(f"Before typecased: {num}, type: {type(num)}")
# num = int(num)
# print(f"After typecased: {num%2}, type: {type(num)}")

# num = int(input("Enter first number: "))
# summation = 0

# for i in range(1,num+1):
#     summation += i
#     print(f"i: {i}, summation: {summation}")

#print(f"The sum of first {num} natural numbers is: {sum}")

# a = 6
# b = 4
# c = "&"

# result= str(a)*a + c +str(b)*b
# print(result)
# name = "rahul"
# half = len(name)//2
# print(len(name))
# print(half)
# print(name[half:])
# print(name[:half])
# print(name[half+1:])
# sym = name[half:] == name[:half] if len(name) % 2 == 0 else name[half+1:] == name[:half]
# print(sym)

# pal = name == name[::-1]
# print("Symmetrical" if sym else "Not Symmetrical")
# print("Palindrome" if pal else "Not Palindrome")

# word = "as"

# if word in keyword.kwlist:
#     print(f"{word} is a keyword")
# else:
#     print(f"{word} is not a keyword")

# test_list = [1, 2, 3, 4, 5]
# test_tuple = (1, 2, 3, 4, 5)

# print(test_list)
# print("\n")
# print(test_tuple)
# print("\n")

# test_list[0] = 10
# print(test_list)
# print("\n")
# test_tuple[0] = 10
# print(test_tuple)

# print(type(True))
# print(type(False))
# print(type(TRUE))

set1 = set(["Geeks", "For", "Geeks"]) #Duplicates are removed automatically
print(set1) 

# loop through set
for i in set1:
   print(i, end=" ") #prints elements one by one
  
# check if item exist in set   
print("Geeks" in set1)

