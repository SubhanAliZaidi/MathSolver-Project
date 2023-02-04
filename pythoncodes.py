# Naziya = "Naziya"
# print('\U0001F60D')
# print(169**0.005)
# print(round(169**0.005,6))
# print("I\'m \\n subhan ali")
# print(32**2)
# print(5124/83)
# print(round(5124/83,85))
# print(485**4)
# print(4/5)


# usd = 75.5
# euros = 80
# inr = 1
# diram = 17
# print("usd,\neuros,\ninr,\ndiram,")

# number1 = 1
# number2 = 2
# Mumber3 = 4
# print(number1, number2, Mumber3)

# name = "Subhan"
# sirname = "Ali"
# lastname = "Zaidi"
# print(name,sirname,lastname)

# print("I\'m Subhan Ali")

# name = "subhan"
# print(name)
# name = "ali"
# print(name)

# subhan = "ali"
# print(subhan)

# print("\n")
# print(22/7)
# print('\n')
# print(484**4)

# print("Subhan 3 Ali 4")
# first_name = "Subhan"
# last_name = "Ali"
# full_name = first_name + last_name

# print(first_name + ' ' + "3" + " " + last_name + " " + str(4))

# print(full_name*5 + last_name *5)

# name = input('what is your name ')
# hello = 'hello '
# print(hello + name)

# age = input("Enter your age here ")
# print('You are ' + age + ' year old')

# number_one = float(input('enter first number '))
# number_two = float(input('enter second number '))
# total = number_one + number_two
# print('total is ' + str(total))

# age, name, address = "18", "Subhan Ali Zaidi ", "138A/12"
# print("Hello " + name + " your age is " + age + " you live in " + address )
# friend_name, work = "ashish prajapati", "computer operator"
# crush_name = "Naziya Parveen"
# Insta_id = "Naziya.14_"
# print(f"My Crush Name is {crush_name} .She Is So Cute. Her Instagram Id is {Insta_id}")

# age, name, address = 24, "Subhan Ali Zaidi", "138A/12"
# print(f"Hello {name} your age is {age} and you live in {address} after 20 year your age will be {age+20}")


# number1, number2, number3 = input("Enter three Values with comma separated : ").split(",")
# print(f"averages of three digits is {(int(number1) + int(number2) + int(number3)) /3}")

# name = input("Enter Your Name : ")
# print("Reverse of your name is " + name[ : :-1])

# name = input("Enter Your Name : ")
# print(f"Reverse Of Your Name is : {name[::-1]}")


# name = input("Enter Your Name : ")
# print(len(name))
# print(f"Your Name in Uppercase : {name.upper()}")
# print(f"Your Name in Lowercase : {name.lower()}")
# print(f"Your Name in Titlecase : {name.title()}")


# name, char = input("Enter Your Name And Character Comma Seperated : ").split(",")
# name1 = len(name)
# print(f"Length of your name is : {name1}")
# name2 = name.lower()
# char1 = char.lower()
# char2 = name2.count(char1)
# print(f"{char2}")


# print(f"Character Count : {name.lower().count(char.lower())}")

# name, char = input("Enter Your Name and Character Comma Seperated : ").split(",")
# name1 = name.replace(" ", "")
# print(f"Length Of Your Name is : {len(name1.strip())}")
# print(f"Character Count is : {name.lower().strip().count(char.lower().strip())}")


# # name.lower().strip().count(Char.lower().strip())
# # Char.lower().strip()

# number1, number2 = input("First no. and Second no. : ").split(",")
# print(str(number1) + str(number2))


# number, number2 = input("Enter First Value and Second Value : ").split()
# # total = number + number2
# print(number + number2)


# name = input("Enter Your Name : ")
# print(name.center(len(name)+10, "*"))


# password = input('Please Enter At Least 8 Digit : ')
# if len(password) >= 8:
#     print("You Can Enter This Password")
# else:
#     print("Enter Minimum 8 Character Long")


# winning_number = 34
# guess_number = input('Enter Any Number : ')
# guess_number = int(guess_number)    #if Want to remove this line give string in winning_number
# if guess_number == winning_number:
#     print("You Win!")
# else:
#     if guess_number > winning_number:
#         print("Too High")
#     else:
#         print("Too Low")


# user_name = input('Enter Your Name : ')
# age = input("Enter Your Age : ")
# age = int(age)
# name = user_name[0:1]
# name = name.lower()
# if name == "a" and age >= 10:
#     print("You Can Watch Coco Movie")
# else:
#     print("Sorry, You Can't Watch Coco Movie")


# i = 1
# while i <=100000:
#     print(f"naziya {i}")
#     i = i + 1

# Total = 0
# Variable = 1
# while Variable <=10:
#     Total = Total + Variable
#     Variable = Variable + 1
# print(Total)


# user_input = input('Enter Any Number : ')
# user_input = int(user_input)
# total = 0
# variable = 1
# while variable <= user_input:
#     total = total + variable
#     variable = variable + 1
# print(total)

# total = int(user_input[0]) + int(user_input[1]) + int(user_input[2]) + int(user_input[3]) + int(user_input[4])
# total1 = int(user_input[0]) + int(user_input[1]) + int(user_input[2])+ int(user_input[3])
# total2 = int(user_input[0]) + int(user_input[1]) + int(user_input[2])
# total3 = int(user_input[0]) + int(user_input[1])


# user_input = input("Enter any Four Digit Number : ")

# if len(user_input) == 5:
#     print(int(user_input[0]) + int(user_input[1]) + int(user_input[2]) + int(user_input[3]) + int(user_input[4]))
# else:
#     if len(user_input) == 4:
#         print(int(user_input[0]) + int(user_input[1]) + int(user_input[2])+ int(user_input[3]))
#     else:
#         if len(user_input) == 3:
#             print(int(user_input[0]) + int(user_input[1]) + int(user_input[2]))
#         else:
#             if len(user_input) == 2:
#                 print(int(user_input[0]) + int(user_input[1]))
#             else:
#                 if len(user_input) == 1:
#                     print(int(user_input[0]))



# number = input('Enter any Number : ')
# total = 0
# i = 0
# while i < len(number):
#     total += int(number[i])
#     i += 1
# print(total)

# temp_var = ""
# name = input('Enter Your Name : ')
# i = 0
# while i < len(name):
#     if name[i] not in temp_var:
#         temp_var = temp_var + name[i]
#         print(f"{name[i]} : {name.count(name[i])}")
#     i = i + 1



# var = 0
# while var == var:
#     print('Naziya')
#     var += 1



# while True:
#     print('Naziya Parveen')


# for NAZIYA in range(101):
#     print(f'Naziya Parveen{NAZIYA}')


# user_input = input("Enter any number : ")
# user_input = int(user_input)
# number = 0
# for i in range(0, user_input + 1):
#     number += i
# print(number)


# user_input = input("Enter Any Number : ")
# total = 0
# for i in range(0, len(user_input)):
#     total += int(user_input[i])
# print(total)


# name = input("Enter Your Name : ")
# total = ""
# for i in range(0, len(name)):
#     if name[i] not in total:
#         print(f"{name[i]} : {name.count(name[i])}")
#         total += name[i]


# name = "Naziya Parveen"
# i = 0
# while i<=10:
#     print(f"{name}\t{name}\t{name}") 
#     i+=1


# name = "Naziya Parveen"
# for i in range(0,11):
#     print(i)


# for i in range(1,100):
#     if i == 50:
#         continue
#     if i == 60:
#         continue
#     print(i)


# for i in range(5,25):
#     if i == 20:
#         break
#     print(i)



# guess = 1
# import random
# from types import EllipsisType
# Winning_num = random.randint(1,100)
# user_input = int(input('Enter Any Number Between 1 To 100 : '))
# game_over = False
# while not game_over:
#     if user_input == Winning_num:
#         print(f"You Win This Game In {guess} time")
#         game_over = True
#     else:
#         if user_input < Winning_num:
#             print("Too Low")
#             guess += 1
#             user_input = int(input('Try Again : '))
#         else:
#             print("Too High")
#             guess +=1
#             user_input = int(input('Try Again : '))

# for i in range(10,-4,-1):
#     print(i)


# guess = 1
# import random
# winning_number = random.randint(1, 100)
# user_input = int(input("Enter Any Number From 1 To 100 : "))
# game_over = False

# while not game_over:
#     if user_input == winning_number:
#         print(f"You Win This Game in {guess} Times")
#         game_over = True
#     else:
#         if user_input < winning_number:
#             print("Too Low")
#         else:
#             print("Too High")
#         guess += 1
#         user_input = int(input("Please Try Again : "))



# num = input('Enter Any Number : ')
# total = 0
# for i in num:
#     total += int(i)
# print(total)



# guess = 1
# import random
# number = random.randint(1,500)
# input1 = int(input("Enter Any Number From 1 To 500 : "))
# game_over = False
# while not game_over:
#     if input1 == number:
#         print(f"You win this game in {guess} time")
#         game_over = True
#     else:
#         if input1 < number:
#             print("Too Low")
#         else:
#             print("Too High")
#         guess += 1
#         input1 = int(input("Please Try Again : "))



# def add(x,y):
#     return x + y

# num1, num2 = input("Enter Any Two Number + Seperated : ").split("+")
# num1 = float(num1)
# num2 = float(num2)
# total = add(num1, num2)
# print(total)



# def add(x,y,z):
#     return x + y + z

# num1, num2, num3 = input("Enter Any Two Number + Seperated : ").split("+")
# num1 = float(num1)
# num2 = float(num2)
# num3 = float(num3)
# total = add(num1, num2, num3)
# print(total)



# def bigger_number(x,y):
#     if x > y:
#         print(f'{x} is bigger')
#     else:
#         print(f'{y} is bigger')
# num1, num2 = input("Enter Any Two Number + Seperated : ").split(",")
# num1 = int(num1)
# num2 = int(num2)
# bigger = bigger_number(num1,num2)




# def bigger_number(x,y,z):
#     if x > y and x > z:
#         return(x)
#     else:
#         if y > x and y > z:
#             return(y)
#         else:
#             if z > x and z > y:
#                 return(z)
#             else:
#                 return("All are same value")

# num1, num2, num3 = input("Enter Any Two Number + Seperated : ").split(",")
# num1 = int(num1)
# num2 = int(num2)
# num3 = int(num3)
# bigger = bigger_number(num1,num2,num3)
# print(bigger)



# def is_palidrom(x):
#     palidrom = (user_input [::-1])
#     if user_input == palidrom:
#         return (True)
#     else:
#         return(False)

# user_input = input("Enter Any Palidrom Word : ")
# palidrom1 = is_palidrom(user_input)
# print(palidrom1)



# def fibonnaci_seq(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     elif n == 2:
#         print(a, b)
#     else:
#         print(a, b, end = " ")
#         for i in range(n-2):
#             c = a + b
#             a = b
#             b = c
#             print(b , end = " ")

# user_input = input("Enter Any Number : ")
# no = int(user_input)
# no2 = fibonnaci_seq(no)



# user_input = input("Enter Any Number : ")
# a = 0
# b = 1
# if user_input == 1:
#     print(a)
# elif user_input == 2:
#     print(b)
# else:
#     if i in range(user_input):
#         a = 1


# vegetables = ["Carrot" , "ladyfinger" , "onion"]
# fruits = ["Apple" , "Mango" , "guava"]
# fruits.insert(2 ,  "Banana")
# vegetables.append("Bottleguard")
# mixed = fruits + vegetables
# print(mixed)
# print(f"{fruits + vegetables}")



# vegetables = ["Carrot" ,'Brinjal' , "ladyfinger" , "onion" , "Apple"]
# vegetables.sort()
# print(vegetables)
# vegetables.append("onion")
# print(vegetables.count("onion"))
# print(vegetables)



# count                 =         fruits.count()
# sort method           =         fruits.sort()    OR   numbers.sort()
# sorted function       =         print(sorted(fruits))
# reverse               =         fruits.reverse()
# Clear                 =         fruits.clear()
# copy                  =         numbers.copy()
# insert                =         fruits.insert(2, "mango")
# append                =         fruits.append()    
# extend                =         fruits.extend()



# user_info = ["Naziya Parveen" , "18"]
# print(",".join(user_info))



# user_name = ["subhan ali" , "ashish prajapati" , "gaurav chaurasiya" , "subhan ali" , "prince soni"]
# for name in user_name:
#     print(f'{name.upper()}', end = "\t")


# matrix = [[1,2,3] , [4,5,6] , [7,8,9]]
# for i in matrix:
#     print(i)



# matrix = [[1,2,3] , [4,5,6] , [7,8,9]]
# for sublist in matrix:
#     for i in sublist:
#         print(i)
# print(matrix[1][0])
# print(type(matrix))

# number = list(range(1,102))
# number1 = number
# print(number1)


