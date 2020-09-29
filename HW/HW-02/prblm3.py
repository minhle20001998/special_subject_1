lis = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
res = []
arr = [x.lower() for x in input().split('-')]
for part in arr:
    replace = ''
    for i in range(len(part)):
        if part[i].isalpha():
            for ind in range(len(lis)):
                if part[i] in lis[ind]:
                    replace += str(ind + 2)
        else:
            replace += part[i]
    res.append(replace)
print("-".join(res))

            