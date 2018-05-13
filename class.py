import datetime
class TestClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sample_instancemethod(self, display_x= True, display_y=True):
        if display_x:
            print('x is {}'.format(self.x))
        if display_y:
            print('y is {}'.format(self.y))

    @classmethod
    def sample_classmethod(cls, date_diff):
        today = datetime.date.today()
        d = today + datetime.timedelta(days=date_diff)
        return cls(d.month, d.day)

    @staticmethod
    def sample_staticmethod(x, y):
        #self, cls引数がいらない
        print( x + y )

if __name__=='__main__':
    testClass = TestClass(100, 50)
    testClass.sample_instancemethod(display_x=False)
    testClass.sample_instancemethod(display_y=False)
    testClass.sample_instancemethod(False, False)
    #インスタンス化しなくてよい
    testClass = TestClass.sample_classmethod(1)
    testClass.sample_instancemethod(display_y=False)
    testClass.sample_instancemethod(display_x=False)
    testClass.sample_instancemethod(False, False)

    #インスタンス化しなくて良い
    TestClass.sample_staticmethod(1,2)