# def square_list(l):
#     sqre = []
#     for i in l:
#         sqre.append(i**2)
#     return sqre


# num = list(range(1,20))
# # num = list(range(1,6))
# square = square_list(num)
# print(square)



# def reverse_list(l):
#     reversed = []
#     for i in range(len(l)):
#         popped_item = l.pop()
#         reversed.append(popped_item)
#     return reversed


# num = list(range(1,11))
# rvrs = reverse_list(num)
# # print(num)




# def reverse_list(l):
# 	r_list = []
# 	for i in range(len(l)):
# 		popped_item = l.pop()
# 		r_list.append(popped_item)
# 	return r_list

# numbers = [1,2,3,4]



# x = list(int(input("Enter X Coloum with Comma Seperated : ").split(" ")))
# print(x)
# x1 = int(x)
# f = input("Enter f Coloum with Comma Seperated : ")



# # try block to handle the exception
# try:
# 	my_list = []
	
# 	while True:
# 		my_list.append(int(input()))
		
# # if the input is not-integer, just print the list
# except:
# 	print(my_list)

# number of elements
# n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
# a = list(map(int,input("Enter the numbers : ").strip().split()))

# print("List is - ", a)





# x = [int(item) for item in input("Enter the list items : ").split()]
# print(f"{y}")
# # f = list(map(int,input("Enter F Coloum (Space Seperated) : ").split(" ")))
# # if len(f) == len(x):
# #     print(f)
# # else:
# #     print("Frequency len is not matching with x length")


# # y = x
# i = sum(y)
# print(i)

# y = sum(f)
# print(y)

# def add_list(l):
#     y = []
#     for i in range(0,l):
#         sigmaX = int(l[0])
#         # y += sigmaX

# x = list(input("Enter X Coloum (Space Seperated) : ").split(" "))
# total = add_list(x)
# print(total)


# import random
# assumed_mean = random.choice(x)
# print(f"Assumed Mean = {assumed_mean}")


# x = list(map(int,input("Enter X Coloum (Space Seperated) : ").split(" ")))
# y = x
# i = sum(y)
# print(x)
# print(f"\nEnter 0 If There is No F Coloumn")
# f = list(map(int,input("Enter F Coloum (Space Seperated) : ").split(" ")))
# if len(f) == len(x):
#     z = f
#     o = sum(z)
#     print(f)
#     print(f"Summation X = {i}")
#     print(f"Summation F = {o}")

#     na = 0
#     da = []
#     for i in range(len(x)):
#         fx = (x[na] * f[na])
#         na += 1
#         da.append(fx)
#     print(f"FX = {da}")

#     sumda = sum(da)
#     print(f"Summation FX = {sumda}")
#     assumed_mean = (sumda/o)
#     print(f"Mean = {assumed_mean}")


#     d = []
#     t = 0
#     for i in range(len(x)):
#         d1 = x[t] - assumed_mean
#         d.append(d1)
#         t += 1
#     print(f"Deviation (D) = {d}")

#     deviation_square = d
#     deviation_square1 = []
#     naz = 0
#     for i in range(len(d)):
#         square = (deviation_square[naz]**2)
#         naz += 1
#         deviation_square1.append(square)
#     print(f"Deviation Square : {deviation_square1}")

#     summation_Deviation = sum(deviation_square1)

#     napa = []
#     naziya = 0

#     for i in range(len(f)):
#         f_dsquare = (f[naziya] * deviation_square1[naziya])
#         napa.append(f_dsquare)
#         naziya += 1
#     print(f"F.Dsquare : {napa}")


#     sigmadeviation = sum(napa)
#     print(f"Summation of Deviation = {summation_Deviation}")
#     print(f"Summmation of FDsquare = {sigmadeviation}")

#     standard_deviation = (sigmadeviation/o)
#     print(f"{standard_deviation}")
#     import math
#     Sd = math.sqrt(standard_deviation)
#     print(f"STANDARD DEVIATION OF DISCRETE SERIES IS = {Sd} \n\n\t\t\t\t\t Solved By - Subhan Ali")


# else:
#     if f == [0]:
#         print("\nThis is Individual Series")
#         print(f"\nSummation X = {i}")
#         print(f"Number Of X Item (N) = {len(x)}")

#         indi_series = (i/len(x))
#         import math
#         sd = math.sqrt(indi_series)
#         print(f"STANDARD DEVIATION OF INDIVIDUAL SERIES IS = {sd} \n\n\t\t\t\t\t Solved By - Subhan Ali")

#     else:
#         if len(x) is not len(f):
#             print(f"\nLENGTH OF X COLOUMN IS NOT MATCHING WITH F COLOUMN , PLEASE ENTER SAME AMOUNT OF ELEMENTS \n\n \t\t\t - Developer SUBHAN ALI")



# def reverse_list(l):
#     d = []
#     for i in l:
#         reverse = i[::-1]
#         d.append(reverse)
#     print(d)


# x = ['abc' , 'def' , 'ghi' , 'jkl']
# y = reverse_list(x)


# def odd_even_list(f):
#     odd_list = []
#     even_list = []
#     for i in f:
#         if i % 2 == 0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
#     output = [odd_list , even_list]
#     print(output)

# li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# odd_even_list(li)
    


# def common_number(f , y):
#     cnum = []
#     for i in f:
#         if i in y:
#             cnum.append(i)
#     print(cnum)

# li , yi = [1,2,3,4,5,8] , [1,2,3,1,9,12,8]
# hi = common_number(li, yi)



# def difference(l):
#     min_num = min(l)
#     max_num = max(l)
#     diff = (max_num - min_num)
#     return diff

# hii = list(range(1,50 + 1))
# print(difference(hii))



# def list_num(k):
#     c = 0
#     for i in k:
#         if type(i) == list:
#             c += 1
#     return c

# x = [1,2,3, [5,6,4],[7,8,9]]
# print(list_num(x))



# d = 1
# f = "Impossible To Stop"
# while d <= 2:
#     print(f)
#     d += 1


# tuples are immutable you can change value of it
# tuples = (1 , 2 , 3 , 4 , 5)
# tuples data type can be anything
# with pop , insert, append ,remove, or del
# we can only use count method and index method or len function

# in function if returning two Values
# it will be in tuples

# you can create two variable variable to get function return two values without tuples



# from subprocess import HIGH_PRIORITY_CLASS
# from turtle import hideturtle
# import pyautogui, time
# time.sleep(5)
# spam = "hii"
# t = 0
# while t <= len(spam):
#     # print(spam)
#     pyautogui.typewrite(spam)
#     pyautogui.press("enter")




# dictionary
# user = dict(name = "naziya" ,  last_name = "parveen")
# print(user['name'] , ["last_name"])


# user_info = dict(
#     name = "subhan",
#     age  = "19",

# )

# user_info['last_name'] = 'ali'
# print(user_info)



# user = dict(name = 'subhan ali' , 
            
#             )

# print(user)

# hobbies = {"hobbie" : ['reading books' , 'coding' , 'photoshop'],
#             "work" : 'computer operator' , 
#             'age' : 25 ,
# }

# user.update(hobbies)

# print(user)

# user.pop("age")
# print(user)

# user.popitem()
# print(user)



# fromkeys
# d = {'name': 'unknown' , 'age' : 'unknown'}
# d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
# print(d)


# getmethod (useful)
# dic = {'name': 'Subhan' ,
#         'age' : 'unknown'}
# print(dic["name"]) #just for reference

# print(dic.get('names'))

# dic.clear() #this will clear Dictionary

# d1 = dic.copy()  #to copy the dictionary




                # Cube Finder Program

# def cube_finder(n):
#     d = {}
#     for i in range(1,n+1):
#         d[i] = i**3
#     return(d)

# cube_finders = int(input('Enter Any Number : '))
# print(cube_finder(cube_finders))


# user = {}

# name = input("Enter Your Name : ")
# age = input("Enter Your Age : ")
# fav_movies = input("Enter Your Fav Movies Comma Seperated : ").split(",")
# fav_songs = input("Enter Your Fav Songs Comma Seperated : ").split(",")

#             USED TO TAKE INPUT FROM USER AND CONVERT IN DICTIONARY

# user["name"] = name
# user["age"] = age
# user["fav_movies"] = fav_movies
# user["fav_songs"] = fav_songs

# for i,y in user.items():
#     print(f'\n{i} : {y}')


#             TO CHECK SPECIAL KEYVALUE IN DICTIONARY

# for "name" in user:
    # print("anything")                       name = keyvalue of dictionary

# MAINLY PRINT A DATA IN DICTIONARY

# print(d["name"])            name = keyvalue

# Its better to use get method instead of upper method
# print(d.get("name") , Not Found!)


# TO PRINT ALL KEYS IN DICTIONARY

# for i in d:             d = dictionary
#     print(i)


# TO PRINT ALL VALUES IN DICTIONARY

# for i in d.values():        d = dictionary
#     print(i)


# TO DELETE OR POP DATA IN DICTIONARY

# popped = d.pop("name")
# print(popped)


# TO DELETE DATA FROM LAST IN DICTIONARY

# popped = d.popitem()
# print(popped)




#                         INTRODUCTION TO SET

# YOU CAN ONLY CONTAIN NUMBER, FLOAT NUMBER, OR STRING IN SET
# YOU CAN'T CONTAIN LIST OR DICTIONARY IN SET


# s = {1,2,3,4,5,6}           We Can't Use Same Item In Set , Like 2 Times 1
# print(s)                we can't use indexing in set like we did in list
#                         like print(s[1])  = This will give error

# set also removes duplicate item in list

# lis = [1,2,3,4,5,6,7,8,9,10,11,12,12,12,12,13,13,13]
# set1 = set(lis)
# print(set1)                     This Will Remove all duplicate in List


#         TO ADD DATE IN SET

# set1.add(20)
# print(Set1)                     This Will Add Data In Set

# set1.remove(1)                  This Will Delete Data In Set
# set1.discard(1)                 This Will Not Give Error If date in not available in set
# set1.clear()                      This Will Clear Everything in set
# set1.copy()                       This Will Copy The SEt


            # UNION IN SET
    
# S1 = {1,2,3,4,5}
# S2 = {5,8,9,78,5,4,1}

# IF WE WANT TO Make set without repeating number, WE WILL USE UNION

# UNION_sET = S1 | S2                 # We Use | (pipe) For union
# print(UNION_sET)


            # INTERSECTION

# S1 = {1,2,3,4,5}
# S2 = {5,8,9,78,5,4,1}

# intersection_set = S1 & S2              # We Use & (and) For intersection
# print(intersection_set)


# new_list2 = ['subhan', 'ali' , 'zaidi']

# new_list3 = [i[0] for i in new_list2]
# print(new_list3)



# def new_reverse(l):
#     return[i[::-1] for i in l] 

# new_list2 = ['subhan', 'ali' , 'zaidi']
# print(new_reverse(new_list2))



# from turtle import *
# speed(10)
# color("red")
# bgcolor("black")
# b = 200
# while b > 0:
#     right(b)
#     forward(b * 3)
#     b = b - 1


# x = int(12)
# print(int(x)*2)


# numbers = list(range(1,11))

# even_nums = [i for i in numbers if i%2 == 0]
# print(even_nums)

# odd_nums = [i for i in range(1,11) if i%2 == 1]
# print(odd_nums)




# def numbers_to_str(l):
#     return [str(i) for i in l if (type(i) == int or type(i) == float)]

# # input = ['subhan', 'ali' , 'zaidi' , True , False , [1.0 , 12 , 15]]
# print(numbers_to_str([True , False , [1.0 , 12 , 15], 1 , 2.0 , 15]))


# def new_list(l):
#     return [(i*2) if (i%2 == 0) else -i for i in l]

# lit = list(range(1,11))
# var = new_list(lit)
# print(var)


# new_list = [[i for i in range(1,4)] for i in range(5)]
# print(new_list)



# new = [i**2 for i in range(1,11)]
# print(new)


# even = [i for i in range(1,21) if (i%2 == 0)]
# print(even)
# l = list(range(1,20))
# odd = [i*2 if (i%2 == 0) else -i for i in l]
# print(odd)


# lis= {num:num**2 for num in range(1,11)}
# print(lis)

# name = "Naziya"
# rep = {i:name.count(i) for i in name}
# print(rep)


# odd_even = {i:'even' if i%2==0 else 'odd' for i in range(1,11)}
# print(odd_even)


                            # ARGS OPERATOR

# def total_num(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total


# f1 = tuple(map(int,input("\nEnter X Coloum (Space Seperated) : ").strip().split(" ")))
# print(type(f1))
# f2 = (f1)
# print(total_num(f1))


# def multiply_nums(*args):
#     multiply = 1
#     for i in args:
#         multiply *= i
#     return multiply


# inupt = list(map(int,input("\nEnter X Coloum (Space Seperated) : ").strip().split("*")))
# print(inupt)
# inupt1 = inupt
# print(multiply_nums(*inupt1))




