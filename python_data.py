# write a python function which takes length , breadth as user input and returns the area of rectangle.
def rectangle_area(length, breadth):
    area = length * breadth    
    return area

# write a python function which takes a number as user input and print square, and cube of the number
def square_cube(number):
    print(number ** 2)  
    print(number ** 3)  
    
# write a python program that takes height in centimeters as user input and return height in feet and inches   
cm=int(input("Enter the height in centimeters:"))
inches=0.394*cm
feet=0.0328*cm
print("The length in inches",round(inches,2))
print("The length in feet",round(feet,2))

# write a python program to remove duplicates from the list and print the result
l = [1,2,3,4,5,5,5,5,5,5,5,7,8,8,0]
result = set(l)
print("Result : ",result)

#write a python function which takes length of sides as user input to calculate and return the area of a triangle

def triangle_area(a,b,c):
    s = (a+b+c)/2
    area = (s(s-a)*(s-b)*(s-c)) ** 0.5
    return(area)

# write a python program to swap two numbers
num1 = 130
num2 = 34
num1,num2 = num2,num1
 
# Write a python program to obtain principal amount, rate of interest and time from user to print simple interest.
principal = float(input("Enter principal : "))
rate= float(input("Enter rate : "))
time = float(input("Enter time : "))
simple_interest = print(f"Simple Interest : {(principal*rate*time/100)}")

# write a python program using while loop to reverse a number and print the reversed number
Number = int(input("Please Enter any Number: "))    
Reverse = 0    
while(Number > 0):    
    Reminder = Number %10    
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print("\n Reverse of entered number is = %d" %Reverse)  

# write a python program to take year as input and check if it is a leap year or not

year = int(input("Enter a year: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print(f"{year} is a leap year")  
       else:  
           print(f"{year} is not a leap year")  
   else:  
       print(f"{year} is a leap year")  
else:  
   print(f"{year} is not a leap year")
   
# write a python program to input a number to test and print if it is a prime number

num = int(input("Enter number :"))
lim = int(num/2) + 1
for i in range(2,lim):
    rem = num % i
    if rem == 0 :
        print(num,"is not a prime number")
        break
else:
    print(num,"is a prime number")
    
# write a python program to input a string from user and convert input string into all upper case and print the result
string = input("Please Enter your Own String : ")

string1 = string.upper()
 
print("\nOriginal String in Lowercase  =  ", string)
print("The Given String in Uppercase =  ", string1)

# write a python program to input a string from user and count vowels in a string and print the output

str1 = input("Please Enter Your Own String : ")
vowels = 0
 
for i in str1:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A'
       or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1
 
print("Total Number of Vowels in this String = ", vowels)

# write a python program to input a Number N from user and print Odd Numbers from 1 to N

maximum = int(input(" Please Enter any Maximum Value : "))

for number in range(1, maximum + 1):
    if(number % 2 != 0):
        print("{0}".format(number))
        
# write a python program to input a Number N from user and print Even Numbers from 1 to N

maximum = int(input(" Please Enter the Maximum Value : "))

for number in range(1, maximum+1):
    if(number % 2 == 0):
        print("{0}".format(number))
        
# write a python program to input two numbers from user and add two Numbers and print the result

number1 = input(" Please Enter the First Number: ")
number2 = input(" Please Enter the second number: ")

sum = float(number1) + float(number2)
print('The sum of {0} and {1} is {2}'.format(number1, number2, sum))

# write a python program that takes two integers as input and check if the first number is divisible by other

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
remainder  = num1 % num2
if remainder == 0:
    print(num1 ," is divisible by ",num2)
else :
    print(num1 ," is not divisible by ",num2)
    
# write a python program to print the table of input integer

num = int(input("Please enter a number "))
for a in range(1,11):
    print(num , 'x' , a , '=' ,num*a)
    
# write a python program to print the factorial of number
num = int(input("Please enter a number "))
fact = 1
a = 1
while a <= num :
    fact *= a
    a += 1
print("The factorial of ",num, " is ",fact)

# write a python program which takes 3 numbers as input and to print largest of three numbers using elif statement

a = float(input("Please Enter the First value: "))
b = float(input("Please Enter the First value: "))
c = float(input("Please Enter the First value: "))

if (a > b and a > c):
          print("{0} is Greater Than both {1} and {2}". format(a, b, c))
elif (b > a and b > c):
          print("{0} is Greater Than both {1} and {2}". format(b, a, c))
elif (c > a and c > b):
          print("{0} is Greater Than both {1} and {2}". format(c, a, b))
else:
          print("Either any two values or all the three values are equal")
          
# write a python program which takes input a number N and print first N elements of fibonacci series

N = int(input("Please enter a number "))
first = 0
second = 1
print(first)
print(second)
for a in range(1,N-1):
    third = first + second
    print(third)
    first,second = second , third
    
# write a python program to print the divisors of a integer
num = int(input("Please enter a integer "))
mid = int(num / 2)
print("The divisiors of ",num," are :" )
for a in range(2,mid + 1):
    if num % a == 0:
        print(a, end = ' ')
else :
    print()
    print("-End-")
    
# write a python program to find the average of list of numbers provided as input by user
n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))

