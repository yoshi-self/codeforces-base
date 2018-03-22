#!/usr/bin/env python

import sys
import os
import re
import subprocess

class CodeforcesTest():
    def __init__(self):
        pass

    def run(self):
        f = open('test.txt')
        test_content = f.read()
        flags = (re.MULTILINE | re.DOTALL)
        r = re.compile(r'<input>\n(.*?)</input>.*?<output>\n(.*?)</output>', flags);
        match_iter = r.finditer(test_content)
        i = 1
        for match in match_iter:
            test_input = match.group(1)
            test_answer = match.group(2)
            print('##### Test %d #####' % (i))
            p = subprocess.run(['./a.out'], input=test_input, stdout=subprocess.PIPE, encoding='utf_8')
            test_output = p.stdout
            if test_answer == '<nooutput />\n':
                print('Answer not specified')
                print('-- input --\n%s' % (test_input), end='')
                print('-- your output --\n%s' % test_output, end='')
            elif test_answer == test_output:
                print('Test succeeded')
            else:
                print('Test failed')
                print('-- input --\n%s' % (test_input), end='')
                print('-- expected output --\n%s' % (test_answer), end='')
                print('-- your output --\n%s' % test_output, end='')
            i += 1
            
    def build(self):
        command = '../g++cf'
        dirname = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
        filename = dirname + ".cpp"
        print('##### Compiling %s #####' % (filename))
        subprocess.run([command, filename])

if __name__ == '__main__':
    build_flag = False
    if len(sys.argv) > 1 and sys.argv[1] == '-b':
        build_flag = True;

    try:
        cftest = CodeforcesTest()
        if build_flag:
            cftest.build()
        print('')
        cftest.run()
    except Exception as e:
        raise
