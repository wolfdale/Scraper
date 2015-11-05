""" PROJECT SCRAPER """		

from bs4 import BeautifulSoup
import urllib2

def scrape_img( url, tag_name, attr, attr_name ):

	''' BEAUTIFUL SOUP INIT '''
	
	web=urllib2.urlopen(url)
	soup=BeautifulSoup(web,'html.parser',from_encoding='utf-8')
	

	''' CONTENT LIST '''
	content=[]
	for link in soup.find_all(tag_name):
            all_links = link.get('src')
            content.append(all_links)
	print content

	#content.append(soup.find_all('img'))
	#print content
	#for img_tag in soup.find_all(tag_name , src = True ):
	#	content.append(tag_name['scr'])
	'''
	if cls_name != 'null':
		for tag in soup.find_all(tag_name, attrs={'class':cls_name}):
			content.append(tag.text.encode('utf-8'))	
	elif tag_id != 'null':
		for tag in soup.find_all(tag_name, attrs={'id':tag_id}):
			content.append(tag.text.encode('utf-8'))
	elif cls_name=='null' and tag_id=='null':
		for tag in soup.find_all(tag_name):
			content.append(tag.text.encode('utf-8'))

	'''

def scraper(url, tag_name, attr, attr_name):

	''' BEAUTIFUL SOUP INIT '''
	web=urllib2.urlopen(url)
	soup=BeautifulSoup(web,'html.parser',from_encoding='utf-8')

	''' ***** CONTENT LIST ***** '''
	content=[]


	if attr == 'class':
		for tag in soup.find_all(tag_name, attrs={'class':attr_name}):
			content.append(tag.text.encode('utf-8'))	
	
	elif attr == 'id':
		for tag in soup.find_all(tag_name, attrs={'id':attr_name}):
			content.append(tag.text.encode('utf-8'))
	
	elif attr == 'null' and attr == 'null':
		for tag in soup.find_all(tag_name):
			content.append(tag.text.encode('utf-8'))

	print content
	
	''' ***** DATE DICTIONARY ***** '''
	'''
	date=[]

	for tag in soup.find_all(tag_name,{'class':cls_name}):
		date.append(tag.text.encode('utf-8'))	
	
	'''

	''' **** Multiple DICTIONARY **** '''
	'''
	multiple=[]

	for i in range(0,len(content)):
		result= date[i] +' '+ content[i]
		multiple.append(result)	

	print multiple
	'''

if __name__=='__main__':
	
	'''MODULE PARAMETERS'''

	url=raw_input()
	tag_name=raw_input()
	attr=raw_input()
	attr_name=raw_input()
	
	if tag_name == 'img':
		scrape_img(url, tag_name, attr , attr_name)
	else:
		scraper(url, tag_name, attr, attr_name)	