# def power_list(num, *args):
#     if args:
#         return [i**num for i in args]
#     else:
#         return "You didn't pass any args"

# sub = [1,2,3]
# print(power_list(5,))
        


# def func_tion(l , **kwargs):
#     if kwargs.get("reverse_str") == True:
#         return [name[::-1].title() for name in l]

#     else:
#         return [name.title() for name in l]



# names = ['subhan' , 'ali' , 'naziya']
# print(func_tion(names))




# car = lambda a,b : a*b
# print(car(5,56))



# def func(a):
#     return True if a % 2 == 0 else False

# print(func(6))


# iseven = lambda a : a%2 == 0
# print(iseven(1))

# last = lambda s : s[-1]
# print(last('Subhan'))


# func = lambda s : len(s) > 5
# print(func('Subh'))



#                             ENUMERATE FUNCTION


# names = ['abc' , 'adcdef' , 'subhan']
# for pos, name in enumerate(names):
#     print(f"{pos} ------> {name}")


# def func(l,s):
#     for pos, name in enumerate(l):
#         if name == s:
#             return pos

#     else:
#         return -1

# print(func(names, "adcdef"))



# lis =  [1,2,3,4,5,6]

# def func(l):
#     var = [i**2 for i in l]
#     return var 

# pri = list(range(1,5))   
# print(func(pri))


# li = list(range(1,11))

# def squa(l):
#     return l**2

# ma = list(map(squa , li))
# print(ma)


# na = list(map(int,input("Enter Any Number : ").strip().split(" ")))
# print(na)


# lis = ['abadfad' , 'abfadfadfafdadffffffffacd' , 'abdedf']
# prin = list(map(len , lis))
# print(prin)




# def evens(a):
#     return a%2==0

# even = [2,5,8,5,6,5,7,9,1,3,4,5,8,6]

# var = list(filter(evens , even))   
# print(var)       



                # ZIP FUNCTION

# SU = ["FIRST NAME" , "LAST NAME" , "AGE"]
# SUB = ["SUBHAN" , "ALI" , "18"]

# print(list(zip(SU , SUB)))



# LIS = [(1,2), (3,4), (5,6)]

# l1 , l2 = list(zip(*LIS))
# print(list(l1))
# print(list(l2))


# f = [1, 8, 5, 9, 96, 5]
# s = [2, 4, 6, 58, 56, 1]

# h = []

# for i in zip(f,s):
#     h.append(max(i))

# print(h)






# def rank(l):
#     a = {}
#     ranks = 1
#     for i in sorted(l):
#         if i not in a:
#             a[i] = ranks
#             ranks += 1
#     return[a[i] for i in l]


# ls = rank([2, 4, 7, 5, 1])
# print(ls)



# n = 3
# for i in range(0,n):
#     for j in range (0,n-i-1):
#         print(end =' ')
#     for j in range(0,i +1):
#         print('* ' , end ="")
#     print()

# for i in range(n-1,0,-1):
#     for j in range(n,i,-1):
#         print(end =' ')
#     for j in range(0, i):
#         print("* " , end = "")
#     print()


# l , la, lb = [1,2,3] , [4,5,6] ,  [7,8,9]

# var = lambda *args : [sum(i)/len(i) for i in zip(*args)]

# print(var(l,la,lb))




# l = [1,3,5,7,9,11,17]
# var = lambda l : [(i%2 == 0) for i in l]
# print(any(var(l)))



# def check_error(*args):
#     if all([(type(i) == int or type(i) == float) for i in args]):
#         li = 0
#         for j in args:
#             li += j
#         return li
#     else:
#         print("wrong input")

# print(check_error(*l))


# names = ["subhan" , "subhan ali" , "naziya" , "parveen"]
# # h = []
# # for i in range(len(names)):
# #     d = len(names[i])
# #     h.append(d) 
# # print(max(h))

# h = lambda names : [len(names[i]) for i in range(len(names))]
# print(max(h(names)))


# def func(item):
#     return [len(item)]


# names = ["subhan" , "subhan ali" , "naziya" , "parveen" , "naz"]
# print(max(names , key = lambda list : [len(list)]))


# stud = [
#     dict(name =  'subhan' , score = 90 , age = 19),
#     dict(name = 'naziya' , score = 100 , age = 18),
#     dict(name = 'saz' , score = 80 , age = 25)
# ]

# stud = [
#     dict(name =  'subhan' , score = 90 , age = 19),
#     dict(name = 'naziya' , score = 100 , age = 18),
#     dict(name = 'saz' , score = 80 , age = 25)
# ]

# print(max(stud, key = lambda item : item.get('score'))['name'])



# model_guitars = [
#     {'model' : 'yamaha f310' , 'price' : 8400},
#     {'model' : 'faith naptune' , 'price' : 50000},
#     {'model' : 'faith apollo venus' , 'price' : 35000},
#     {'model' : 'taylor 814ce' , 'price' : 450000},
# ]

# both lines are same .get method or ['name'] method

# print(sorted(model_guitars , key = lambda dic : dic['price'] , reverse = True))
# print(sorted(model_guitars , key = lambda dic : dic.get('price') , reverse = True))



                    # RETURNING FUNCTION INSIDE FUNCTION

# def outer_func():
#     def inner_func():
#         print("inside innner function")
#     return inner_func()

# var = outer_func()


# def naziya(msg):
#     def parveen():
#         print(f"Message is {msg}")
#     return parveen

# varr = naziya("Naziya Parveen")
# varr()



# def power(x): # x=3
#     def num(n): # n=2
#         return n**x
#     return num

# var = power(5)
# print(var(5))



                        # DECORATOR FUNCTION 

# def decorator_func(any_function):
#     def wrap_function(*args, **kwargs):
#         print("This is decorator function")
#         return any_function(*args, **kwargs)
#     return wrap_function


# @decorator_func
# def func(a,b):
#     return (a + b)

# print(func(6,5))


# from functools import wraps

# def decorator_function_data(naziya):
#     @wraps(naziya)
#     def parveen(*args, **kwargs):
#         print(f"You are calling {naziya.__name__} fucntion")
#         print(naziya.__doc__)
#         return naziya(*args, **kwargs)
#     return parveen

# @decorator_function_data
# def substract(a,b):
#     '''This Function Takes Two Number as argument and substract it'''
#     return a - b


# print(substract(5,9))

# from functools import wraps
# import time

# def calculate_time(naziya):
#     @wraps(naziya)
#     def parveen(*args , **kwargs):
#         t1 = time.time()
#         returned_value = naziya(*args, **kwargs)
#         t2 = time.time()
#         print(f"Your function took {t2 - t1} second to run")
#         return returned_value
#     return parveen

# @calculate_time
# def substract(a,b):
#     # '''This Function Takes Two Number as argument and substract it'''
#     return a - b

# print(substract(5965,856))
        


                            # DECORATORS WITH ARGUMENTS

# from functools import wraps
# import time

# def only_datatype(naziya):
#     def decorators(parveen):
#         @wraps(parveen)
#         def wrappers(*args ,**kwargs):
#             if all([type(i) == naziya for i in args]):
#                 tim = time.time()
#                 var = parveen(*args ,**kwargs)
#                 tim2 = time.time()
#                 print(var)
#             print("invalid arguments")
#             print(f"Your function took {tim - tim2} seconds to run")
#         return wrappers
#     return decorators



# @only_datatype(str)
# def string_join_function(*args):
#     stri = ""
#     for i in args:
#         stri += i
#     return stri

# print(string_join_function("Naziya" , "Parveen"))




                                # GENERATOR SEQUENCE (FUNCTION)


# def naziya(n):
#     for i in range(1,n+1):
#         yield(i)

# for i in naziya(10):
#     print(i)

# numbers = naziya(10)
# print(numbers)



# def generator(n):
#     for i in range(1, n +1):
#         if i%2 == 0:
#             yield i

# for i in generator(7):
#     print(i)


# def generator(n):
#     for i in range(2, n +1 ,2):
#            yield i

# for i in generator(7):
#     print(i)


# WE USE PARANTHESIS() TO GENERATE GENERATORS

# square = (i**2 for i in range(1,11))
# print(square)

# for i in square:
#     print(i)

# import time
# t = time.time()
# square = (i**2 for i in range(1,1001))
# print(square)
# for i in square:
#     print(i)
# print(time.time() - t)







                        # OBJECT ORIENTED PROGRAMMING (OOP) IN PYTHON



                        

# class Person:
#     def __init__(self , first_name, last_name, age):
#         print("This will print when constructor // init method called")
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
        
# p1 = Person("naziya" , "parveen" , 18)
# p2 = Person("subhan" , "ali" , 19)

# print(p1.first_name)



# class laptop:
#     def __init__(self , brand_name , model_name , price):
#         self.name = brand_name
#         self.modelname = model_name
#         self.price = price

# l1 = laptop("dell" , "pavillion" , 250000)
# print(l1.name)



# class Person:
#     def __init__(self , first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     def is_above_18(self):
#         return self.age>16
        
# p1 = Person("naziya" , "parveen" , 18)
# p2 = Person("subhan" , "ali" , 19)
# print(p1.is_above_18())

# print(p1.full_name())
# print(Person.full_name(p1))




# class Laptop:
#     discount_percent = 10
#     def __init__(self ,name , model_name , price):
#         self.percent = name
#         self.mode_name = model_name
#         self.price = price

#     def apply_discount(self):
#         retu = self.price/100 * self.discount_percent
#         return self.price - retu
        
# p1 = Laptop("dell", "pavillion" , 65600)
# p2 = Laptop("apple" , "Macbook" , 250000)
# p2.discount_percent = 50

# print(p2.apply_discount())




# class Circle:
#     pi = 3.14
#     def __init__(self , radius):
#         self.radius = radius

#     def circle_area(self):
#         return 2*Circle.pi*self.radius

# c = Circle(10)
# print(c.circle_area())
        


# class Person:
#     sel = 0
#     def __init__(self , first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         Person.sel += 1
        
# p1 = Person("naziya" , "parveen" , 18)
# p2 = Person("subhan" , "ali" , 19)

# print(Person.sel)





# class Person:
#     sel = 0
#     def __init__(self , first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         Person.sel += 1
    
#     @classmethod
#     def from_str(cls, string):
#         first,last,age =  string.split(",")
#         return cls(first,last,age)

#     @staticmethod
#     def naziya():
#         print("Static Method Is Called")

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
        
# p1 = Person("naziya" , "parveen" , 18)
# p2 = Person("subhan" , "ali" , 19)
# p3 = Person.from_str("subhan,ali,19")

# print(Person.sel)
# print(p3.full_name())
# print(Person.naziya())






    # ENCAPSULATION , ABSTRACTION , SOME SPECIAL NAMING CONVENTION AND NAME MANGLING


# ENCAPSULATION = Making a class of DATA and collecting it in a sequence way is called
                    # encapsulation. Like below there is class of data (phone_company etc)
                    # and we arranged it in sequence manner


# class Phone:
#     def __init__(self , phone_company, phone_model, price):
#         self.company = phone_company
#         self.phone_model = phone_model
#         self.price = price

#     def calling(self , phone_number):
#         return f"Calling {phone_number}......"

#     def full_name(self):
#         return f"{self.company} {self.phone_model}"



# ABSTRACTION = Hiding complexities from the user is called Abstraction , like in python
              # there is sort method which we use but behind that there is very complex algorithm
              # but we only know sort method that is called abstraction



# SPECIAL NAMING CONVENTION = Convention is that which we use to show other developer to not
                            # touch that part where we use convention. afcourse he can make 
                            # changes in any part but it just a way to show that it a private 
                            # property where we use convention 

# EX - _name is a private property because we use underscore and we are saying to other
       # developer to not touch that part where we use convention(_) 
#__name__ we called this dunder method or magic method where we use double underscore




# NAME MANGLING = __name (this is not a convention) it is something which we can use when
                # we want to make python to change class 

# EX - if we use (objectname.__name) in any class , and print this then this will not print
        # because python will automatically change from (object.__name) to 
        # (objectname._classname__name) python will automatically add (_classname) in 
        # this and now we have to write (objectname._classname__name) to print





# PROPERTY AND SETTER DECORATOR

# class Phone:
#     def __init__(self , phone_company, phone_model, price):
#         self.company = phone_company
#         self.phone_model = phone_model
#         self.price = max(price,0)
#         # we can also use if , else function instead of max 

#     def calling(self , phone_number):
#         return f"Calling {phone_number}......"

#     @property
#     def pprice(self):
#         return self.price

#     @pprice.setter
#     def pprice(self, new_price):
#         self.price = max(new_price,0)


#     @property #we use property function to not call function as a function
#     # now we can call function without paranthesis
#     def complete_specification(self):
#         return f"{self.company} {self.phone_model} and price is {self.price}"


