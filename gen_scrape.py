
def scraper( url, tag, tag_id, tag_class):

	import urllib2
	from bs4 import BeautifulSoup

	# PULL WEBSITE DATA
	website=urllib2.urlopen(url)
	soup=BeautifulSoup(website,'html.parser',from_encoding='utf-8')
	
	# DATA COLLECTOR LIST 
	content=[]	
	
	#PULL DATA FROM TAG [ NO ID/ NO CLASS ]
	if(tag_id=='null' and tag_class=='null'):
		with open('output.txt','w') as file:
			for tag in soup.find_all(tag):
				file.write(tag.text.encode('utf-8')+ "\n")

	#PULL DATA FROM TAG CLASS	
	elif(tag_id=='null'):
		for tag in soup.find_all(tag,{'class':tag_class}):
			content.append(tag.text.encode('utf-8'))
	
        print(content)


scraper('http://www.reuters.com/article/2015/11/03/us-asean-malaysia-idUSKCN0SS07F20151103','p','null','null')
