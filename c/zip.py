string = list(input())
string.append('\0')
count = 0

if (string[0] == 'w'):  # 最初が白なら、"0"と出力する
    print("0 ", end="")

i = 0  # 配列の場所を示す

judge_str = string[0]  # 一つ前の文字を記憶しておく
while (i < len(string)):
    if (string[i] == judge_str):  # 数え上げの処理
        count += 1
        i += 1
    else :  # 異色やった場合の処理
        print(count, end="")  # ひとかたまりを抜けた一つ目
        count = 0
        judge_str = string[i]  # 記憶する
        if (i + 1 >= len(string)):
            continue
        print(' ', end="")  # 空白を可視化
print()  # 改行
        
    
        
