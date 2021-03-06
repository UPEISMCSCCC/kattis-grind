#!/usr/bin/env python3
import os
import sys
import shutil
import pathlib
import requests
import argparse

ISON_WINDOWS = sys.platform == 'win32'
EXE_NAME = 'a' if ISON_WINDOWS else './a.out'
WRITER_NAME = 'type' if ISON_WINDOWS else 'cat'
parser = argparse.ArgumentParser(description='Runs Kattis problem through their test cases')
parser.add_argument('--id', type=str, default='_NONE_', help='id of problem to fetch')
args = parser.parse_args()
qid = args.id

if qid == '_NONE_':
    qid = input('Enter ID: ')
qdir = os.path.join(os.getcwd(),qid)

qext = 'z'
while qext != 'c' and qext != 'p':
    qext = input('Which language (py/cpp): ')
    qext = qext[:1].lower()

if qext == 'p':
    EXE_NAME = '%s/_%s.py'%(qdir,qid)

isinfile_inqdir = lambda name: name.startswith("input") and os.path.isfile(os.path.join(qdir,name))
input_files = list(filter(isinfile_inqdir, os.listdir(qdir)))
ilen = len(input_files)

os.system('g++ \"' + qdir + '/_' + qid + '.cpp\"')

for i in range(ilen):
    print('TEST CASE ' + str(i+1))
    output = os.popen('%s \"'%WRITER_NAME + os.path.join(qdir,'input' + str(i+1)) + '\" | %s'%EXE_NAME).read().rstrip()
    print('OUTPUT:')
    print(output)
    with open(qdir + '/output' + str(i+1)) as expected:
        content = expected.read().rstrip()
        print('EXPECTED OUTPUT:')
        print(content)
        if content==output:
            print('PASSED')
        else:
            print('FAILED')