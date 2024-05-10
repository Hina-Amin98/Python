def greaternumber():
    greaternum = [10, 40, 30]
    if(greaternum[0] >= greaternum[1]):
     return(greaternum[0])
    if(greaternum[1] >= greaternum[2]):
     return(greaternum[1])
    else:
     return(greaternum[2])
print(greaternumber())    