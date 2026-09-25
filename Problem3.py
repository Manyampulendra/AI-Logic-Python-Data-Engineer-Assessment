n = int(input())
list1 = list(map(int, input().split()))

m = int(input())
list2 = list(map(int, input().split()))

result = []
carry = 0
i = 0

while i < n or i < m or carry:
    digit1 = list1[i] if i < n else 0
    digit2 = list2[i] if i < m else 0

    total = digit1 + digit2 + carry
    result.append(total % 10)
    carry = total // 10

    i += 1

print(*result)
=================================================
--Input-1--
3
2 4 3
3
5 6 4
--Output--
7 0 8
==================================================
--Input2--
1
0
1
0
--Ouput--
0
===================================================
--Input3--
7
9 9 9 9 9 9 9
4
9 9 9 9
--Output--
8 9 9 9 0 0 0 1