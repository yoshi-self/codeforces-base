#!/usr/bin/env python

import sys
import os
import re
import shutil
from urllib.request import urlopen

class Example():
    def __init__(self, input, output):
        self.input = input
        self.output = output

class App():
    NAME = 'cfprepare'
    
    def __init__(self, problem):
        self.problem = problem
        self.examples = []

    def run(self):
        if not self.problem.startswith('http'):
            # when problem id specified
            self.problem_id = self.problem
            # make url from problem id
            match = re.match('^([0-9]+)([^0-9]+.*)$', self.problem)
            if(match == None or match.lastindex < 2):
                raise Exception('Invalid problem id')
            contest_id = match.group(1)
            problem_index = match.group(2)
            url = 'http://codeforces.com/problemset/problem/%s/%s' % (contest_id, problem_index)
        else:
            # when problem URL specified
            url = self.problem
            match = re.search(r'/([^/]+?)/([^/])+?/?$', url)
            self.problem_id = match.group(1) + match.group(2)

        print('Start preparing for codeforce problem %s' % self.problem_id)
        print('Get problem from URL: %s' % (url))
        f = urlopen(url) 
        # NOTE: getcode() returns int
        if(f.getcode() != 200):
            raise Exception("URL not found")
        content = f.read()
        content = content.decode(f.info().get_content_charset())
        r = re.compile('<div class="input">.*?<pre.*?>(.*?)</pre>.*?<div class="output">.*?<pre.*?>(.*?)</pre>')
        match_iter = r.finditer(content, re.MULTILINE)
        for match in match_iter:
            if match.lastindex < 2:
                raise Exception("Failed to parse examples")
            example_input =  re.sub('<br.*?>', '\n', match.group(1), re.MULTILINE)
            example_output =  re.sub('<br.*?>', '\n', match.group(2), re.MULTILINE)
            self.examples.append(Example(example_input, example_output))

        if not os.path.exists(self.problem_id):
            os.mkdir(self.problem_id)
        self.write_example_file()
        self.copy_files()

    def write_example_file(self):
        file_path = os.path.join(self.problem_id, 'test.txt')
        f = open(file_path, 'w')
        for example in self.examples:
            write_str = '''
<input>
%s</input>
<output>
%s</output>
''' % (example.input, example.output)
            f.write(write_str[1:])

    def copy_files(self):
        shutil.copy('cftest.py', self.problem_id)
        shutil.copy('build', self.problem_id)
        shutil.copy('main.cpp', os.path.join(self.problem_id, self.problem_id + '.cpp'))

    @staticmethod
    def get_usage():
        usage = '''
Usage: %s <problem>

    problem: <contest_id + index> or <URL of the problem>

Examples:

    %s 950A
    %s http://codeforces.com/problemset/problem/950/A

''' % (App.NAME, App.NAME, App.NAME)
        return usage[1:-1]

    @staticmethod
    def print_usage():
        print(App.get_usage())

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('ERROR: You must specify a problem number')
        print('')
        App.print_usage()

        sys.exit(1);

    try:
        app = App(sys.argv[1])
        app.run()
    except Exception as e:
        App.print_usage()
        raise
