import os
filepath = '/Users/kerneltyu/code/Pyworks/training'

if os.path.exists(filepath):
    print('指定のファイル，またはディレクトリが存在しています。')

    if os.path.isfile(filepath):
        print('指定のパスはファイルです')
    if os.path.isdir(filepath):
        print('指定のパスはディレクトリです')
else:
    print('指定のファイル，またはディレクトリが存在しいていません．')
