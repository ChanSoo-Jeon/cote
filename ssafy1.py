


n,k = map(int,input().split())

a = list(map(int,input().split()))



b = sorted(a)
result = b
ecept = []
bec = result[1]

for i in range(1,n+1):  #1 2 3 4
    origin = b[i-1]

    for j in range(1,n): # 1 2 3
        if b[i-1] - b[j] < -k:

            ecept.append(b[j])
        else:
            continue


for i in result:
    if i in ecept:
        if i == bec:
            result = [b[0]]
            break
        else:
            result.remove(i)

print(len(result))




