""" PROJECT SCRAPER """		

from bs4 import BeautifulSoup
import urllib2



def scraper(url, outer_tag, outer_attr, outer_attr_name, inner_tag, inner_attr, inner_attr_name):

	''' BEAUTIFUL SOUP INIT '''
	web=urllib2.urlopen(url)
	soup=BeautifulSoup(web,'html.parser',from_encoding='utf-8')

	''' ***** CONTENT LIST ***** '''
	content=[]
	

	for outer_ in soup.find_all(outer_tag,{outer_attr : outer_attr_name}):
		for inner_ in outer_.find_all( inner_tag,{inner_attr : inner_attr_name}):
			content.append(inner_.text.encode('utf-8'))
	for i in range(len(content)):
		content[i]=' '.join(content[i].split())
		#content[i]= ''.join([ch for ch in content[i] if ord(ch)<=128])
		#content[i]=content[i].strip()
	print content


def decode_prams():
	pass

if __name__=='__main__':
	print 'url'
	url=raw_input()
	print 'outer tag name'
	outer_tag=raw_input()
	print ' outer attr'
	outer_attr=raw_input()
	print 'outer attr name'
	outer_attr_name=raw_input()
	print 'inner tag'
	inner_tag=raw_input()
	print 'inner attr'
	inner_attr=raw_input()
	print 'inner attr name'
	inner_attr_name=raw_input()
	scraper(url, outer_tag, outer_attr, outer_attr_name, inner_tag, inner_attr, inner_attr_name)
