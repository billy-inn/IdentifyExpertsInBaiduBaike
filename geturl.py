# coding=utf-8
import re
import urllib
import capture

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def search(name, info):
	key = name.encode('utf-8')
	url = "http://baike.baidu.com/search?word=%s&pn=0&rn=0&enc=utf8" % key
	html = getHtml(url)

	firstname = name[1:].encode('utf-8')
	familyname = name[0].encode('utf-8')
	
	reg = r'<a href="http://baike.baidu.com/(sub)?view/[0-9]*(/[0-9]*)?\.htm" target="_blank"><em>%s.*%s</em>' % (familyname,firstname)
	urlre = re.compile(reg)
	ans = re.search(urlre,html)
	
	if ans is None:
		print "No Found!"
		return
	else:
		print ans.group()
	
	reg = r'view/[0-9]*(\.htm|/)'
	urlre = re.compile(reg)
	url = re.search(urlre,ans.group())
	url = 'http://baike.baidu.com/%s.htm' % url.group().strip('/htm.')
	
	html = getHtml(url)
	reg = r'/subview/[0-9]*/[0-9]*\.htm'
	urlre = re.compile(reg)
	urlList = re.findall(urlre,html)

	html = getHtml(url)
	key = info.encode('utf-8')
	
	reg = r'%s' % key
	infore = re.compile(reg)
	ans = re.search(infore,html)
	if ans is not None:
		capture.capture(url)
		return

	for url in urlList:
		url = 'http://baike.baidu.com' + url
		html = getHtml(url)
		key = info.encode('utf-8')

		reg = r'%s' % key
		infore = re.compile(reg)
		ans = re.search(infore,html)
		if ans is not None:
			capture.capture(url)
			return
