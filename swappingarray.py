swappingnum = [10, 20, 0]
print ("values before swapping")
print(swappingnum[0])
print(swappingnum[1])

swappingnum[2] = swappingnum[0]
swappingnum[0] = swappingnum[1]
swappingnum[1] = swappingnum[2]

print ("values after swapping")
print(swappingnum[0])
print(swappingnum[1])