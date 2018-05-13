def key_func(n):
    return int(n)

def convert_str(n):
    return str(n)

l=[2,3,4,'111']
print(min(l, key=key_func))
print(max(l, key=key_func))
print(min(l, key=convert_str))
print(max(l, key=convert_str))
