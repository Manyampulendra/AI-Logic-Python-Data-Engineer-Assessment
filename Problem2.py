from collections import deque

n = int(input())
arr = list(map(int, input().split()))
k = int(input())

min_deque = deque()
max_deque = deque()

left = 0
max_length = 0
start_position = 1

for right in range(n):

    while min_deque and arr[min_deque[-1]] > arr[right]:
        min_deque.pop()
    min_deque.append(right)

    while max_deque and arr[max_deque[-1]] < arr[right]:
        max_deque.pop()
    max_deque.append(right)

    while arr[max_deque[0]] - arr[min_deque[0]] > k:
        if min_deque[0] == left:
            min_deque.popleft()

        if max_deque[0] == left:
            max_deque.popleft()

        left += 1

    length = right - left + 1

    if length > max_length:
        max_length = length
        start_position = left + 1

print(max_length, start_position)
==============================================
--Input--
8
4 2 2 3 1 5 4 2
2
===============================================
--Output--
4 1