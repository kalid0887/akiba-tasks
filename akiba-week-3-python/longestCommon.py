strs = []

bzat = int(input("how many words do u want to input in to the list: "))
for i in range(bzat):
    word = input(f"enter the index {i} word ")
    strs.append(word)
print(strs)

for wor in strs:
    for i in range(len(strs[0])):
        if strs[wor][i] == strs[wor + 1][i] == strs[wor + 2][i]:
            print(strs)