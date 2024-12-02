

list_a = []
list_b = []

with open('1/data.txt', 'r') as data_file:
    for line in data_file:
        list_a.append(int(line.split()[0]))
        list_b.append(int(line.split()[1]))

list_a.sort()
list_b.sort()

dist = 0
for a, b in zip(list_a, list_b):
    dist += abs(a-b)

print(dist)

similarity = 0
for id in list_a:
    count = list_b.count(id)
    similarity += id * count

print(similarity)