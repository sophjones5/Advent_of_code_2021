#TASK 1
import re
with open('input3.txt') as f:
    input3 = f.readlines()
#print(input3)
i = 0
while i< len(input3):
    input3[i] = (re.sub("\n", "", input3[i]))
    i+=1
    
#print(input3[0][0])

gammarate = []
epsilonrate = []
i = 0
x=0
while x <= len(input3[0]):
    onecount = 0
    zerocount = 0 
    while i< len(input3):
        #print(input3[i][x])
        if input3[i][x] == '1':
            onecount += 1
        elif input3[i][x] =='0':
            zerocount +=1
        i+=1
    #print(onecount)
    #print(zerocount)

    if onecount>zerocount :
        gammarate.append(1)
        epsilonrate.append(0)
    else:
        gammarate.append(0)
        epsilonrate.append(1)
    x +=1
print(gammarate)
print(epsilonrate)

gamma = int(''.join(str(i) for i in gammarate))
print(gamma)
epsilon = int(''.join(str(i) for i in epsilonrate))
print(epsilon)
print(gamma*epsilon)


