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
    print("No argument is set, so no information can be retrieved. You need to specify the file you want to look up as an argument.")
