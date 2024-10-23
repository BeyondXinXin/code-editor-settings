import os
import os.path
import sys

ignore_paths = ["./libs"]

path = ""
if len(sys.argv) >= 2:
    path = sys.argv[1]
if path == "":
    path = sys.path[0]

print("Target Directory:%s" % (path))

for root, dirs, files in os.walk(path):
    if any(os.path.commonpath([root, os.path.abspath(ignore_path)]) == os.path.abspath(ignore_path) for ignore_path in ignore_paths):
        continue
    
    for name in files:
        if name.endswith(".h") or name.endswith(".cpp"):
            localpath = os.path.join(root, name)
            print(localpath)
            os.system("clang-format -i %s -style=File" % (localpath))

print("Format Finish")