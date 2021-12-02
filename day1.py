#TASK 1
import re
with open('input1.txt') as f:
    input1 = f.readlines()

i = 0
while i< len(input1):
    input1[i] = int(re.sub("\n", "", input1[i]))
    i = i+1

#print(input1)
#above reading in the input text file and removing the /n and making a list of inputs

def checkprevious(x,y):
    if x<y:
        return 'smaller'
    elif x>y:
        return 'larger'
    else:
        return 'same'

#print(checkprevious(5,10))
#creating a function that compares two inputs and returns if the first is smaller larger or the same then testing it
s=0
count = 0
while s < len(input1):
    result = checkprevious(input1[s-1],input1[s])
    if result == 'smaller':
        count = count+1
    s = s+1
# go through every element and use fucntion to compare to last
#if smaller add one to count
print(count)

#TASK 2
t=0
sumlist = []
while t < (len(input1)-2):
    sum = (input1[t] + input1[t+1] + input1[t+2])
    sumlist.append(sum)

    t = t+1
#make a list of all the sums of three

s=0
count = 0
while s < len(sumlist):
    result = checkprevious(sumlist[s-1],sumlist[s])
    if result == 'smaller':
        count = count+1
    s = s+1
# go through every element and use fucntion to compare to last
#if smaller add one to count
print(count)

#reused the code from the first part to compare and add to count