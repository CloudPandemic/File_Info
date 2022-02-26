import chardet
import sys

val = sys.argv

if len(val) > 1 :
    for arg in val:
        if arg != "encoding.py":
            print(arg)
            with open(arg,'rb') as f:
                print(chardet.detect( f.read() ) )
else:
    print("引数が未設定")
