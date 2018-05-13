import os
import os.path as p

print(os.sep)
print(os.pathsep)
print(os.extsep)

print(p.splitext('splitext.py'))

test_str = 'kerneltyu.com'

#改行コード os.linesepの取得
print(test_str.replace('.', os.linesep))

for env in os.environ:
    print(env)

print('----------------------------------')
print(os.environ.get('NODE_PATH'))
