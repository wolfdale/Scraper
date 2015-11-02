""" PROJECT SCRAPER """


from bs4 import BeautifulSoup
import urllib2

url='http://www.reuters.com/article/2014/03/06/us-syria-crisis-assad-insight-idUSBREA250SD20140306 '

web=urllib2.urlopen(url)
soup=BeautifulSoup(web,'html.parser')



'''GET ALL CONTENT IN <P> TAG'''

with open('output.txt','w') as file:
	for tag in soup.find_all('p'):
		file.write(tag.text.encode('utf-8')+ "\n")





'''GET ALL HYPER LINK IN <A> TAG '''

with open('hyperlink.txt','w') as file:
	for tag in soup.find_all('a'):
		file.write(tag.encode('utf-8')+ '\n')




