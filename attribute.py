class AttrTest():
    def __init__(self):
        self.code = -1

attr_test = AttrTest()
attr_test.name = 'python-izm'

print(hasattr(attr_test, 'code'))
print(hasattr(attr_test, 'name'))
print(hasattr(attr_test, 'x'))

print(getattr(attr_test, 'code'))
print(getattr(attr_test, 'name'))
print(getattr(attr_test, 'x', 'No Attr'))

#AttributeError
print(getattr(attr_test, 'x'))
