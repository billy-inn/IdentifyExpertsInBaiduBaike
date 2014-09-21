# coding=utf-8
import re
import urllib
import urllib2
import capture
import time

def getHtml(url):
	heads = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36',
	#'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	#'Accept-Language':'Izh-CN,zh;q=0.8,en;q=0.6',
	#'Accept-Encoding':'gzip,deflate,sdch',
	#'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3',
    #'Cache-Control':'max-age=0',
	#'Connection':'keep-alive',
	#'Keep-Alive':'115',
	'Referer':url,
	#'Host':'baike.baidu.com'
	}
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
	urllib2.install_opener(opener) 
	req = urllib2.Request(url)
	opener.addheaders = heads.items()
	def get():
		try:
			html = opener.open(req).read()
		except Exception:
			html = get()
		return html
	html = get()
	return html

def split_org(org):
	split_word_list = ["大学","院"]
	for split_word in split_word_list:
		reg = r'%s' % split_word
		split_re = re.compile(reg)
		org_list = re.split(split_re,org,1)
		if org_list[0] == org or org_list[0]+split_word == org: continue
		org_list[0] += split_word
		return org_list
	return [org,]

def search(name, org, title, keyword):
	key = name.encode('utf-8')
	url = "http://baike.baidu.com/search?word=%s&pn=0&rn=0&enc=utf8" % key
	html = getHtml(url)

	firstname = name[1:].encode('utf-8')
	familyname = name[0].encode('utf-8')
	
	reg = r'<a href="http://baike.baidu.com/(sub)?view/[0-9]*(/[0-9]*)?\.htm" target="_blank"><em>%s(</em><em>)?%s</em>' % (familyname,firstname)
	urlre = re.compile(reg)
	ans = re.search(urlre,html)
	
	if ans is None:
		return "No Found!"
	
	reg = r'view/[0-9]*(\.htm|/)'
	urlre = re.compile(reg)
	ID = re.search(urlre,ans.group())
	url = 'http://baike.baidu.com/%s.htm' % ID.group().strip('/htm.')
	
	html = getHtml(url)
	reg = r'/sub%s/[0-9]*\.htm' % ID.group().strip('/htm.')
	urlre = re.compile(reg)
	urlList = re.findall(urlre,html)

	key_org = org.encode('utf-8')
	key_title = title.encode('utf-8')
	split_word = "拆分词条"
	split_re = re.compile(split_word)

	orgList = split_org(key_org)
	for item in orgList:
		item = item.strip('/')
		#print item

	keywordList = []
	for word in keyword:
		key_word = word.encode('utf-8')
		keywordList.append(key_word)

	fw = open('trainingSet/%s.txt' % ID.group().strip('/htm.view'),"w")

	if len(urlList) == 0:
		html = getHtml(url)
		
		org_val = 0
		for word in orgList:
			reg = r'%s' % word
			org_re = re.compile(reg)
			org_ans = re.findall(org_re,html)
			org_val += len(org_ans)

		reg = r'%s' % key_title
		title_re = re.compile(reg)
		title_ans = re.findall(title_re,html)
		title_val = 0
		if len(title_ans) > 0: title_val = 1

		keyword_val = 0
		for word in keywordList:
			reg = r'%s' % word
			word_re = re.compile(reg)
			word_ans = re.findall(word_re,html)
			keyword_val += len(word_ans)

		#fw.write("%s %d %d %d " % (url, title_val, org_val, keyword_val))
		#print url, title_val, org_val, keyword_val
		if org_val > 0: 
			#capture.capture(url)
			return url
		else:
			return 'No Found!'
		#label = raw_input()
		#fw.write("%s\n" % label)

	maxVal = 0
	targetUrl = -1

	for url in urlList:
		url = 'http://baike.baidu.com' + url
		Html = getHtml(url)
		htmlList = re.split(split_re,Html)
		if len(htmlList) < 2: continue
		html = htmlList[1]
		
		org_val = 0
		for word in orgList:
			reg = r'%s' % word
			org_re = re.compile(reg)
			org_ans = re.findall(org_re,html)
			org_val += len(org_ans)

		reg = r'%s' % key_title
		title_re = re.compile(reg)
		title_ans = re.findall(title_re,html)
		title_val = 0
		if len(title_ans) > 0: title_val = 1

		keyword_val = 0
		for word in keywordList:
			reg = r'%s' % word
			word_re = re.compile(reg)
			word_ans = re.findall(word_re,html)
			keyword_val += len(word_ans)

		#fw.write("%s %d %d %d " % (url, title_val, org_val, keyword_val))
		#print url, title_val, org_val, keyword_val
		if maxVal < title_val + org_val + keyword_val:
			maxVal = title_val + org_val + keyword_val
			targetUrl = url
		#label = raw_input()
		#fw.write("%s\n" % label)

	if maxVal > 1: 
		#capture.capture(targetUrl)
		return targetUrl
	else:
		return 'No Found!' 

#	key = info.encode('utf-8')
	
#	reg = r'%s' % key
#	infore = re.compile(reg)
#	ans = re.search(infore,html)
#	if ans is not None:
#		capture.capture(url)
#		return
#
#	for url in urlList:
#		url = 'http://baike.baidu.com' + url
#		html = getHtml(url)
#		ans = re.search(infore,html)
#		if ans is not None:
#			capture.capture(url)
#			return
