t = (1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3, 9)
freq = {}
for i in t:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
max_count = max(freq.values())
ans = []
for i in freq:
    if freq[i] == max_count:
        ans.append(i)
print(max(ans))
