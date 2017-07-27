#!/usr/bin/python3
from bs4 import BeautifulSoup
import urllib.request
import time
import datetime
from tqdm import tqdm
from urllib.request import URLError
def site_test():
    f = open("log.txt","a")
    url =[]
    def bar():
        for k in tqdm(range(100)):
            time.sleep(0.009)
    for i in range(3):
        url.append( input("enter the url,in  format:\n").lower())
    bar()
    while True:
     for i in range(3):
        url[i] =url[i].replace('https://','http://')
        if ("http://") not in url[i]:

            url[i] = "http://"+url[i]
        
        try:
            d = datetime.datetime.now().isoformat()
            page = urllib.request.urlopen(url[i], timeout=7)
            soup= BeautifulSoup(page,'lxml')
            f.write("\n%s -- %s -- site working\n"%(d,url[i]))
            print("%s ---site working"%(url[i]))
        
        except Exception as ex :
            print(ex)
            print("%s --"%(url[i]))
            
            f.write("%s --%s--%s \n" %(d, url[i],str(ex)))
     time.sleep(5)      
            
    f.close()
if __name__ == "__main__":
        site_test()
