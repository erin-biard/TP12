def listSum(L):
    if len(L) == 0:
        return 0
    else:
        return listSum(L[1:])+L[0]


print(listSum([])) # 0
print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11
