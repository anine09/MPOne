import time
import os
import re
import sys

NOW_VERSION = "0.0.4"

def fix_version():
    with open("pyproject.toml", "rt") as file:
        x = file.read()
        
    with open("pyproject.toml", "wt") as file:
        pattern = "(?<=(version = \")).*?(?=(\"))"
        version = time.strftime(".dev%Y%m%d%H%M", time.localtime()) 
        x = re.sub(pattern, NOW_VERSION+version, x, count=1)
        file.write(x)


def upload_win():
    print("del old dist")
    os.system("rmdir /q/s dist")
    print("run: python -m build")
    os.system("python -m build")
    print("run: upload to test pypi")
    os.system("twine upload --repository testpypi dist/*")

def upload_linux():
    raise NotImplementedError


if __name__ == "__main__":
    fix_version()
    if sys.platform.startswith("win32"):
        upload_win()
    elif sys.platform.startswith("linux"):
        upload_linux()
    else:
        raise NotImplementedError
