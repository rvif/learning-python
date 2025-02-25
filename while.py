i = 10
while i > 0:
    print(i)
    i -= 1
    
    
# implementing the same dictionary loop using while loop
d = {'a': 1, 'b': 2, 'c': 3}
keys = list(d.keys())
i = 0
while i < len(keys):
    key = keys[i]
    value = d[key]
    print(f"key: {key}, value: {value}")
    i += 1
