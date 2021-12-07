#TASK 1
import re
with open('input 4.1.txt') as f:
    input4_1 = f.readlines()

print(input4_1)

input4_2 = []
with open('input 4.2.txt') as f:
    input4_2 = f.readlines()
    

input4_2 = list(map(lambda x:x.strip(),input4_2))

print(input4_2)

i = 0
while i< len(input4_2):
    if input4_2[i] == '':
        del input4_2 [i]

    i+=1
   
#print(input4_2)


input4_2_1 = [input4_2[x:x+4] for x in range(0, len(input4_2), 4)]
print(input4_2_1)

i = 0
while i< len(input4_2_1[0]):
    input4_2_1[i].replace(' ',',')

    i+=1

print(input4_2_1)
    