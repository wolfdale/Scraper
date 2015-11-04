""" PROJECT SCRAPER """
'''GET URL FROM BBC NEWS'''

from bs4 import BeautifulSoup
import urllib2

url='http://www.bbc.com/news'

web=urllib2.urlopen(url)
soup=BeautifulSoup(web,'html.parser')


with open('news_url.txt','w') as file:
	for tag in soup.find_all('a',{'class':'title-link'}):
		url=tag.get('href')
		file.write(tag.text.encode('utf-8'))
		file.write('www.bbc.com'+url + '\n')
		

