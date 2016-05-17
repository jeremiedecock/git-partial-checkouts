#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Jérémie DECOCK (http://www.jdhp.org)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
This module copy the commits form one git repository to another one.
"""

import sys, os

def main():
    GIT_LOG_FILE = "/tmp/git_log.tmp"
    SRC_REPOSITORY = "~/git/pub/demos/cpp/bullet_osg/BULLET_OSG_FRAMEWORK"
    #DST_REPOSITORY = "~/sandbox/git/botsim"
    DST_REPOSITORY = "~/git/pub/botsim"

    #os.chdir(SRC_REPOSITORY)
    #cmd = 'git checkout master'
    #os.system(cmd)
    #cmd = 'git log --pretty=oneline . > "' + GIT_LOG_FILE + '"'
    #os.system(cmd)

    commit_list = []

    with open(GIT_LOG_FILE, "rU") as fd:
        for line in fd.readlines():
            sha = line.split()[0]
            message = " ".join(line.split()[1:])
            #print(sha, message)
            commit_list.append([sha, message])

    if len(commit_list) == 0:
        sys.exit(1)

    commit_list.reverse()

    for commit in commit_list:
        sha = commit[0]
        message = commit[1]
        print()
        print("* ", sha, message)

        os.chdir(SRC_REPOSITORY)
        cmd = 'git checkout -f ' + sha
        print(cmd)
        os.system(cmd)

        cmd = 'git clean -d -f'
        print(cmd)
        os.system(cmd)

        cmd = 'mv "' + DST_REPOSITORY + '/.git" /tmp/mlkjmkjmk.git'
        print(cmd)
        os.system(cmd)
        cmd = 'rm -rf "' + DST_REPOSITORY + '"/*'
        print(cmd)
        os.system(cmd)
        cmd = 'mv /tmp/mlkjmkjmk.git "' + DST_REPOSITORY + '/.git"'
        print(cmd)
        os.system(cmd)
        cmd = 'cp -a "' + SRC_REPOSITORY + '"/* "' + DST_REPOSITORY + '/"'
        print(cmd)
        os.system(cmd)

        os.chdir(DST_REPOSITORY)
        cmd = 'git add .'
        print(cmd)
        os.system(cmd)
        cmd = 'git commit -m "' + message + '"'
        print(cmd)
        os.system(cmd)

if __name__ == '__main__':
    main()
