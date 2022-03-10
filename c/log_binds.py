# 入力
n = int(input())
input_dic = {}
for _ in range(n):
    (id, string) = input().split()
    id = int(id)
    if (id in input_dic):
        input_dic[id] += string  # 文字列の連結
    else :
        input_dic.update({id : string})

# 出力
for id in input_dic:
    print(id, input_dic[id])

