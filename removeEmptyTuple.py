data = [(), (1,), [], 'abc', (), (), (1,), ('a',), ('a', 'b'), ((),), '']
result = []
for i in data:
    if i != () and i != [] and i != '':
        result.append(i)
print(result)
