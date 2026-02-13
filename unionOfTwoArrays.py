def find_union(a, b):
    s = set()
    
    for num in a:
        s.add(num)
        
    for num in b:
        s.add(num)
    
    return list(s)


a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

print(find_union(a, b))
