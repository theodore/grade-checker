#!/usr/bin/python2


import pickle
gradings = pickle.load(open('gradings.data', 'rb'))


import sys, getopt
PROFESSION = 'MATH'
for opt in getopt.getopt(sys.argv[1:], 'sc')[0]:
    if '-s' in opt:
        gradings.sort(key=lambda l : l[6] + ',')
    if '-c' in opt:
        PROFESSION = 'CHIN'

def output(gradings):
    def calc_width(s):
        # ul = cn + en, l = cn * 3 + en
        ul = len(s)
        l = len(s.encode('utf-8'))
        # fix the strange character
        fix = 0
        if s[-1] == u'\u2160':
            fix = 1
        return 50 - (l - ul) / 2 + fix

    template = u'{0:3} {2:14} {4:.<{WIDTH}} {5:4} {6}'
    for l in gradings:
        l = [i.decode('utf-8') for i in l]
        print template.format(*l, WIDTH=calc_width(l[4]))

output(gradings)

def calc_gpa(gradings):
    num = 0
    den = 0
    TOGPA={'A': 4, 'A-': 3.7, 'B+': 3.3, 'B': 3, 'B-': 2.7, 'C+': 2.3,
           'C': 2, 'C-': 1.7, 'D': 1.3, 'D-': 1, 'F': 0}
    for l in gradings:
        s = TOGPA.get(l[6])
        if s:
            num += float(l[5]) * s
            den += float(l[5])
    return num / den

print 'GPA =', calc_gpa(gradings)

professional = [l for l in gradings if l[2][:4] == PROFESSION]
output(professional)
print 'professional GPA =', calc_gpa(professional)
