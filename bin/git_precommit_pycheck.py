#!/usr/bin/env python


# Run this code from project_root/.git/hooks/pre-commit to check your python
# code with pep8 and pyflakes before commiting it to the repository.


import sys
import re
import subprocess, commands

modified = re.compile('modified:\s+(?P<name>.*\.py)')
new = re.compile('new file:\s+(?P<name>.*\.py)')


def main():
    p = subprocess.Popen(['git', 'status'], stdout=subprocess.PIPE)
    out, err = p.communicate()
    modifieds = modified.findall(out)
    news = new.findall(out)

    modifieds += news

    rrcode = 0
    for file in set(modifieds):
        pep8_out = commands.getoutput('pep8 --ignore=E501 %s' % file)
        pyflakes_out = commands.getoutput('pyflakes %s' % file)
        if pep8_out or pyflakes_out:
            if pep8_out:
                print pep8_out
            if pyflakes_out:
                print pyflakes_out
            rrcode = 1

    sys.exit(rrcode)

if __name__ == '__main__':
    main()
