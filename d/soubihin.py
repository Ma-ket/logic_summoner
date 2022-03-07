(a, b) = tuple(map(int, input().split()))
(c, d) = tuple(map(int, input().split()))

a_b = a / b
c_d = c / d

if (a_b > c_d):
    print(b)
else :
    print(d)