#     def full_name(self):
#         return f"{self.company} {self.phone_model}"

# phone1 = Phone("Apple" , "iphone 13 pro max" , 165000)
# # print(phone1.full_name())
# # print(phone1.price)
# phone1.pprice = - 500
# print(phone1.price)
# print(phone1.complete_specification)





# INHERITANCE


# class Phone: #base class / parent class
#     def __init__(self , phone_company, phone_model, price):
#         self.company = phone_company
#         self.phone_model = phone_model
#         self.price = max(price , 0)

#     def calling(self , phone_number):
#         return f"Calling {phone_number}......"

#     def full_name(self):
#         return f"{self.company} {self.phone_model}"


# class Smartphone(Phone): # derived class / child class

#     def __init__(self , phone_company, phone_model, price , ram , rom , rear_camera):
#         # Phone.__init__(self,phone_company, phone_model , price) #this is uncommon way
#         super().__init__(phone_company, phone_model , price) #this is common way
#         self.ram = ram
#         self.rom = rom
#         self.rear_camera = rear_camera

#         # we also imported function of phone class when we inherit phone class

# class Flagship(Smartphone):
#     def __init__(self, phone_company, phone_model, price, ram, rom, rear_camera, front_camera):
#         super().__init__(phone_company, phone_model, price, ram, rom, rear_camera)
#         self.front_camera = front_camera

#     def full_specs(self):
#         return f"{self.phone_model} {self.price} {self.ram} {self.rom} {self.rear_camera} {self.front_camera}"

# phone = Phone("nokia" , "3300" , 1500)
# smartphone = Smartphone("oneplus" , "6 pro" , 25000 , "8gb" , "128gb" , "24mp")
# flagship = Flagship("Apple" , "iphone 13 pro max" , 25000 , "4gb" , "64gb" , "12mp" , "16mp")

# print(f"{smartphone.full_name()} and {smartphone.ram}")
# print(f"{phone.full_name()} and price is {phone.price}")
# print(f"{flagship.full_specs()}")





#RAISE ERROR

# def add(a,b):
#     if type(a) is int and type(b) is int:
#         return a + b
#     raise TypeError("OOPs you are passing wrong data type")
#     # to raise error type raise (error type) 

# print(add(4 , 6))



# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def sound(self):
#         raise NotImplementedError("You have to define sound method for every class")


# class Dog(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def sound(self):
#         return "Bau Bau"

# class Cat(Animal):
#     def __init__(self,name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def sound(self):
#         return "Meow Meow"


# pd = Dog("German" , "shepherd")
# print(pd.sound())




# EXCEPTION HANDLING

# while True:
#     try:
#         age = int(input("Enter Your Age : "))
#         break
#     except:
#         print("invalid error......")

# if age >= 18:
#     print("you can play this game")
# else:
#     print("you can't play this game")



# def divide(a,b):
    
#     try:
#         return a/b
#     except ZeroDivisionError as err:
#         print(err)
#     except TypeError:
#         print("You can only enter integers")
#     except:
#         print("unexpected error")


# print(divide(10,"2"))




# DEBUGGING OF PYTHON DEBUGGER

# import pdb
# pdb.set_trace()
# class NameTooShortError(TypeError):
#     pass

# def validate(name):
#     if len(name) < 8:
#         raise NameTooShortError("Name is too short")
#     else:
#         return name

# username = validate(input("Enter Your name : "))
# print(f"Hello {username}")






                                # READ TEXT FILE WITH PYTHON 


# f = open( r"D:\Documents\Subhan\hii.txt")
# print(f'{f.tell()}') #this will show start position of cursor

# print(f.read())

# print(f"{f.tell()}") #this will show end position of cursor

# print(f"{f.seek(0)}") #this will change position of cursor like 0 or 8
# print(f.readlines()) #you can use end = "" to not show space between lines


# for i in f.readlines():
#     print(i , end = "")

# print(f.name)

# f.close()
# print(f.closed)


# with open("D:\Documents\Subhan\hii.txt") as f:
#     data = f.read()
#     print(data)


# for i in f.readlines()[:5]:
#     print(i , end = "")




# with open("file2.txt" , "a") as f:  # use "w" when to overwrite data and use "a" when to append data
#     f.write("\nhow are you?")
#     # f.write("\ni hope you are doing good")




# with open(r"C:\Users\Subhan\Documents\Python\text1.txt" , "r") as rf:
#     with open(r"C:\Users\Subhan\Documents\Python\text2.txt" , "w") as wf:
#         wf.write(rf.read())




# with open(r"C:\Users\Subhan\Documents\Python\Index.html" , "r") as webpage:
#     with open(r"C:\Users\Subhan\Documents\Python\text2.txt" , "a") as wf:
#         for line in webpage.readlines():
#             if "<a href=" in line:
#                 pos = line.find('<a href=')
#                 first = line.find('\"', pos)
#                 second = line.find('\"', first+1)
#                 url = line[first + 1 : second]
#                 wf.write(url + "\n")


# with open(r"C:\Users\Subhan\Documents\Python\Index.html" , "r") as webpage:
#     with open(r"C:\Users\Subhan\Documents\Python\text2.txt" , "a") as wf:
#         page = webpage.read()
#         link_exist = True
#         while link_exist:
#             pos = page.find("<a href=")
#             if pos == -1:
#                 link_exist = False
#             else:
#                 first = page.find('\"', pos)
#                 second = page.find('\"', first+1)
#                 url = page[first + 1 : second]
#                 wf.write(url + "\n")
#                 page = page[second :]


# TO READ FILE WITH EMOJI WE CAN USE encoding = "utf-e" THIS ENCODING METHOD CAN ENCODE EMOJIS ALSO
# BY DEFAULT ENCODING METHOD IS CP1252 WHICH IS WINDOWS DEFAULT ENCODING METHOD WHICH CAN'T DECODE EMOJIS




                        # READ AND WRITE CSV FILE IN PYTHON



# from csv import DictReader

# with open(r"C:\Users\Subhan\Documents\Python\Comman Seperated.csv" , "r") as rf:
#     csv_reader = DictReader(rf, delimiter = "|") #if delimiter or seperated values are seperated with another thing like pipe
#                                                 # then you have to use (delimiter = "|") in dictreader function to use csv file
#     for naziya in csv_reader:
#         print(naziya)
#         print(naziya["mobileno."])



# from csv import writer as parveen

# with open("file3.csv" , 'w' , newline = "") as rf:
#     naziya = parveen(rf)
#     # method are writerow , writerows
#     # naziya.writerow(["name" , "country"])
#     # naziya.writerow(["subhan" , "India"])
#     # naziya.writerow(["naziya" , "India"])
#     naziya.writerows([["name" , "country"] , ["subhan" , "India"] , ["naziya" , "India"]])


# from csv import DictWriter as parveen

# with open(r"C:\Users\Subhan\Documents\Python\file3.csv" , "w" , newline= "") as naz:
#     naziya = parveen(naz, fieldnames=["first_name", "last_name" , "age"])
#     naziya.writeheader()
#     # naziya.writerow({
#     #     "first_name" : "subhan ali",
#     #     "last_name" : "Zaidi",
#     #     "age" : 19
#     # })

#     # naziya.writerow({
#     #     "first_name" : "naziya",
#     #     "last_name" : "parveen",
#     #     "age" : 18
#     # })

#     naziya.writerows([

#         {"first_name" : "subhan ali",
#         "last_name" : "Zaidi",
#         "age" : 19},

#         {"first_name" : "naziya",
#         "last_name" : "parveen",
#         "age" : 18}
#     ])




# from csv import DictWriter , DictReader

# with open(r"C:\Users\Subhan\Documents\Python\file3.csv"  , "r") as rf:
#     with open(r"C:\Users\Subhan\Documents\Python\CommanSeperated1.csv" , "w" , newline= '') as wf:
#         naziya = DictReader(rf)
#         parveen = DictWriter(wf, fieldnames=["firstname","lastname","age"])
#         parveen.writeheader()
#         for row in naziya:
#             fname , lname, age = row["first_name"] , row["last_name"] , row["age"]
#             parveen.writerow({
#                 "firstname" : fname.upper(),
#                 "lastname" : lname.upper(), 
#                 "age" : age ,
#             })






                                    # OS MODULE IN PYTHON



# import os

# print(os.getcwd())
# # os.mkdir("movies") #to make folder in current working directory or cwd
# # print(os.path.exists("movies"))  #to check folder exists or not in cwd

# if os.path.exists("movies"):
#     print("already exists")
# else:
#     os.mkdir("movies")

# open("file7.csv" , "a").close() #to create file in current working directory or cwd

# os.mkdir(r"D:\subhan") #to make folder in different drive or directory

# os.chdir(r"C:\users") #to change current working directory or cwd
# print(os.getcwd())

# print(os.listdir()) #to check list of all files and folders in directory
# print(os.listdir(r"D:")) # to get list of particulare directory


# for item in os.listdir():
#     path = os.path.join(os.getcwd(),item)
#     print(path)
    

# for item in os.listdir(os.chdir(r"D:")):
#     path = os.path.join(os.getcwd(),item)
#     print(path)
    



# import os

# # # os.chdir(r"D:\movies")
# # path = os.walk(r"D:\documents")  #to walk in or go deep in folders and check all files and folders
# # for i, j , k in path:
# #     print(f"current_path = {i}")
# #     print(f"folder_names = {j}")
# #     print(f"file_names = {k}")

# print(os.getcwd())
# os.makedirs("naziya\parveen") #to make folders inside folders



# SHUTIL MODULE

# import shutil
# # shutil.rmtree("naziya")  #this will delete whole folder either file is there or not but this will not
# #                         # send deleted folder or file to recycle bin this will permanently delete file


# shutil.copytree("naziya" , "new folder/naziya_parveen")  #to copy a folder or file from one
#                                                     # directory/folder to another directory/folder

# shutil.move("file or folder name" , "directory where you want to move/file or folder name")





# import os

# from PIL import Image
# from PIL import ImageEnhance as Naziya

# os.chdir(r"C:\users\subhan\documents\python")
# print(os.getcwd())

# img = Image.open("Utopia Planet 16-Bit.png")
# img.save("Utopia Planet 16-Bit.pdf")
# img.show("gar")

# size = (250,250)  # to resize image
# img.thumbnail(size)
# img.save("Utopia Planet 16-Bitsmall.png")


# for item in os.listdir():
#     if item.endswith(".png"):
#         im = Image.open(item)
#         filename , extension = os.path.splitext(item)
#         im.save(f"{filename}.jpeg")







                                # WORKING WITH SHARPNESS, COLOR , CONTRAST

                            
# import os
# from PIL import Image
# from PIL import ImageEnhance as Naziya
# from PIL import ImageFilter as parveen

# os.chdir(r"C:\users\subhan\documents\python")   #to change directory to image location

# # SHARPNESS

# img = Image.open("Utopia Planet 16-Bit.png")

# enhancer = Naziya.Sharpness(img)
# enhancer.enhance(3).save("Utopia Planet 16-Bit(shaped).jpg")

# # 0 ==> to get blurry image
# # 1 ==> to get original image
# # 2 ==> to get image with increased sharpness by 2
# # 3......  ==> and so on




# # COLOR

# img = Image.open("Utopia Planet 16-Bit.png")

# enhancer = Naziya.Color(img)
# enhancer.enhance(1.5).save("Utopia Planet 16-Bit(colored).jpg")

# # 0 ==> to get Desaturated image
# # 1 ==> to get original image
# # 2 ==> to get image with increased saturation by 2
# # 3......  ==> and so on




# # Brightness

# img = Image.open("Utopia Planet 16-Bit.png")

# enhancer = Naziya.Brightness(img)
# enhancer.enhance(5).save("Utopia Planet 16-Bit(brightnessss).jpg")

# # 0 ==> to get Dark image
# # 1 ==> to get original image
# # 2 ==> to get image with increased Brightness by 2
# # 3......  ==> and so on




# # Contrast

# img = Image.open("Utopia Planet 16-Bit.png")

# enhancer = Naziya.Contrast(img)
# enhancer.enhance(1.1).save("Utopia Planet 16-Bit(contrast).jpg")

# # 0 ==> to get Grey/Decontrast image
# # 1 ==> to get original image
# # 2 ==> to get image with increased contrast by 2
# # 3......  ==> and so on




# # Image Blur

# img = Image.open("Utopia Planet 16-Bit.png")
# img.filter(parveen.GaussianBlur(50)).save("Utopia Planet 16-Bit(blurred).png")

# # 0 ==> to get original image
# # 2 ==> is default value if you didn't put any value it will automatically blurred by 2
# # 3 ==> to increase blur
# # 4 ==> to increase blur by 4 and so on



# open("FirstGuiApplication.py" , 'a').close()









                            # USE FOR LOOP WITH TKINTER TO CREATE LABLE AND ENTRYBOX


