# 入力
[n, m, a, b] = list(map(int, input().split()))
damege_list = list(map(int, input().split()))

# 処理
life = m
for damage in damege_list:
    life += damage
    if (life < 0):
        life = 0
        break
    if (damage < 0 and life <= a):
        life += b

# 出力
print(life)
