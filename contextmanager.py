from contextlib import contextmanager
@contextmanager
def context_manager_test():
    print('enter')
    yield
    print('exit')

class ContextManagerTest:
    def __enter__(self):
        print('__enter__')
        return 'as obj'
    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__')
        print(exc_type)
        print(exc_value)
        print(traceback)
        return True

with ContextManagerTest() as as_obj:
    print(as_obj)

with context_manager_test():
    print('with')
