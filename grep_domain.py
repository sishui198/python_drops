import string
import re
import urllib
import sys


class parser:

    def __init__(self, results, word):
        self.results = results
        self.word = word
        self.temp = []

    def genericClean(self):
        self.results = re.sub('<em>', '', self.results)
        self.results = re.sub('<b>', '', self.results)
        self.results = re.sub('</b>', '', self.results)
        self.results = re.sub('</em>', '', self.results)
        #self.results = re.sub('%2f', ' ', self.results)
        #self.results = re.sub('%3a', ' ', self.results)
        self.results = re.sub('<strong>', '', self.results)
        self.results = re.sub('</strong>', '', self.results)
        self.results = re.sub('<wbr>','',self.results)
        self.results = re.sub('</wbr>','',self.results)

        i= 3
        while True:
            self.results = urllib.unquote(self.results)
            if "%25" in self.results and i>0:
                self.results = urllib.unquote(self.results)
                i -= 1
                continue
            else:
                self.results = urllib.unquote(self.results)
                i -= 1
                break


        for e in ('>', ':', '=', '<', '/', '\\', ';', '&', '%3A', '%3D', '%3C'):
            self.results = string.replace(self.results, e, ' ')

    def urlClean(self):
        self.results = re.sub('<em>', '', self.results)
        self.results = re.sub('</em>', '', self.results)
        self.results = re.sub('%2f', ' ', self.results)
        self.results = re.sub('%3a', ' ', self.results)

        for e in ('<', '>', ':', '=', ';', '&', '%3A', '%3D', '%3C'):
            self.results = string.replace(self.results, e, ' ')

    def emails(self):
        self.genericClean()
        reg_emails = re.compile(
            # Local part is required, charset is flexible
           # https://tools.ietf.org/html/rfc6531 (removed * and () as they provide FP mostly )
            '[a-zA-Z0-9.\-_+#~!$&,;=:]+' +
            '@' +
            '[a-zA-Z0-9.-]*' +
            self.word)
        self.temp = reg_emails.findall(self.results)
        emails = self.unique()
        return emails


    def hostnames(self):
        self.genericClean()
        reg_hosts = re.compile('[a-zA-Z0-9]'+'[a-zA-Z0-9.-]*\.' + self.word)
        #reg_hosts = re.compile('[a-zA-Z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}'+self.word)
        self.temp = reg_hosts.findall(self.results)
        hostnames = self.unique()
        return hostnames

    def smilarhostnames(self):
        self.genericClean()
        #reg_hosts = re.compile('[a-zA-Z0-9.-]*\.' + self.word)
        reg_hosts = re.compile('(?i)^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}'+self.word.split('.')[-2])
        self.temp = reg_hosts.findall(self.results)
        smilarhostnames = self.unique()
        return smilarhostnames


    def unique(self):
        self.new = []
        for x in self.temp:
            if x not in self.new:
                self.new.append(x)
        return self.new
if __name__ == "__main__":
    if len(sys.argv) == 3:
        fp =open(sys.argv[1],"r")
        #print fp.readlines()
        parser = parser(str(fp.readlines()),sys.argv[2])
        #parser.smilarhostnames()
        hosts = parser.hostnames()
        for _ in hosts:
            print _

        similarhost = parser.smilarhostnames()
        for _ in similarhost:
            print _
    else:
        print "Usage Example:{0} sourcefile domainname".format(sys.argv[0])

