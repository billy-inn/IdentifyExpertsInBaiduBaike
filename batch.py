# coding=utf-8
import read
import geturl

fr = open('fileList.txt','r')
fileList = fr.readlines()
fr.close()

fw = open('ans.txt','a')

cnt = 24
n = len(fileList)

while cnt <= n:
	name,title,org,keyword = read.read('reviewer/'+fileList[cnt-1].strip())
	url = geturl.search(name,org,title,keyword)
	fw.write('%s %s %s %s\n' % (name.encode('utf-8'),title.encode('utf-8'),org.encode('utf-8'),url))
	print cnt
	cnt += 1

fw.close()
