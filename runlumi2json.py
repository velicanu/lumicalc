#!/usr/bin/env python

import sys, itertools

def ranges(i):
    for a, b in itertools.groupby(enumerate(i), lambda (x, y): y - x):
        b = list(b)
        yield [b[0][1], b[-1][1]]

f = open(sys.argv[1], 'r')
lumi_max = 0
line = f.readline()
run_lumi = {}
while line != '':
    run, lumi = map(int, line.split(' '))
    # print "%s %s" % (run,lumi)
    if not run_lumi.has_key(run):
        run_lumi[run] = {}
    if not run_lumi[run].has_key(lumi):
        run_lumi[run][lumi] = True
    lumi_max = max(lumi_max, lumi)
    line = f.readline()
f.close()
print '{'
run_list = sorted(run_lumi.keys())
for i in range(len(run_list)):
    run = run_list[i]
    if i == len(run_list) - 1:
        separator = ''
    else:
        separator = ','
    print '"%d": %s%s' % (
        run, str(list(ranges(sorted(run_lumi[run].keys())))),
        separator)
print '}'

