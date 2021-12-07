#TASK 1
import re
with open('input3.txt') as f:
    input3 = f.readlines()
print(input3)
i = 0
while i< len(input3):
    input3[i] = (re.sub("\n", "", input3[i]))
    i+=1
    
print(input3)

gammarate = []
epsilonrate = []
x=0
while x < len(input3[0]):
    i = 0
    onecount = 0
    zerocount = 0 
    while i< len(input3):
        #print(input3[i][x])
        if input3[i][x] == '1':
            onecount += 1
        elif input3[i][x] =='0':
            zerocount +=1
        i+=1
    print(onecount)
    print(zerocount)

    if onecount>zerocount :
        gammarate.append(1)
        epsilonrate.append(0)
        print(gammarate)
        print(epsilonrate)
    else:
        gammarate.append(0)
        epsilonrate.append(1)
        print(gammarate)
        print(epsilonrate)
    x +=1
print(gammarate)
print(epsilonrate)

gamma = int(''.join(str(i) for i in gammarate))
print(gamma)
epsilon = int(''.join(str(i) for i in epsilonrate))
print(epsilon)

bnum1 = gamma
dnum1 = 0
i = 1
while bnum1!=0:
    rem1 = bnum1%10
    dnum1 = dnum1 + (rem1*i)
    i = i*2
    bnum1 = int(bnum1/10)

print("\n First Equivalent Decimal Value = ", dnum1)

bnum2 = epsilon
dnum2 = 0
i = 1
while bnum2!=0:
    rem2 = bnum2%10
    dnum2 = dnum2 + (rem2*i)
    i = i*2
    bnum2 = int(bnum2/10)

print("\n Second Equivalent Decimal Value = ", dnum2)
print("\n Value = ", dnum1*dnum2)

#Task 2
