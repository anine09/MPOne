import datetime
import os
import pytz
import re
import sys

import mpone

NOW_VERSION = mpone.__version__


def fix_version():
    with open("pyproject.toml", "rt") as file:
        pyproject = file.read()

    with open("pyproject.toml", "wt") as file:
        pattern = "(?<=(version = \")).*?(?=(\"))"
        if sys.platform.startswith("win32"):
            pyproject = re.sub(pattern, NOW_VERSION, pyproject, count=1)
            file.write(pyproject)
        elif sys.platform.startswith("linux"):
            version = datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai')).strftime(".dev%Y%m%d%H%M")
            pyproject = re.sub(pattern, NOW_VERSION + version, pyproject, count=1)
            file.write(pyproject)
        else:
            raise NotImplementedError


def upload_win():
    print("del old dist")
    os.system("rmdir /q/s dist")
    print("run: python -m build")
    os.system("python -m build")
    print("run: upload to pypi")
    # os.system("twine upload --repository pypi dist/*")


def upload_linux():
    print("run: python -m build")
    os.system("python -m build")


if __name__ == "__main__":
    fix_version()
    if sys.platform.startswith("win32"):
        upload_win()
    elif sys.platform.startswith("linux"):
        upload_linux()
    else:
        raise NotImplementedError