# import tkinter
# from tkinter import ttk

# naziya = tkinter.Tk()
# naziya.title("Naziya Parveen")

# labels = ["name" , "age" , "country" , "state" , "city" , "pincode"]

# for i in range(len(labels)):
#     current_label = 'label' + str(i)
#     current_label = ttk.Label(naziya , text= labels[i])
#     current_label.grid(row= i, column= 0 , sticky=tkinter.W , padx = 2 , pady = 2)


# entryvar = tkinter.StringVar()
# entry_dic = {
#     "name" : tkinter.StringVar() ,
#     "age" : tkinter.StringVar() ,
#     "country" : tkinter.StringVar() ,
#     "state" : tkinter.StringVar() ,
#     "city" : tkinter.StringVar() ,
#     "pincode" : tkinter.StringVar() ,
# }

# counter = 0
# for i in entry_dic:
#     entrybox_name = "entry" + i
#     entrybox_name = ttk.Entry(naziya , width= 15 ,textvariable= entry_dic[i])
#     entrybox_name.grid(row=counter ,column=1 , padx = 2 , pady = 2)
#     counter += 1 

# def naz():
#     print(entry_dic["name"].get())
#     print(entry_dic["age"].get())
#     print(entry_dic["country"].get())
#     print(entry_dic["state"].get())
#     print(entry_dic["city"].get())
#     print(entry_dic["pincode"].get())


# submit_btn = ttk.Button(naziya , text = "Submit" , command = naz)
# submit_btn.grid(row=6 ,columnspan=2)


# naziya.mainloop()










                            # LABLE FRAME WIDGET



# import tkinter
# from tkinter import ttk

# naziya = tkinter.Tk()
# naziya.title("Naziya Parveen")


# Label_frame = tkinter.LabelFrame(naziya, text = "Enter Your details below : ")
# Label_frame.grid(row=0 , column=0 , padx=40 ,pady=10)
# Label_frame.configure(foreground="Red")


# labels = ["What's Your Name :", "What's Your Country :" , "What's Your State :" ,
#          "What's Your City :" , "What's Your Area Pincode :"  , "What's Your Age :" ]

# age1 = tkinter.StringVar()
# Combo_box = ttk.Combobox(Label_frame , values = [i for i in range(18,51)] , textvariable=age1)
# Combo_box.grid(row= 5 ,column=1)
# Combo_box.current(0)

# for i in range(len(labels)):
#     current_label = 'label' + str(i)
#     current_label = ttk.Label(Label_frame , text= labels[i])
#     current_label.grid(row= i, column= 0 , sticky=tkinter.W , padx = 8 , pady = 10)


# entryvar = tkinter.StringVar()
# entry_dic = {
#     "name" : tkinter.StringVar() ,
#     "country" : tkinter.StringVar() ,
#     "state" : tkinter.StringVar() ,
#     "city" : tkinter.StringVar() ,
#     "pincode" : tkinter.StringVar() ,
# }

# counter = 0
# for i in entry_dic:
#     entrybox_name = "entry" + i
#     entrybox_name = ttk.Entry(Label_frame , width= 15 ,textvariable= entry_dic[i])
#     entrybox_name.grid(row=counter ,column=1 , padx = 10 , pady = 6)
#     counter += 1 

# def naz():
#     print(entry_dic["name"].get())
#     print(age1.get())
#     print(entry_dic["country"].get())
#     print(entry_dic["state"].get())
#     print(entry_dic["city"].get())
#     print(entry_dic["pincode"].get())


# submit_btn = ttk.Button(naziya , text = "Submit" , command = naz)
# submit_btn.grid(row=7 ,columnspan=2 , pady = 30)


# # entry_box = ttk.Entry(Label_frame,width = 15)
# # entry_box.grid(row = 0 , column=0)


# # labe = ttk.Label(naziya , text = "Submit")
# # labe.grid(row = 1 , column = 0)
# # labe.configure(background="Red")


# naziya.mainloop()






                            # MAKE TAB WITH TKINTER IN PYTHON



# import tkinter as tk
# from tkinter import ttk


# naziya = tk.Tk()
# naziya.title("Naziya Parveen")

# parveen = ttk.Notebook(naziya)
# page1 = ttk.Frame(parveen)
# page2 = ttk.Frame(parveen)

# parveen.add(page1 , text = "ONE")
# parveen.add(page2 , text = "TWO")
# # parveen.grid(row=0,column=0)
# parveen.pack(expand=True , fill = "both")

# labe = ttk.Label(page1 , text = "This is Page one")
# labe.grid(row=0, column=0)

# box = ttk.Entry(page1, width = 15)
# box.grid(row=0,column=1)


# naziya.mainloop()








                    # MAKE MENU BAR LIKE (FILE,EDIT,SELECTION) AND OTHER WITH PYTHON




# import tkinter as tk
# from tkinter import ttk
# from turtle import width

# naziya = tk.Tk()
# naziya.title("Naziya Parveen")


# ***************** SIMPLE MENU BAR *******************

# menubar = tk.Menu(naziya)
# menubar.add_command(label= "File")
# menubar.add_command(label= "Edit")
# menubar.add_command(label= "Type")
# menubar.add_command(label= "Tools")
# menubar.add_command(label= "View")
# menubar.add_command(label= "Window")



# menu_bar = tk.Menu(naziya)

# # file menu bar
# file_menu = tk.Menu(menu_bar , tearoff=0)
# file_menu.add_command(label= "Open New")  #we can use command here to make it functional by defining function
# file_menu.add_separator()
# file_menu.add_command(label= "Save")
# file_menu.add_command(label= "Save As")
# file_menu.add_separator()
# file_menu.add_command(label= "Close")
# menu_bar.add_cascade(label = "File" , menu = file_menu)


# # edit menu bar
# edit_menu = tk.Menu(menu_bar , tearoff=0)
# edit_menu.add_command(label= "Undo")
# edit_menu.add_command(label= "Redo")
# edit_menu.add_separator()
# edit_menu.add_command(label= "Cut")
# edit_menu.add_command(label= "Copy")
# menu_bar.add_cascade(label= "Paste" , menu = edit_menu)


# naziya.config(menu=menu_bar)

# naziya.mainloop()







#                               MESSAGE BOX AND EXCEPTION HANDLING


# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox as naz

# naziya = tk.Tk()
# naziya.title("Naziya Parveen")

# frame_label = tk.LabelFrame(naziya , text ="Contact Details")
# frame_label.grid(row=0 ,column= 0 , padx= 20 , pady= 10)
# frame_label.configure(foreground = "blue")


# # name label

# name_label = ttk.Label(frame_label , text ="Enter Your Name Please" , font= ("Arial black", 9 , "bold"))
# name_label.grid(row=0, column=0, padx= 5 , pady= 5 , sticky=tk.N)

# var_name = tk.StringVar()
# name_box = ttk.Entry(frame_label , width= 35 , textvariable= var_name)
# name_box.grid(row=1 ,column=0, padx= 10 , pady= 5)


# # age label

# age_label = ttk.Label(frame_label , text ="Enter Your Age Please" , font= ("Arial black", 9 , "bold"))
# age_label.grid(row=0, column=1, padx= 5 , pady= 5 , sticky=tk.N)

# var_age = tk.StringVar()
# age_box = ttk.Entry(frame_label , width= 35, textvariable= var_age)
# age_box.grid(row=1 ,column=1, padx= 10 , pady= 5)

# def Naziya():
#     names = var_name.get()
#     ages = var_age.get()
#     if len(names) == 0 or len(ages) == 0:
#         naz.showerror("Empty Box", "You have not filled your details")

#     else:
#         try:
#             age = int(ages)
            
#         except ValueError:
#             naz.showerror("Error" , "Enter Your age in numbers")

#         else:
#             if age < 18:
#                 naz.showwarning("Warning" ,"Your are not above 18")
#             else:  
#                 print(f"{names},{age}")
#                 naz.showinfo("Submitted" , "You have successfully submitted Your details")

            
        
# submit = ttk.Button(naziya , text="Submit" , command= Naziya )
# submit.grid(row= 1 , columnspan = 2)

# naziya.mainloop()






# from shutil import move
# from turtle import *

# naz = Turtle()
# naz.shape("classic")
# # naz.color("yellow", "white")
# nazi = Screen()
# nazi.title("my first game")
# nazi.bgcolor("white")

# naz.speed(0)
# # naz.hideturtle()

# # naz.forward(200)
# # naz.left(90)
# # naz.forward(200)
# # naz.left(90)
# # naz.forward(200)
# # naz.left(90)
# # naz.forward(200)
# # naz.penup()
# # naz.right(90)
# # naz.forward(100)
# # naz.pendown()

# # naz.circle(50,80)
# # naz.circle(-80,270)
# # naz.circle(-60,170)
# naz.right(45)
# for i in range(2):
    
#     naz.circle(15,90)
#     naz.circle(32,90)
# naz.circle(15,45)

# naz.color("black", "black")
# naz.begin_fill()
# naz.circle(8,720)
# naz.end_fill()


# naz.circle(15,45)
# naz.penup()
# naz.right(45)
# naz.forward(40)

# naz.right(10)
# naz.pendown()
# naz.right(125)
# for i in range(2):
    
#     naz.circle(-15,90)
#     naz.circle(-32,90)
# naz.circle(-15,45)
# naz.color("black", "black")
# naz.begin_fill()
# naz.circle(-8,720)
# naz.end_fill()



# done()











# from sketchpy import library as lib

# obj = lib.rdj()

# obj.draw()

# import turtle

# canvas1 = [[(-40, 120), (-70, 260), (-130, 230), (-170, 200), (-170, 100), (-160, 40), (-170, 10), (-150, -10), (-140, 10),
#            (-40, -20), (0, -20)],
#           [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10), (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),
#            (40, 120), (0, 120)]]
# canvas2 = [[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0), (-186, -30), (-186, -40), (-120, -170), (-110, -210),
#            (-80, -230), (-64, -210), (0, -210)],
#           [(0, -210), (64, -210), (80, -230), (110, -210), (120, -170), (186, -40), (186, -30), (176, 0), (130, -40),
#            (100, -46), (50, -40), (40, -30), (0, -30)]]
# canvas3 = [[(-60, -220), (-80, -240), (-110, -220), (-120, -250), (-90, -280), (-60, -260), (-30, -260), (-20, -250),
#            (0, -250)],
#           [(0, -250), (20, -250), (30, -260), (60, -260), (90, -280), (120, -250), (110, -220), (80, -240), (60, -220),
#            (0, -220)]]

# turtle.hideturtle()
# turtle.bgcolor('#ba161e')  # Dark Red
# turtle.setup(500, 600)
# turtle.title("I AM IRONMAN")
# canvas1Goto = (0, 120)
# canvas2Goto = (0, -30)
# canvas3Goto = (0, -220)
# turtle.speed(2)


# def logo(a, b):
#     turtle.penup()
#     turtle.goto(b)
#     turtle.pendown()
#     turtle.color('#fab104')  # Light Yellow
#     turtle.begin_fill()

#     for i in range(len(a[0])):
#         x, y = a[0][i]
#         turtle.goto(x, y)

#     for i in range(len(a[1])):
#         x, y = a[1][i]
#         turtle.goto(x, y)
#     turtle.end_fill()


# logo(canvas1, canvas1Goto)
# logo(canvas2, canvas2Goto)
# logo(canvas3, canvas3Goto)
# turtle.hideturtle()
# turtle.done()



# var = "2"
# var1 = 1
# var2 = 2
# var3 = "3"
# print(var+var3)



# naz = {
#     'root' : '',
# }

# x = 1,3,5,6,8,9,6
# y = [1,3,5,6,8,9,6]
# z = y[::-1]
# print(z)

# res = {}
# for key in x:
# 	for value in z:
# 		res[key] = value
# 		z.remove(value)
# 		break

# print ("Resultant dictionary is : " + str(res))




# firstlist = [52,56,98,52,63,52,54,58,98,56]

# x = []
# for NAZIYA in range(101):
#     x.append(NAZIYA)


# res = {}
# for key in x:
#     for value in firstlist:
#         res[key] = value
#         firstlist.remove(value)
#         break

# print ("Resultant dictionary is : " + str(res))




# Real World Program Challenge

# firstlist = "0-10 ,10-20, 20-30, 30-40, 40-50, 50-60, 60-70, 70-80, 80-90, 90-100"


# li = (firstlist).strip().split(",")
# print(f"{li}")
# print(type(li))

# deviation = []
# for i in li:
#     z = (i).strip().split("-")
#     deviation.append(z)
#     print(i)
# print(f"{deviation}")


# lis = []
# naz = 0
# for i in deviation:
#     g = i
#     naz+=1
#     for i in g:
#         we = int(i)
#         lis.append(we)
# print(f"{lis}")

