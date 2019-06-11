#!/usr/bin/python2


import pickle
gradings = pickle.load(open('gradings.data', 'rb'))


import sys, getopt
if getopt.getopt(sys.argv[1:], 's')[0]:
    gradings.sort(key=lambda l : l[6] + ',')

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
