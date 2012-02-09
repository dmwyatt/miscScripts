import re
import os
import sys


def get_id(nfo):
    #movie: <id>tt1022603</id>
    #tv: <id>73244</id>
    f = open(nfo, "r")
    contents = f.read()
    f.close()
    movie = re.compile("<id>(tt\d+)</id")
    show = re.compile("<id>(\d+)</id")

    try:
        i = movie.search(contents).groups()[0]
        return i
    except AttributeError:
        pass

    try:
        i = show.search(contents).groups()[0]
        return i
    except AttributeError:
        pass

    return ""


pathname = sys.argv[1]
print pathname
raw_input()


movies = {}
for root, dirs, files in os.walk(pathname):
    for f in files:
        filepath = os.path.join(root, f)

        if os.path.splitext(filepath)[1] == ".nfo":
            i = get_id(filepath)
            if i <> "":
                movies[i] = ""
                print i

print len(movies)