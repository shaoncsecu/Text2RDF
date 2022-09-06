import re
import urllib.request

PATH = 'http://aclweb.org/anthology/'

def retriever(link, fname):
    urllib.request.urlretrieve(link, fname)
    

def main():
    f = 'ACL.htm'
    with open(f) as fin:
        content = fin.read()
        links = re.findall('a href="([^"]*)"', content, flags=re.U | re.DOTALL)
        links = [l for l in links if l[0].isupper()]
    for l in links:
        req = urllib.request.Request(PATH + l)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            files = re.findall('a href="([^"]*)"', html, flags=re.U | re.DOTALL)
            files = [r for r in files if 'pdf' in r]
            if files is None:
                continue
            for r in files:
                print(PATH + l + r)
                retriever(PATH + l + r, 'corpus/' + r)
        
if __name__ == '__main__':
    main()