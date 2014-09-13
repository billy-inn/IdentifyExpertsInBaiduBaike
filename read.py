#coding=utf-8
import xml.dom.minidom

def read(filename):
	file_xml = open(filename,"r").read()
	file_xml = file_xml.decode('gbk').encode('utf-8')

	dom = xml.dom.minidom.parseString(file_xml)

	root = dom.documentElement

	psn_name = root.getElementsByTagName('psn_name')
	org_name = root.getElementsByTagName('org_name')
	prof_title_name = root.getElementsByTagName('prof_title_name')
	zh_keywords = root.getElementsByTagName('zh_keywords')
	#zh_title = root.getElementsByTagName('zh_title')
	
	wordSet = set()

	for node in zh_keywords:
		keyword = node.getElementsByTagName('keyword')
		for item in keyword:
			word = item.firstChild.data
			if word not in wordSet:
				wordSet.add(word)
	
	return psn_name[0].firstChild.data,prof_title_name[0].firstChild.data \
			,org_name[0].firstChild.data,wordSet


