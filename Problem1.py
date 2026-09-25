n = int(input())

intervals = []

for i in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

intervals.sort()

result = []

for start, end in intervals:
    if not result or start > result[-1][1]:
        result.append([start, end])
    else:
        result[-1][1] = max(result[-1][1], end)

for start, end in result:
    print(start, end)
	
--Input--
4
1 3
8 10
15 18
--Ouput--
1 6
8 10
15 18
Logic: Sort the ranges by starting time, then merge a range with the previous one whenever they overlap.