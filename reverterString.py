stringInput = input()
emptyStr = ''
for x in range(len(stringInput)-1,-1,-1):
    emptyStr += stringInput[x]

print(emptyStr)
