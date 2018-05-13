# _*_ coding: utf-8 _*_
def test_func(*args):
    print(args)

def _test_func(**args):
    print(args)

class TestClass:
    def __init__(self, code, name):
        self.code = code
        self.name = name

class Inheritance(TestClass):
    def __init__(self, code, name, tall):
        super().__init__(code, name)
        self.tall = tall


if __name__ == "__main__":
    test_func(1,1,2,3,5)
    _test_func(i=1,j=1,k=2,x=3,y=5)
    classes = []
    classes.append(Inheritance(1, "テスト１", 145))
    classes.append(Inheritance(2, "テスト２", 150))
    for i in classes:
        print('code-->'+str(i.code))
        print('name-->'+i.name)
