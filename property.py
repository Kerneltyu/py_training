class PropertyTest(object):
    def __init__(self, url):
        self._url = url
    def get_url(self):
        print('--get_url--')
        return self._url

    def set_url(self,url):
        print('--set_url--')
        self._url = url

    def del_url(self, url):
        print('--del_url--')
        del self._url
    url = property(get_url, set_url, del_url)

class PropertyDecorator(object):
    def __init__(self,url):
        self._url = url

    @property
    def url(self):
        print('--get_url--')
        return self._url

    @url.setter
    def url(self, url):
        print('--set_url--')
        self._url = url

    @url.deleter
    def url(self):
        del self._url

prop = PropertyTest('https://www.python-izm.com/')
prop.url = 'python_izm'
print(prop.url)

prop_dec = PropertyDecorator('https://www.python-izm.com/')
prop.url = 'python_izm'
print(prop_dec.url)
