N = int(input())
way = input()

a_list = []

i = 1
for LR in way:
    if (LR == 'R'):
        a_list.append(i)
    else :
        a_list = [i, *a_list]
    i += 1

for i in range(N):
    print(a_list[i], end="")
    if (i + 1 == N):
        print()
        break
    print(' ', end="")
    