# y = 0
# x = 1
# for i in range(len(lis)//2):
#     xy = lis[y]+lis[x]
#     x+=2
#     y+=2
#     print(f"{xy}")





# # initializing list
# test_list = [1, 4, 5, 6, 3, 5]

# # printing original list
# print("The original list is : " + str(test_list))

# li = last_elem = test_list[-1:][0]

# z = 0
# for i in test_list:
#     z+=1
#     if z == len(test_list):
#         print('final')
#     else:
#         print('going')


# # using slicing to print last element
# # print("The last element using slicing is : ", li)

# x = round(2.5)
# y = round(3.5)
# print(x)
# print(y)

# def solve(nums):
#    if nums[1] <= nums[0]:
#       return False
#    for i in range(len(nums)):
#       if i - 1 >= 0:
#          if nums[i] == nums[i - 1]:
#             return False

#    return True

# nums = [2, 4, 8, 7, 5, 1, 5, 7, 2, 1]
# print(solve(nums))






# def maxnum(lis):
#     s1 = 0
#     s= max(lis)
#     for i in lis:
#         if i == s:
#             s1+=1

#     if s1 <= 1:
#         print('there is no repeating max number')
#     else:
#         print(f'there is {s1} repeating number')



# listy = [1,2,3,8,2,6,8,4,2,3]
# # print(maxnum(listy))


# def solve(nums):
#     if nums[1] <= nums[0]:
#         return False
#     for i in range(len(nums)):
#         if i - 1 >= 0:
#             if nums[i] == nums[i - 1]:
#                 return False

#     return True

# print(solve(listy))



# odd = []
# for i in range(1,20):
#     if i % 2:
#         odd.append(i)
# print(odd)







# VIEWS .PY 1354 LINE BACKUP CONTINUOUS SERIES ODD EVEN

# tr = solve(secondlist)
            # print(tr)

            # if tr == True:

                # Naziya['false'] = tr
                # grou = []
                # if len(secondlist)%2:
                #     for i in range(len(secondlist)//2 + 1):
                #         z = secondlist[i]
                #         grou.append(z)

                # Naziya['grou'] = grou
                # Naziya['lengrou'] = len(grou)

                # naziya = []
                # if len(secondlist)%2:
                #     for i in range(len(secondlist)//3 + 1):
                #         z = secondlist[i]
                #         naziya.append(z)
                # else:
                #     print('this is nothing')

                # # naziya.pop(-1)
                # Naziya['naziya'] = naziya
                # Naziya['lennaz'] = len(naziya)

                
                # naziya1 = []
                # if len(secondlist)%2:
                #     for i in range(len(secondlist)//3 +1):
                #         z = secondlist[i]
                #         naziya1.append(z)
                # else:
                #     print('this is nothing')

                # Naziya['naziya1'] = naziya1


                # naziya2 = []
                # if len(secondlist)%2:
                #     for i in range(len(secondlist)//3 + 1):
                #         z = secondlist[i]
                #         naziya2.append(z)
                # else:
                #     print('this is nothing')

                # print(f"this is len{len(naziya2)}")

                # Naziya['naziya2'] = naziya2


# from filecmp import cmp

# def alternating(l):
#     return all(cmp(a, b)*cmp(b, c) == -1 for a, b, c in zip(l, l[1:], l[2:]))

# listy = [1,2,3,8,2,6,4,2,3,7]

# va = 1

# for i in range(0,li):
#     if listy[i] <= listy[va]:
#         va+=1

#     else:
#         print('this list is alternating')
#         break


# def repeating(lis):

#     li = lis.index(max(lis))+1

#     for i in range(li,len(lis) ):
#         if lis[i] == max(lis):
#             return True        
#         else:
#             continue



# p = repeating(listy)

# if p == True:
#     print('used grouping method')
# else:
#     print('used simple method')




# listy1 = [1,2,3,8,2,6,4,4,8,2,3,7,8]
# listy12 = [1,2,3,8,4,3,7,1,5,1,5]
# listy13 = [1,2,3,8,4,3,1]



# def alternating(listy1):
#     l = 0
#     lk = 1
#     li = listy1.index(max(listy1))+1
#     col = []

#     for i in range(len(listy1)):
#         if listy1[l] <= listy1[lk]:
#             l += 1
#             lk += 1
#             print(i)
#             True
#             continue
#         else:
#             for i in range(li,len(listy1)):
#                 if listy1[i] <= listy1[i+1]:
#                     # print('this is alternating series')
#                     break
#                     # col.append(listy1[i])
#                 else:
#                     if listy1[i] >= listy1[i+1]:
#                         # print('this is alternating series')
#                         break
#                     else:
#                         # print('this series is not alternating')
#                         break


# print(alternating(listy1))
# print(alternating(listy12))
# print(alternating(listy13))




# def maxnum(lis):
#     s1 = 0
#     s= max(lis)
#     for i in lis:
#         if i == s:
#             s1+=1

#     if s1 <= 1:
#         return False
#     else:
#         return True

# listy12 = [1,2,3,8,2,6,4,4,2,3,7]
# print(maxnum(listy12))



# even = []
# for i in range(1,11):
#     if i % 2 == 0:
#         even.append(i)
# print(even)

# odd = []
# for i in range(0,11):
#     if i % 2 != 0:
#         odd.append(i)
# print(odd)


# even.extend(odd)
# print(even)

# prime1 = []
# for j in range(10,18+1):
#     if j > 1:
#         for i in range(2,j):
#             if (j%i)==0:
#                 break
#             # else:
#             #     print(j)


# prime = []
# for i in range(10, 18):
#     for j in  range(2,i):
#         if i%j == 0:
#             prime.append(i)
#             break
#         else:
#             # prime.append(i)
#             for i in prime:
#                 if i%2==0:
#                     # prime.remove(i)
#                     print(i)

# print(set(prime))






















# liss = [1,2,3,8,3,2,1]

# def rept(listy):
#     va = 0
#     va1 = 1
#     for i in range(max(listy)):
#         if listy[i] > listy[i+1]:
#             return False
#         else:
#             if listy[i] < listy[i+1]:
#                 va += 1
#                 va1 += 1
#                 continue
#             if listy[va] > listy[va1]:
#                 return False
#             else:
#                 if listy[va] < max(listy):
#                     va += 1
#                     va1 += 1
#                     continue
#                 else:
#                     return True  


# print(rept(liss))









# for i in l:
#     print(i)
#     print(type(i))


# aa = 8.058
# q = str(aa)
# z = (q).strip().split(".")

# first = int(z[0])
# a = float('.'+z[1])

# print(first)
# print(a)


# l = [59,89,56,41,74,52,45,85,74,-12,16,23,59]

# def remove_list_item(list,naz):
#     for j in naz:
#         list.remove(j)

#     return list

# n = [23,59,-12]
# z = remove_list_item(l,n)
# print(z)













# l = ['-', '1', 'Naziya', 'Naziya', '-','Naziya','-']

# def indexingfunction(l,Naziya):
#     indexlist = []
#     for i in range(len(l)):
#         if l[i] == Naziya:
#             indexlist.append(i)

#     return indexlist
            

# print(indexingfunction(l,"Naziya"))







# i = 1
# while i < 2:
#     print('TU MJ')





# l = [2,3,8,9,6,4,2,3,8,7,9]


# def maxnum(lis):
#     s1 = 0
#     s= max(lis)
#     for i in lis:
#         if i == s:
#             s1+=1

#     if s1 <= 1:
#         return False
#     else:
#         return True


# print(indexingfunction(l,max(l)))











# listy1 = [1,2,3,2,6,8,4,4,2,3,7]
# # listy12 = [1,2,3,8,4,3,7,1,5,1,5]
# # listy13 = [1,2,3,8,4,3,1]

# # z = listy1.index(max(listy1))
# # for i in range(z+1):
# #     print(listy1[i])

# def solve(nums):
#     if nums[1] <= nums[0]:
#         return False
#     for i in range(len(nums)):
#         if i - 1 >= 0:
#             if nums[i] == nums[i - 1]:
#                 return False

#     return True

# print(solve(listy1))
# # print(solve(listy12))
# # print(solve(listy13))


# l = ['5--10','--10-20-','20-30']
# z = ['0-10', '10--20', '20-30', '30-40-', '40--50-', '50-60', '6-0-70', '70-80-', '-80-90', '90-100-']

# def ErrorHandling(Naziya):
#     q = []
#     for i in Naziya:
#         try:
#             z = i.strip().split('-')
#             if len(z) > 2:
#                 for i in z:
#                     zs = str(i)
#                     try:
#                         if int(zs) == int(i):
#                             z1 = [z[0],z[-1]]
#                             q.append(i)
#                     except ValueError:
#                         continue
#             else:
#                 q.append(z)
#         except SyntaxError:
#             print('There Is Two Comma In Your Input Please Remove That')

#     return q


# q = ErrorHandling(z)

# a = []
# for i in q:
#     if type(i) == list:
#         for j in i:
#             a.append(j)
#     else:
#         a.append(i)

# k = 0
# o = 1
# newl = []
# newl2 = []

# for i in range(len(a)//2):
#     r = a[k] +"-"+ a[o]
#     k += 2
#     o += 2
#     newl.append(r)

# for i in a:
#     newl2.append(int(i))

# print(newl)
# print(newl2)

# print(newl2.count(10))

# import numpy as np

# a = [1,6,10,18,20,21,26,30,38,40]

# z = []
# for i in a:
#     if i == max(a):
#         z.append(1)

# if len(z) == len(a):
#     print("Mode is not possible")
# else:
#     print("running Function")


# def closestvalue(Naziya,Parveen):
#     o = 0
#     for i in Naziya:
#         if i>= Parveen:
#             o+=i
#             break
#         else:
#             continue

#     return o

# print(closestvalue(a,22))

# z = 400
# l = z**len(str(z))
# print(l)

# # def naz(d):
# #     z = 0
# #     for i in d:
# #         z+=1
# #         return d**z

# # print(naz(z))

# s = 4685
# for i in s:
#     print(i)


# def intfloatconverter(x):
#     if x == int(x):
#         z = int(x)
#         return z
#     else:
#         return x

# z = 8
# s = 5
# print(intfloatconverter(s-z))





# l = ['5--10','--10-20-','20-30']
# z = ['0-10', '10--20', '20-30', '30-40-', '40--50-', '50--60-', '60-70', '70-80-', '-80-90', '90-100-',]

# s = "5,8,6,9,8,9,6,8,5,2,5,"

# def ErrorHandling(Naziya):
#     q = []
#     for i in Naziya:
#         try:
#             z = i.strip().split('-')
#             # print(z)
#             if len(z) > 2:
#                 for j in z:
#                     print(j)
#                     zs = str(j)
#                     try:
#                         if int(zs) == int(j):
#                             z1 = [z[0],z[-1]]
#                             q.append(j)

#                         else:
#                             if zs == str(zs):
#                                 print('there is string')

#                     except ValueError:
#                         continue
#             else:
#                 q.append(z)
#         except SyntaxError:
#             print('There Is Two Comma In Your Input Please Remove That')

#     return q

# q = ErrorHandling(z)

# a = []
# for i in q:
#     if type(i) == list:
#         for j in i:
#             a.append(j)
#     else:
#         a.append(i)

# k = 0
# o = 1
# newl = []

# for i in range(len(a)//2):
#     r = a[k] +"-"+ a[o]
#     k += 2
#     o += 2
#     newl.append(r)

# print(newl)

# z = []
# z1 = s.strip().split(",")
# for i in z1:
#     if i == '':
#         continue
#     else:
#         z.append(i)
# print(len(z))
# print(z)

# def indexingfunction(l,Naziya):
#     indexlist = [i for i in range(len(l)) if l[i]==Naziya]
#     return indexlist

# print(indexingfunction([3,45,4,3],3))

# lis = [1,2,3,4,5,6]
# for i in range(len(lis)):
#     print(i)

# def intfloatconverter(x):
#     return int(x) if x == int(x) else x

# def floatstopper(x):
#     return float('{:.3f}'.format(x))

# def square(Naziya):
#     return [intfloatconverter(floatstopper(i**2)) for i in Naziya]
# l = [3,4,3]
# print(square(l))

# l = [39,59,49,59,38,40,30]
# for i in enumerate(l):
#     print(i)

# print(len(l))

# gen = 1
# print('this is message'+f'{gen}')

# def gen(x):
#     for i in range(x):
#         yield(i)

# lis = [i for i in range(100000)]
# for i in lis:
#     print(i)
#     lis.remove(i)
#     break

# z = [{'Message':
# {'Message1': 'There it is for second checking',
# 'Message2': 'this is subhan from web side',
# 'Message3': 'this is nothing just last message',
# 'Message4': 'fourth message'}}]

