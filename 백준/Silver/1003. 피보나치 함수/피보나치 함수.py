T = int(input())

n = [0]*T

for i in range(T):
    n[i] = int(input())

max_number = max(n)

zero = [0] * 41
one = [0] * 41

zero[0] = 1
one[1] = 1

for i in range(2, max_number + 1):
    one[i] = one[i - 1] + one[i - 2]
    zero[i] = zero[i - 1] + zero[i - 2]

for i in range(T):
    print(zero[n[i]], one[n[i]])