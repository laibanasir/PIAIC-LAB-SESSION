#------import random module------
import random

#------Create an empty list------
numbers = []

#------Append 100 random numbers to the numbers list------
for num in range (100):
    n = random.randint(1,1000)
    numbers.append(n)
print('This list consists of the following numbers : \n', numbers)

#------Finding mean------
total = 0
for i in numbers :
    total += i
mean = total / 100
print('\nNumbers in list : 100' , '\nTotal           : ' , total , '\t Mean : ' , mean)

#------Using max and min function------
maxnum = max(numbers)
minnum = min(numbers)
indexmax = numbers.index(maxnum)
indexmin = numbers.index(minnum)
print('Maximum number  : ' , maxnum , '\t\tIndex : ' , indexmax)
print('Minimum number  : ' , minnum , '\t\tIndex : ' , indexmin)
print('\n---------------------------------------------')
