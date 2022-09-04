##from selenium import webdriver
##from selenium.webdriver.common.by import By
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
 
s = Service(r"C:\python\Scripts\msedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.get('http://jwc.cpu.edu.cn/851/list.htm')
n=5
##driver = webdriver.Edge("C:\Python\MicrosoftWebDriver.exe")
##driver.get('http://jwc.cpu.edu.cn/851/list.htm')
driver.implicitly_wait(10)
txt=driver.page_source
driver.quit()
##li=txt.split('target="_blank"')
li=re.split('target="_blank"|</a></span><span ',txt)
l0=[i for i in li if 'title="' in i]
l1=[re.split('title="|">',k)[1] for k in l0]
    
l2=[j[17:29] for j in li if 'class="news_meta">'in j]
r_l=list(zip(l1,l2))
re_l=['\n\t'.join(i[::-1]) for i in r_l]
print('\n'.join(re_l[:n]))

##l1=[i[6:-16] for i in li if 'title="' in i]
##for x in range(len(l1)):
##    l_x=len(l1[x])
##    l1[x]=l1[x][1:l_x//2]
##l2=[j[17:-6] for j in li if 'class="news_meta">'in j]
##r_l=list(zip(l1,l2))
##re_l=['\n\t'.join(i[::-1]) for i in r_l]
##print('\n'.join(re_l[:n]))

while 0<n<=14:
    n=int(input())
    if 0<n<=14:
        print('\n'.join(re_l[:n]))
