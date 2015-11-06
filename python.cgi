#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
cgitb.enable()    
print("Content-Type: text/html;charset=utf-8")
print 
import cgi 
from bs4 import BeautifulSoup
import urllib2


form = cgi.FieldStorage()
url = form.getvalue("url")
tag_name = form.getvalue("tag_name")
attr = form.getvalue("attr")
attr_name = form.getvalue("attr_name")

def scrape_img( url, tag_name, attr, attr_name ):

	''' BEAUTIFUL SOUP INIT '''
	
	web=urllib2.urlopen(url)
	soup=BeautifulSoup(web,'html.parser',from_encoding='utf-8')
	

	''' CONTENT LIST '''
	content=[]
	for link in soup.find_all(tag_name):
            all_links = link.get('src')
            content.append(all_links)
	print '<p>' + content + '</p>'

	


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

	print '<title>CGI SCRIPT</title>'
	print '<h1>'+ str(content[0]) + '</h1>'


if tag_name == 'img':
		scrape_img(url, tag_name, attr , attr_name)
else:
		scraper(url, tag_name, attr, attr_name)