# j2 = []
# for k in z:
#     for i in k.values():
#         for j in i:
#             j2.append(j)
# print(j2)
# print(str(j2[-1])[-1])



# k2 = [j for j in i for i in k.values() for k in z]
# print(k2)


# v = {'Email1': 'almeenfatima7998@gmail.com',
# 'Email2': 'almeenfatima799@gmail.com'}

# # vs = [i for i in v.values()]

# if 'almeenfatima98@gmail.com' in v.values():
#     print(True)
# else:
#     print(False)



# vks = [{

#     'Email': 
#         {'Email1': 'Subhanali7861299@gmail.com',
#          'Email2': 'Subhanali78@gmail.com',         'Email3': 'Subhanali7861299@gmail.com', 
#          'Email4': 'Subhanali7861299@gmail.com', 
#          'Email5': 'Subhanali7897928120@gmail.com',}, 

#     'Message': 
#         {'Message1': 'HELLO ITS ME AGAIN',
#          'Message2': 'fasdfasd',
#          'Message3': 'fasdfasd',
#          'Message4': 'fasdfasd',},
# }] 

# # for i in vks:
# #     for mes in i.get('Message'):
# #         print(mes)
# j2 = []
# mai = 'Subhanali78@gmail.com'
# for adbra in vks:
#     for i in adbra['Email'].values():
#         j2.append(i)

# if mai in j2:
#     print('its here')
# else:
#     print('its not here')


# dic = {
#     'User1' : {
#         'Question1':{
#             'Firstinput':'',
#             'Secondinput':''
#         },
#         'Question2':{
#             'Firstinput':'',
#             'Secondinput':''
#         }
#     } ,

#     'User2' : {
#                 'Question1':{
#             'Firstinput':'',
#             'Secondinput':''
#         },
#         'Question2':{
#             'Firstinput':'',
#             'Secondinput':''
#         }
#     }
# }

# s = '127.0.0.1'
# print(s.replace('.','_'))

# z =['0-10,10-20,20-30,30-40,40-50,50-60,60-70,70-80,80-90,90-100', '1,5,4,8,2,1,10,4,8,2']

# l = [['0-10,10-20,20-30,30-40,40-50,50-60,60-70,70-80,80-90,90-100', '1,5,4,8,2,1,5,4,8,2'],
# ['25-35,35-45,45-55,55-65,65-75,75-85,85-95,95-105,105-115', '1,5,4,8,2,1,5,4,8'],
# ['0-10,10-20,20-30,30-40,40-50,50-60,60-70,70-80,80-90,90-100', '1,5,4,8,2,1,5,4,8,2']]

# if z not in l:
#     print('no')
# else:
#     print('yes')

# import pymongo
# import time

# Subhan = {
#     'Naz' : {
#         'sent': {
#             'Time':{
#                 'CurrentTime':'12:00pm',
#                 'Message':'hello this is me',
#             }
#         },
#         'received': '',
#     },
#     'subhan' : {
#         'sent': '',
#         'received': '',
#     },
#     'aman' : {
#         'sent': '',
#         'received': '',
#     },
#     'ashish' : {
#         'sent': '',
#         'received': '',
#     },
# }

# Name = 'subhan'
# usernumber = '+917897928120'
# number1 = '+919598947125'
# number2 = '+919336486847'
# time1 = time.time()
# sentmessage = 'hello there'
# receivedmessage = 'hii'
# currenttime = time.strftime("%I:%M:%S %p")

# Database_Link = pymongo.MongoClient("mongodb://localhost:27017")
# Database_Name = Database_Link["ChatsUp"]

# Collection_Name = Database_Name[Name]
# Data = {
#     usernumber : usernumber,
#     'data' : {
#         number1 : {
#             'sent': {
#                 currenttime :{
#                     'currenttime' : currenttime,
#                     'message' : sentmessage
#                 }
#             },
#             'received': {
#                 currenttime:{
#                     'currenttime' : currenttime,
#                     'message' : receivedmessage
#                 }
#             },
#         },
#     }
# }

# Collection_Name.insert_one(Data)

# time2 = time.time()
# print(time2-time1)

# checking_last_message_count = [i for i in Collection_Name.find({usernumber:usernumber},{'_id':0})]

# import Naziya as NAZIYA
# import math,random,time,asyncio

# a = time.strftime('%X')

# async def standarddev(firstinput,secondinput):
#     Naziya = {'root':[],
#         'classinterval':[],}

#     if firstinput == '' and secondinput == '':
#         Naziya['seriesname1'] = 'Please Enter Your Question First'
#         Naziya['emp'] = 0
#     else:
#         if firstinput == '':
#             Naziya['seriesname1'] = 'Please Enter X (No. of items) or C.I. (Class Interval)'
#             Naziya['emp'] = 0
#         else:
#             try:
#                 if secondinput == '':
#                     secondinput = '0'
#                 Naziya['match'] = secondinput

#                 # SEPERATING WITH COMMA
#                 list12 = (firstinput).strip().split(',')
#                 listnaz = (secondinput).strip().split(',')

#                 list2 = NAZIYA.ErrorHandling(listnaz).Empty_Error()
#                 list1 = list12
#                 li = list12

#                 try:
#                     cixitem = NAZIYA.ErrorHandling(li).Try()
#                 except ValueError:
#                     q = NAZIYA.ErrorHandling(list12).Dash_Error()
#                     colo = NAZIYA.ErrorHandling(q).Exception()
#                     li = colo[0]
#                     cixitem = colo[1]

#                 if len(cixitem) == len(list2):
#                     Naziya['seriesname'] = "CONTINUOUS SERIES"
#                     Naziya['classinterval'] = li

#                     firstlist = [i for i in cixitem]
#                     Naziya['x'] = firstlist

#                     # # SECOND LIST
#                     secondlist = [int(i) for i in list2]
#                     Naziya['f'] = secondlist

#                     # SUM OF X FIRST LIST
#                     sumof_x = sum(cixitem)
#                     Naziya["sumx"]= sumof_x

#                     # SUM OF F SECOND LIST
#                     sumof_f = sum(secondlist)
#                     Naziya["sumf"]= sumof_f

#                     # # TAKING ASSUME MEAN
#                     assumed_mean = random.choice(firstlist)
#                     Naziya["assumedmean"]= assumed_mean

#                     # CALCULATING DEVIATION
#                     deviation = NAZIYA.substraction(firstlist,assumed_mean)
#                     Naziya['d'] = deviation
#                     Naziya["sumd"]= sum(deviation)

#                     # DEVIATION SQUARE
#                     deviation2 = NAZIYA.square(deviation)
#                     Naziya['d2'] = deviation2
#                     Naziya["sumd2"]= sum(deviation2)

#                     # FREQUENCY AND DEVIATION MULTIPLY
#                     fdeviation = NAZIYA.multiply(secondlist,deviation)
#                     Naziya['fd'] = fdeviation
#                     Naziya["sumfd"]= sum(fdeviation)

#                     # FREQUENCY AND DEVIATION SQUARE MULTIPLY   
#                     fdeviation2 = NAZIYA.multiply(secondlist,deviation2)
#                     Naziya['fd2'] = fdeviation2
#                     Naziya["sumfd2"]= sum(fdeviation2)

#                     # DIVINDING SUMMATION FD2 WITH SUMMATIOM F
#                     divide1 = NAZIYA.floatstopper2(sum(fdeviation2)/sumof_f)
#                     Naziya['divide1']= divide1

#                     divide2 = NAZIYA.floatstopper2(sum(fdeviation)/sumof_f)
#                     Naziya['divide2']= divide2

#                     square2 = divide2*divide2
#                     g = NAZIYA.floatstopper(square2)
#                     Naziya['square2'] = g

#                     subs = divide1 - g
#                     g1 = NAZIYA.floatstopper(subs)
#                     Naziya['subs'] = g1

#                     sqrroot = NAZIYA.floatstopper(math.sqrt(g1))
#                     Naziya['sqrroot'] = sqrroot

#                     # ACTUAL MEAN METHOD
#                     parveen = NAZIYA.multiply(firstlist,secondlist)
#                     Naziya['fx'] = parveen
#                     Naziya['sumfx']=sum(parveen)

#                     # TAKING ACTUAL MEAN
#                     actualmean = sum(parveen)/sumof_f
#                     Naziya['actualmean'] = NAZIYA.floatstopper(actualmean)

#                     # CALCULATION DEVIATION OF ACTUAL MEAN METHOD
#                     acdeviation = NAZIYA.substraction(firstlist,actualmean)
#                     Naziya['acd'] = acdeviation
                    
#                     nazpar= sum(acdeviation)
#                     nazpar1 = NAZIYA.floatstopper2(nazpar)
#                     Naziya["sumacd"]= nazpar1

#                     # ACTUAL MEAN DEVIATION SQUARE
#                     acdeviation2 = NAZIYA.square(acdeviation)
#                     Naziya['acd2'] = acdeviation2
#                     varacd2 = sum(acdeviation2)
#                     nazpar21 = NAZIYA.floatstopper2(varacd2)
#                     Naziya["sumacd2"]= nazpar21

#                     # ACTUAL MEAN FREQUENCY AND DEVIATION SQUARE MULTIPLY

#                     acfdeviation2 = NAZIYA.multiply(secondlist,acdeviation2)
#                     Naziya['acfd2'] = acfdeviation2
                    
#                     varac= NAZIYA.floatstopper2(sum(acfdeviation2))

#                     varac1 = NAZIYA.intfloatconverter(varac)
#                     Naziya["sumacfd2"]= varac1

#                     divide3 = sum(acfdeviation2)/sumof_f
#                     Naziya['divide3'] = NAZIYA.floatstopper2(divide3)

#                     acsqr = NAZIYA.floatstopper(math.sqrt(divide3))
#                     Naziya['acsqrroot'] = acsqr

#                     # COEFFICIENT OF STANDARD DEVIATION
#                     cosd = NAZIYA.floatstopper(acsqr/actualmean)
#                     Naziya['coefficientofsd'] = cosd
#                     Naziya['coefficientofvar'] = cosd*100
#                     Naziya['variance'] = acsqr**2

#                     return acsqr

#             except:
#                 Naziya['allerror'] = 'Handle'
#                 Naziya['seriesname1'] = 'Please Enter Your Question Correctly'

# async def median(firstinput,secondinput):

#     Naziya = {'root':[],
#         'parveen':'Click Below To Solve Median',
#         'cando':'Please enter your question with comma seperated in textbox',
#         'question':'Median',
#         'info':'Ex - 52,85,64,41,92,34......(For Individual/Discrete Series)',
#         'info2':'Ex - 0-10,10-20,20-30......(For Continuous Series)',}


#     if firstinput == '' and secondinput == '':
#         Naziya['seriesname1'] = 'Please Enter Your Question First'
#         Naziya['emp'] = 0
#     else:
#         if firstinput == '':
#             Naziya['seriesname1'] = 'Please Enter X (No. of items) or C.I. (Class Interval)'
#             Naziya['emp'] = 0
#         else:
#             try:
#                 if secondinput == '':
#                     secondinput = '0'
#                 Naziya['match'] = secondinput

#                 # SEPERATING WITH COMMA
#                 list12 = (firstinput).strip().split(',')
#                 listnaz = (secondinput).strip().split(',')
                
#                 list2 = NAZIYA.ErrorHandling(listnaz).Empty_Error()
#                 list1 = list12
#                 li = list12

#                 try:
#                     cixitem = NAZIYA.ErrorHandling(li).Try()
#                 except ValueError:
#                     q = NAZIYA.ErrorHandling(list12).Dash_Error()
#                     colo = NAZIYA.ErrorHandling(q).Exception()
#                     li = colo[0]
#                     cixitem = colo[1]

#                 if len(cixitem) == len(list2):
#                     # FOR CONTINUOUS SERIES
#                     Naziya['seriesname'] = "CONTINUOUS SERIES"
#                     Naziya['len1'] = len(list1)
#                     Naziya['dislen'] = len(list1)
#                     Naziya['len'] = len(list1)

#                     Naziya['classinterval'] = li
#                     f = NAZIYA.intfloatconverter_list(list2)
#                     Naziya['f'] = f

#                     # TAKING SUM OF F
#                     Naziya['sumf'] = sum(f)

#                     # TAKING N/2
#                     sum_f = NAZIYA.intfloatconverter(NAZIYA.floatstopper(sum(f)/2))
#                     Naziya['n2'] = sum_f

#                     # TAKING CUMULATIVE FREQUENCY
#                     cf = NAZIYA.Cumulative(f)
#                     Naziya['cf'] = cf

#                     # CHOOSING CLOSEST VALUE IN LIST
#                     val= NAZIYA.closestvalue(cf,sum_f)
#                     indexing = NAZIYA.Indexing(val,sum_f,cf).Median_Indexing()

#                     # TAKING POSITION IN LIST
#                     cfp = cf[indexing-1]
#                     Naziya['cfp'] = cfp

