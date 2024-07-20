import random

first_number = random.randint(3, 20)
print(first_number)

lst1 = []
number_pair = []
for i in range((first_number) + 1):
    if i == 0:
        continue
    lst1.append(i)

print(lst1)

for j in lst1:
    for k in lst1:
        sum = j + k
        if first_number % sum == 0 and j < k:
            number_pair.append(j)
            number_pair.append(k)

print(number_pair)
