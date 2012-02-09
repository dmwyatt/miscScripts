import os
import shutil
import sys

pathname = sys.argv[1]
extensions = sys.argv[2].split(",")

for root, dirs, files in os.walk(pathname):
    for f in files:
        filepath = os.path.join(root, f)
        if os.path.splitext(filepath)[1][1:] in extensions:
            print filepath
            os.remove(filepath)
