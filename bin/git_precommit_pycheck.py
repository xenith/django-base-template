#!/usr/bin/env python


# Run this code from project_root/.git/hooks/pre-commit to check your python
# code with pep8 and pyflakes before commiting it to the repository.


import sys
import re
import subprocess

modified = re.compile('modified:\s+(?P<name>.*\.py)')
new = re.compile('new file:\s+(?P<name>.*\.py)')


def main():
    p = subprocess.Popen(['git', 'status'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    modifieds = modified.findall(out.decode())
    news = new.findall(out.decode())

    modifieds += news

    rrcode = 0
    for file in set(modifieds):
        p = subprocess.Popen(['pep8', '--ignore=E501', file],
                             stdout=subprocess.PIPE)
        pep8_out, err = p.communicate()
        p = subprocess.Popen(['pyflakes', file], stdout=subprocess.PIPE)
        pyflakes_out, err = p.communicate()
        if pep8_out or pyflakes_out:
            if pep8_out:
                print(pep8_out.decode())
            if pyflakes_out:
                print(pyflakes_out.decode())
            rrcode = 1

    sys.exit(rrcode)

if __name__ == '__main__':
    main()