#                     # TAKING F1 AND L1
#                     f1 = f[indexing] #F1
#                     Naziya['f1'] = f1
                    
#                     l = (li[indexing]).strip().split('-')
#                     l1 = int(l[0]) #L1
#                     Naziya['L1'] = l1

#                     Naziya['i'] = int(l[1]) - int(l[0]) if int(l[0]) > int(l[1]) else int(l[1]) - int(l[0])

#                     divide1 = NAZIYA.intfloatconverter(sum_f/1)
#                     Naziya['divide1'] = divide1

#                     calc = (divide1 - cfp) * Naziya['i']
#                     calc1 = NAZIYA.intfloatconverter(calc)
#                     Naziya['multiply1'] = calc1

#                     med = calc1 / f1
#                     med1 = l1 + med
#                     Naziya['divide2'] = NAZIYA.intfloatconverter(NAZIYA.floatstopper(med))
#                     Naziya['median'] = NAZIYA.intfloatconverter(med1)
#                     return med1
#             except:
#                 Naziya['allerror'] = 'Handle'
#                 Naziya['seriesname1'] = 'Please Enter Your Question Correctly'

# def multiply(n):
#     a = 1
#     for i in range(1,n):
#         a*=i
#     print('this is task a', a)

# def multiply2(n):
#     b = 1
#     for i in range(1,n):
#         b*=i
#     print('this is task b',b)

#This is timing without async funtion 0.305003643035888

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)

# async def main():

#     task1 = asyncio.create_task(
#         multiply(20000))

#     task2 = asyncio.create_task(
#         multiply(90000))

#     a = time.strftime('%X')

#     # Wait until both tasks are completed (should take
#     await task1
#     await task2

#     print(a)
#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())

# import asyncio
# import time

# async def main():

#     task1 = asyncio.create_task(multiply(90000))
#     task3 = asyncio.create_task(multiply(10000))
    
#     a = time.strftime('%X')
#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)

#     await task1
#     await task3

#     print(f"started at {a}")
#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())

# This is timing without async funtion 8.635000944137573

# import threading
# import Naziya as NAZIYA
# import math,random,time,asyncio

# z = time.strftime('%X')

# def multiply(n):
#     a = 1
#     for i in range(1,n):
#         a*=i
#     print('this is task a', a)

# def multiply2(n):
#     b = 1
#     for i in range(1,n):
#         b*=i
#     print('this is task b',b)


# def master():
#     multiply(10000)
#     time.sleep(0.0000000000000000000000000001)

# multiply(90000)

# a = threading.Thread(target=master, args=(10000,))
# a.start()
# b = threading.Thread(target=multiply2, args=(90000,))
# b.start()

# a.join()
# b.join()

# print('this is starting time',z)
# print('this is ending time',time.strftime('%X'))



# print(threading.active_count())




# import threading,time

# def func():
#     print('hello')
#     time.sleep(0.1)
#     print('Parveen')

# x = threading.Thread(target=func)
# x.start()

# time.sleep(0.05)
# print('Naziya')
# print(threading.active_count())

# x.join()

# print(threading.active_count())

# class Solution:
#     def __init__(self,*Naziya) -> None:
#         self.lis = Naziya[0]
#         self.targ : int = Naziya[1]

#     def twoSum(self):
#         self.li = []
#         self.var = 1

#         # [ 4,2,1,5,2 ]
#         # [ 7 ]
#         for i in range(len(self.lis)+1):
#             a = self.lis[i] + self.lis[i+self.var]
#             if a == self.targ:
#                 self.li.append(self.lis.index(self.lis[i]))
#                 self.lis[i]= self.lis[i]+1
#                 self.li.append(self.lis.index(self.lis[i+self.var]))
#                 break
#         return self.li

# a = Solution([3,2,3], 6).twoSum()
# print(a)


# import concurrent.futures,multiprocessing,time

# a = time.perf_counter()

# def multiply(n):
#     a = 1
#     for i in range(1,n):
#         a*=i    
#         return a

# def multiply2(n):
#     b = 1
#     for i in range(1,n):
#         b*=i
#     return b


# with concurrent.futures.ProcessPoolExecutor() as executor:
#     a = executor.submit(multiply,90000)
#     print(a.result())

# d = multiprocessing.Process(target=multiply2,args=[10000])
# d.start()
# d.join()

# b = time.perf_counter()
# print('finished in ', round(b-a,2))

# if __name__ == '__main__':  
#     multiprocessing.freeze_support()

# d = multiprocessing.Process(target=multiply,args=[90000])
# d.start()
# d.join()

# print('this code took this minute to finish')

# import sys
# import time
# import multiprocessing

# def multiply2(n):
#     a = 1
#     for i in range(1,n):
#         a*=i    
#     sys.set_int_max_str_digits(1000000)
#     return a

# def multiply():
#     print('goint to sleep')
#     time.sleep(2)
#     print('done sleeping')

# a = time.perf_counter()

# import cProfile,pstats
# if __name__ == '__main__':
    # multiprocessing.freeze_support()
    # child = multiprocessing.Process(target=multiply2,args=[90000])
    # child1 = multiprocessing.Process(target=multiply2,args=[10000])
    # child.start()
    # child1.start()
    # child.join()
    # child1.join()
    # b = time.perf_counter()
    # print('finished in', round(b-a,2),'seconds')


    # with cProfile.Profile() as Naz:
    #     m = multiply()
    #     # m1 = multiply2(10000)k
    #     print(m)
    #     # print(m1)
    
    # results = pstats.Stats(Naz)
    # results.sort_stats(pstats.SortKey.TIME)
    # results.print_stats()
    # results.dump_stats("result.prof")
# a = time.perf_counter()

# if __name__ == '__main__':
#     multiprocessing.freeze_support()
#     d1 = []
#     for _ in range(10):
#         d = multiprocessing.Process(target=multiply)
#         d.start()
#         d1.append(d)
#     for process in d1:
#         process.join()

#     b = time.perf_counter()
#     print('finished in', round(b-a,2),'seconds')

    
di = [10,45,45,65]
sum = 0
for k in di:
    sum += k
print(sum)

print(len(di))

l = ['naziya','sa','kd']
print(l[1][-1])

a = True
b = False
c = False
ki = 'Hello My World Naziya'

if a or b and c:
    print('hello')
else:
    print('nothing')

class Indexing:
    def __init__(self, *Naziya) -> None:
        self.naz = Naziya[0] 
        self.target = Naziya[1]

    async def function(self) -> None:
        for i in self.naz:
            if i == self.target:
                print(await i)


process = Indexing(di, 65).function()

if a == b:
    print('C')
else:
    print("D")

class solution:
    def two_sums(self,nums,target) -> None:
        self.lis = nums
        self.targ = target
        
        for i in self.lis:
            for j in self.lis:
                if i+j == self.targ:
                    return [self.lis.index(i),self.lis.index(j)]
        return None

a = 45
kd = 'Hello'
r = 4
d = [4,5,65,4]
def funct(d,r):
    if r in d: return r

a = solution().two_sums([2,4,5,6,4,4],11)
print(a)
b = Solution().twoSum([2,2,4],4)
print(b)

k = True
d = False











































# Advance Python Course Revision


#                           Module Importing Name Main Method

# import os
# print(os.listdir('/'))

# def mostimportantfunction():
#     print("everything is a lie")

# def main():
#     print('there is everything that can change')

# if __name__ == "__main__":
#     main()



#                                   *Args **Kwargs

# def nazpar(name,age,gender):
#     print("name =" ,name, "age =" ,age, "gender = " ,gender)

# nazpar('Subhan Ali',21,'male')

# def nazpar(*args):
#     if len(args) == 3:
#         print("name =" ,args[0], "age =" ,args[1], "gender = " ,args[2])
#     else:
#         print("kindly enter your name,age and gender")

# nazpar1 = ['Subhan Ali',21,'male']
# nazpar(*nazpar1)    # use star * operator to unpack list and pass it in args function

# marklist = {
#     'harry': 85,'john': 96,'sara':59,'nikola':60,'henry':40,
# }
# def printmark(**kwargs):
#     print(type(kwargs))
#     for key,value in kwargs.items():
#         print(key,',', value)
# printmark(**marklist)

# def master(normal,*args,**kwargs):
#     print(normal)
#     for i in args:
#         print(i)
#     for key,value in kwargs.items():
#         print(key,',',value)

# master('naziya',*nazpar1,**marklist)



#                                Try,Except And Finally

# try:
#     open('this.txt')
# except Exception as e:
#     print(e)

# try:
#     open('this.txt')
# except EOFError as e:
#     print('eof error')
# except IOError as e:
#     print('io error')
# else:
#     print('this statement will print if there is no exception. if exception statement will not run this will run. if exception statement will run this will not run')
# finally:
#     print('no matter what this will print either try,except statement will run or else statement will will run this will always print')



#                           Comprehension (List, Dictionary, Set, Generator)

# # List Comprehension
# list_1 = [1,44,3,454,8,58,95,83,93,95,9]

# divide_by_3 = []
# for i in list_1:
#     if i%3 == 0:
#         print(i)

# lk = [i for i in list_1 if i%3 == 0]
# print(lk)

# # Dictionary Comprehension
# dict_1 = {'a':56,'b':75,'c':95,'d':94,'e':84,'A':83,'B':95}
# kd = {k.lower():dict_1.get(k.lower(),0) + dict_1.get(k.upper(),0) for k in dict_1.keys() }
# print(kd)

# # Set Comprehension
# set_1 = {a**2 for a in [1,2,3,4,5,5,5,5,3,2,4]}
# print(set_1)

# # Generator Comprehension
# gen_1 = (i for i in range(55) if i%2==0)
# for i in gen_1:
#     print(i)



#                                     Iterable, Iterator, Iteration

# Iterable is generated by Iterator which is a generator which doesn't consume ram memory but allocate
# a object in ram without consuming ram 

# def generator(n):
#     for i in range(n):
#         yield i

# # g = generator(10000000)

# # for i in g:
# #     if i == 49595:
# #         print(i)
# #         break

# obj_1 = generator(4)
# print(next(obj_1))
# print(next(obj_1))
# print(next(obj_1))

# of = '543'
# it = iter(of)
# print(it)
# for i in it:
#     print(i)



#                                           Map, Filter, Reduce Function

# def square(n):
#     return n**2
# def qube(l):
#     return [i**3 for i in l]

# l1 = [1,2,3,4,5,6]
# sq = qube(list(map(square,l1)))
# print(sq)

# def greater_then_2(n):
#     return True if n>2 else False
# h2 = [5,3,5,0,-1,3,-5,-6,3]
# print(list(filter(greater_then_2,h2)))

# from functools import reduce

# def sum_num(a,b):
#     return a+b
# Lili = reduce(sum_num,[1,2,4,6,4,3,5,4])
# print(Lili)


#                                               Enumerate Function

# a = ['tseries', 'gyan therapy', 'vashishth', 'enumerate', 'function', 'naz']
# j = 0
# for i in a:
#     j += 1
#     if j%2==0:
#         print(i)

# for item,dict in enumerate(a):
#     if item+1%2 == 0:
#         print(item,dict)


#                                               Advance List Slicing

# list1 = [1,2,4,5,6,7,8]
# # print(list1[1:30]) #this will not throw error even if list is out of slicing (python 3.6 and after version will handle this automatically)

# # print(list1[-5:])
# # print(list1[-3:])
# # print(list1[-9:-2])

# print(list1[::-2])


#                                                  Bisect Module

# import time
# import bisect as Naziya

# t1 = time.time()
# number = 6.5
# a = [21,3,55,6,7,9,10,11,12]
# print(Naziya.bisect(a,number))
# Naziya.insort(a,number)
# print(a)
# t2 = time.time()

# print(t2-t1)


#                                                 Format Function

# users = ['subhan', 'naziya', 'ali', 'parveen']
# computer = ['rasberry pie', 'iphone', 'android', 'windows']
# for i in range(len(users)):
#     template = '{} computer is used by {} '
#     print(template.format(computer[i], users[i]))


# #                                                  Join Function

# lis = ['chalk', 'duster', 'pen', 'board']
# print(','.join(lis))

# z = '''
# this
# is
# python 
# string
# with 
# line
# change'''
# print(z)

# x = complex(10,-5.6)
# print(x)

# c = bool()
# print(c)

# kd:list = 10
# kd:int =  40
# print(kd)

# print(11%3) # % Use to get reminder of a division
# print(12%3) 

# print(11.5//3)


# print(int(input('Enter Your first number here : ')) + int(input('enter your second input : ')))

a = '()]['

b = a.count('(')
c = a.count(')')
d = a.count('[')
k = a.count(']')
l = a.count('{')
o = a.count('}')

if b == c and d == k and l == o:
    print("True")
else:
    print('False')























































































































