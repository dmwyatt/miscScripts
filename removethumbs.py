import os
import shutil
import sys

pathname = sys.argv[1]


count = 0
for root, dirs, files in os.walk(pathname):
    for f in files:
        filepath = os.path.join(root, f)
        if f.lower() == "thumbs.db":
            print filepath
            os.remove(filepath)
            count += 1

print count