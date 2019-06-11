#!/usr/bin/env python2
# coding: utf-8

# 要求：43 + 28 + 61 + 12 = 144, + 2 tests

# 43 = 14 pol + 14 7mo +
#       8 eng + 2 comp + 4 pe + 1 mil

# 28 = 10 ma + 5 lin. alg + 3 ag + 10 phys

# 61 = 53 + 8

import pickle
courses = pickle.load(open('gradings.data', 'rb'))

for l in courses:
    l = [i.decode('utf-8') for i in l]
for l in courses:
    l.pop()
    l.pop(0)
    l.pop(0)
    l.pop(0)


def find(s):
    l = []
    L = len(s)
    for i in range(len(courses)):
        #x = L
        #if len(courses[i][0]) < x:
            #x = len(courses[i][0])
        if courses[i][0][:L] == s:
            l.append(i)
    ll = []
    for i in range(len(l)):
        ll.append(courses.pop(l[len(l) - i - 1]))
    ll.sort()
    return ll

def out(a, n=0):
    print(" " * n + a)
def output(s):
    for l in s:
        print ' ' * 8,
        for i in l:
            print i,
        print

out("FCT + FET(6)")
output(find('COMP110901'))
output(find('ENGL110901'))



total = 0
for l in courses:
    total += float(l[2])

out("已修课程(%s/144)：" % total)

out("没有意义(43)", 2)
out("政治(14)", 4)
output(find('PTSS'))
out("7Mo(14)", 4)
output(find('CHIN'))
output(find('PHIL'))
output(find('LAWS'))
output(find('INFO'))
output(find('FINE'))
output(find('COMP110016'))
out("军理(1)", 4)
output(find('NDEC'))
out("计算机(2)", 4)
output(find('COMP110035'))
out("体育(4)", 4)
output(find('PEDU'))
out("英语(8)", 4)
output(find('ENGL'))
output(find('FORE'))

out("大物(10)", 2)
output(find('PHYS'))
out("数学(79)", 2)
output(find('COMP12'))
output(find('MATH'))
out("任意(12)", 2)
output(find(''))

print("还差课程")
print("还差学分 = %s" % (144-total+3))
