import tarfile
import os
import sys

pathname = sys.argv[1]
outpath = sys.argv[2]
extensions = sys.argv[3].split(",")

size = 0

tf = tarfile.open(outpath, "w:bz2")
for root, dirs, files in os.walk(pathname):
    for f in files:
        filepath = os.path.join(root, f)
        if os.path.splitext(filepath)[1][1:] in extensions:
            if "extrathumbs" not in root:
                print filepath
                size += os.path.getsize(filepath)
                tf.add(filepath)

tf.close()
print "size: %s" % (str(size))