# write a python program which takes an integer N as input and add the odd numbers up to N and print the result

N = int(input("Enter Number : "))
sum = 0
i = 1
while i <= N:
    sum = sum + i
    i = i + 2
print(sum)

# write a python function which takes input a string and returns whether is is a palindrome or not

def isPalindrome(s):
    return s == s[::-1]
 
# write a python program which takes list as an input and calculate mean of given list of numbers 
lst = eval(input("Enter list : "))
mean = 0
sum = 0
for i in lst:
    sum  = sum + i
mean = sum / len(lst)
print(" The mean of given list is :", mean)

# write a python program which takes list as an input and calculate sum of given list of numbers 
lst = eval(input("Enter list : "))
mean = 0
sum = 0
for i in lst:
    sum  = sum + i
print(" The mean of given list is :", sum)

# write a python program which takes list as an input and find frequency of all elements in list 
lst = eval(input("Enter list : "))
mean = 0
sum = 0
for i in lst:
    sum  = sum + i
print(" The mean of given list is :", sum)

# write a python function that takes two lists as an input an print out common elements in two lists

def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
  
    if (a_set & b_set): 
        print(a_set & b_set) 
    else: 
        print("No common elements")  
        
# write a python function that takes two lists and append second list after the first list 
lst1 = eval(input("Enter list : "))
lst2 = eval(input("Enter list : "))
print(lst1 + lst2)


# write a python program to calculate and print square root of numbers 0 to 100
i = 0
while i<= 100:
 print(i, "\t\t" , i**0.5)
 i = i + 1

#write a python program greets the user with "Hello", after user inputs his name:
name = input ("Input your name: ")
print("HELLO ", name)

# write a python program which takes input a string and print reverse string
name = input("Enter String")
print(name[::-1]) 

# write a python program which takes input a list and print reverse output
lst = eval(input("Enter list"))
print(lst[::-1]) 

# write a python function which takes sentence as input and remove vowels from a sentence

sentence = input("Enter a sentence : ")

def fn(sentence):
    vowels = 'aeiou'
    return ''.join([ l for l in sentence if l not in vowels])

# write a python function which takes two list of same length as input and return a dictionary with one as keys and other as values.

keys = eval(input("Enter key list : "))
values = eval(input("Enter value list : "))
def fn(keys, values):
    return { keys[i] : values[i] for i in range(len(keys)) }

# write a python function that takes an integer as input and returns the factorial of that number

def factorial(n): 
      
    # single line to find factorial 
    return 1 if (n==1 or n==0) else n * factorial(n - 1); 

# write a python function that takes input radius and return area of circle
def findArea(r): 
    PI = 3.142
    return PI * (r*r);

# write a python funtion that takes input principle, rate, time and calculate compound intrest

def compound_interest(principle, rate, time):
    # Calculates compound interest  
    Amount = principle * (pow((1 + rate / 100), time)) 
    CI = Amount - principle 
    print("Compound interest is", CI) 
    
# write a python program to print the ascii value of input character

character = input(" Enter Character :")
print(f"Ascii value of character {character} is : " , ord(character))

# write a python program that takes input an integer and find sum of series with cubes of first n natural numbers using list comprehension which ta
N = int(input("Enter Integer "))
lst = [i**3 for i in range(1, N + 1)]
print(sum(lst)) 

# write a python function that takes list as an input and converts it into tuple
def convert(list): 
    return tuple(list)

# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 

def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# write a python program to concatenate two dictionaries

d1 = {'a' : 1 ,'b' : 2}
d2 = {'c' : 1 ,'d' : 2}
d3 = {**d1,**d2}
print(d3)

# Write a Python program to print the length of a set.

#Create a set
seta = set([5, 10, 3, 15, 2, 20])
#Find the length use len()
print(len(seta))

# write a python program that takes two sets as input and print the common elements
s1 = eval(input("Enter set 1 "))
s2 = eval(input("Enter set 2 "))
print(s1.intersection(s2))

