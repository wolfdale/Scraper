""" PROJECT SCRAPER """		

from bs4 import BeautifulSoup
import urllib2

#url='http://www.indiahabitat.org/programmes' 

url=raw_input()
web=urllib2.urlopen(url)
soup=BeautifulSoup(web,'html.parser',from_encoding='utf-8')


'''***** CONTENT DICTIONARY *****'''
content=[]

for tag in soup.find_all('div',{'class':'eventbody'}):
	content.append(tag.text.encode('utf-8'))	


'''***** DATE DICTIONARY *****'''
date=[]

for tag in soup.find_all('div',{'class':'pull-justify'}):
	date.append(tag.text.encode('utf-8'))	
	


''' **** Multiple DICTIONARY ****'''
multiple=[]

for i in range(0,len(content)):
	result= date[i] +' '+ content[i]
	multiple.append(result)	

print multiple



	

