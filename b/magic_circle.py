N = int(input())  # 何次元配列(lsit)
ary_lst = []
for _ in range(N):
    a_list = list(map(int, input().split()))
    ary_lst.append(a_list)

# 縦横斜めで最大となる値が指標(今回横で見る)
goal = 0
total = 0
target = []  # 0がある位置
for i in range(N):  # 横
    total = sum(ary_lst[i])
    if (goal < total):
        goal = total
    for j in range(N):  # 縦
        if (ary_lst[i][j] == 0):
            target.append((i, j))

if (target[0][1] == target[1][1]):  # 縦に0が並んでいる状態
    for k in range(2):
        (i, j) = target[k]
        ary_lst[i][j] = goal - sum(ary_lst[i])
else :
    for k in range(2):
        (i, j) = target[k]
        total = 0
        for l in range(N):
            total += ary_lst[l][j]
        ary_lst[i][j] = goal - total

# 出力
for i in range(N):
    for j in range(N):
        if (j == N -1):
            print(ary_lst[i][j])
        else :
            print(ary_lst[i][j], end=" ")