# write a python program which takes input a list and prints the mean of elements within the list
s1 = eval(input("Enter list "))
mean = sum(s1) / len(s1) 
print("Mean of sample is : " + str(mean)) 


# write a python program which takes input a list and prints the standard deviation of elements within the list
mean = sum(s1) / len(s1) 
variance = sum([((x - mean) ** 2) for x in s1]) / len(s1) 
res = variance ** 0.5
print("Standard deviation of sample is : " + str(res)) 

# write a python program which prints a random number
import random
n = random.random()
print(n) 

# write a python function that takes input a string and removes duplicates from the same
foo = input("Enter String : ")
print("Duplicates Removed","".join(set(foo)))

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1

# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1

# Write a Python program to count the occurrences of each word in a given sentence.
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


# Write a Python function to create the HTML string with tags around the word(s).
def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)

# Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
             
#Write a Python program that prints each item and its corresponding type from the following list.

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]
for item in datalist:
   print ("Type of ",item, " is ", type(item))


# Write a Python program to sort (ascending) a dictionary by value.
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print({k :v for k,v in sorted(d.items(),key = lambda x : x[1])})

# Write a Python program to sort (Descending) a dictionary by value.
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print({k :v for k,v in sorted(d.items(),key = lambda x : x[1],reverse = True)})

# Write a Python program to sort list.
numbers = [1, 3, 4, 2] 
numbers.sort()  
print(numbers) 

# Write a Python program to sort a list of tuples by second Item
def Sort_Tuple(tup):  

    return(sorted(tup, key = lambda x: x[1]))   
  
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]  

print(Sort_Tuple(tup)) 

# write a python program that tke two inputs from user and check whether they are equal or not.
print("Enter first number")
first = input()
print("Enter second number")
second = input()
print(first == second)

# write a python program that takes input a list and squares every term using list comprehension
s1 = eval(input("Enter list "))
print([i**2 for i in s1])

# write a python program that takes input a list and cube every term using list comprehension

s1 = eval(input("Enter list "))
print([i**3 for i in s1])

# write a python program that takes input a list and square root every term using list comprehension

s1 = eval(input("Enter list "))
print([i**0.5 for i in s1])

# write a python function that takes input a list of string and print the largest string
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]

# write a python program that takes input a string and prints the count of words

s1 = input("Enter string ")
print("Count of words",len(s1.split()))

# write a Python function that takes list of tuples as input and sort those alphabetically
def SortTuple(tup): 
      
    n = len(tup) 
      
    for i in range(n): 
        for j in range(n-i-1): 
              
            if tup[j][0] > tup[j + 1][0]: 
                tup[j], tup[j + 1] = tup[j + 1], tup[j] 
                  
    return tup 

# write a python program which takes a list and swaps the first and last value of the list.
a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("New list is:")
print(a)

# write a python program that print today's date
from datetime import date
print(date.today()) 

# write a python program that takes input number of lines and finds the possible number of intersection
def countMaxIntersect(n): 
    return int(n*(n - 1)/2) 

# write a python program to input a number n and print an inverted star pattern of the desired size.
n=int(input("Enter number of rows: "))
for i in range (n,0,-1):
    print((n-i) * ' ' + i * '*')
    
# write a python program to input a number and check whether a given number is a palindrome.

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
    
# write a python program to input a number and find the smallest divisor of an integer. 
 
n=int(input("Enter an integer:"))
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
a.sort()
print("Smallest divisor is:",a[0])

# write a python program to accept three distinct digits and prints all possible combinations from the digits.

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])

# write a python function to insert an element into sorted python list

def insert(list, n): 
      
    for i in range(len(list)): 
        if list[i] > n: 
            index = i 
            break
      
 
    list = list[:i] + [n] + list[i:] 
    return list

# write a python program to add two numbers
num1 = 1.5
num2 = 6.3
sum = num1 + num2
print(f'Sum: {sum}')

# write a python function to add two user provided numbers and return the sum
def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum

# write a program to find and print the largest among three number
snum1 = 10
num2 = 12
num3 = 14 
if (num1 >= num2) and (num1 >= num3): 
   largest = num1
elif (num2 >= num1) and (num2 >= num3):   
    largest = num2
else:   largest = num3
print(f'largest:{largest}')

# write a python function to subtract two user provided numbers and return the result
def sub_two_numbers(num1, num2):
    sub = num1 - num2
    return sub

# write a python function to multiply two user provided numbers and return the result
def mul_two_numbers(num1, num2):
    mul = num1 * num2
    return mul

# write a python program to pop element form dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))

#write a python program that prints the length of tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))





