#!/usr/bin/env python
import os
import re

pkgbuild = "PKGBUILD"

DEPENDENCIES = {"python":"python3","grub":"grub2-common","python-pyqt5":"python3-pyqt5"}
if not os.path.exists(pkgbuild):
    print(f"Error {pkgbuild} wasn't found")
    exit(1)

def get_key(line):
    equal_index = line.find("=")
    return line[:equal_index]

def to_replace():
    with open(pkgbuild) as f:
        for line in f:
            line = line.removesuffix("\n")
            key = get_key(line)
            if key == "depends":
                print(line)
                values = line.removeprefix(key+"=")
                # values = values.removesuffix(")")
                print(values)
                values = values.replace("' '","' , '")
                print(values)
                depends = set(eval(values))
                new_depends = set()
                for dependency in depends:
                    new_depends.add(DEPENDENCIES[dependency])
                print(new_depends)
                new_depends_to_write = str(tuple(new_depends)).replace(",","")
                print(new_depends_to_write)
                return line , "depends="+new_depends_to_write
to_replace_vals = to_replace()
print(to_replace_vals)
def read_data():
    with open(pkgbuild,"r") as f:
        return f.read()
old_data = read_data()
with open(pkgbuild,"w") as f:
    new_data = old_data.replace(*to_replace_vals)
    # print(new_data)
    f.write(new_data)