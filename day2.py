#TASK1
import re
with open('input2.txt') as f:
    input2 = f.readlines()
#print(input2)
i = 0
while i< len(input2):
    input2[i] = re.sub("\n", "", input2[i])
    i = i+1
#print(input2)

newlist = []
for i in input2:
    newlist.append(i.split(' '))

#print(newlist[0][0])
#making a list of list, ach element has the direction variable and the number

l=0
forwardcount = 0
depthcount = 0
while l < len(newlist):
    if newlist[l][0] == 'forward':
        forwardcount = forwardcount + int(newlist[l][1])
        #print(newlist[l][0])
        #print(forwardcount)
    elif newlist[l][0] == 'down':
        depthcount = depthcount + int(newlist[l][1])
        #print(newlist[l][0])
        #print(depthcount)
    elif newlist[l][0] == 'up':
        depthcount = depthcount - int(newlist[l][1])
        #print(newlist[l][0])
        #print(depthcount)

    l = l+1

#print(forwardcount)
#print(depthcount)
print('task 1 answer = ',forwardcount*depthcount)

#TASK2
# now if forward also does depthcount + aim*x
#down means aim +x
#up means aim -x
#print('task 2')
l=0
forwardcount = 0
depthcount = 0
aim = 0
while l < len(newlist):
    if newlist[l][0] == 'forward':
        forwardcount = forwardcount + int(newlist[l][1])
        depthcount = depthcount + (aim*int(newlist[l][1]))
    elif newlist[l][0] == 'down':
        aim = aim + int(newlist[l][1])
    elif newlist[l][0] == 'up':
        aim = aim - int(newlist[l][1])

    l = l+1

#print(forwardcount)
#print(depthcount)
#print(aim)
print('task 2 answer = ',forwardcount*depthcount)