#!/usr/bin/env python2


import os.path
import urllib2
import cookielib

urlopen = urllib2.urlopen
Request = urllib2.Request
cj = cookielib.LWPCookieJar()
LOGINSITE="http://www.portal.fudan.edu.cn"
txheaders =  {'User-agent' : 'Mozilla/5.0 (X11; Linux i686; rv:29.0) Gecko/20100101 Firefox/29.0 Iceweasel/29.0.1'}



opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

theurl = LOGINSITE + '/main/loginIndex.do?ltype=1'
txdata = None
req = Request(theurl, txdata, txheaders)
handle = urlopen(req)


theurl = LOGINSITE + '/main/login.do?invitationCode='
# FIXME fill in email and password
txdata = "email=&password=&btnLogin=" 
req = Request(theurl, txdata, txheaders)
handle = urlopen(req)


theurl = 'http://www.urp.fudan.edu.cn:78/epstar/app/fudan/ScoreManger/ScoreViewer/Student/Course.jsp'
txdata = None
req = Request(theurl, txdata, txheaders)
handle = urlopen(req)

from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):

    output = ''

    def __init__(self):
        HTMLParser.__init__(self)
        self.tcnt = 0
        self.rcnt = 0
        self.now = False

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.tcnt = self.tcnt + 1
        if tag == 'tr':
            if self.tcnt >= 7:
                self.rcnt = self.rcnt + 1
        if tag == 'td':
            if self.rcnt >= 3:
                self.now = True
                

    def handle_endtag(self, tag):
        if tag == 'td':
            self.now = False

    def handle_data(self, data):
        if self.tcnt >= 7:
            if self.rcnt >= 3:
                if self.now:
                    MyHTMLParser.output = MyHTMLParser.output + data


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed(handle.read())

gradings = MyHTMLParser.output.split('\n')



def remove_tr(z):
    r = ''
    for i in z:
        if i != '\t' and i != '\r':
            r = r + i
    return r



gradings = [remove_tr(i) for i in gradings]
gradings = [i for i in gradings if i]

tmp = []
for i in range(0, len(gradings), 7):
    l = []
    for j in range(7):
        l.append(gradings[i + j])
    tmp.append(l)
gradings = tmp

import pickle
pickle.dump(gradings, open('gradings.data', 'wb'))
#gradings = pickle.load(open('gradings.data', 'rb'))


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
