# coding: utf8
import urllib.request
from chardet.universaldetector import UniversalDetector

def get_encoding(file):
    detector = UniversalDetector()
    with open(file, 'rb') as f:
        line = f.readline()
        detector.feed(line)
    detector.close()
    return detector.result['encoding']

charset1="utf-8" #WEB
charset2="GB2312" #host // chardet is shit
fileh='C:/Windows/System32/drivers/etc/hosts'
URL='https://gitlab.com/ineo6/hosts/-/raw/master/next-hosts?ref_type=heads'
line0="# 地址可能会变动，请务必关注GitHub、Gitlab获取最新消息"
linez="# GitHub Host End"

raw1=urllib.request.urlopen(URL)
html=raw1.read()
print("====Fetching text from : "+URL)

charsetX=get_encoding(fileh)
if charsetX!="ascii":
	charset2=charsetX
print("====Encoding: "+charset1 +" to "+charset2)

data0 = html.decode(charset1)
dataX= data0.encode(charset2)
data1= dataX.decode(charset2)

font_end=0
after_start=0
data_old = ""  # 前部分

#r+ 读写 w新建 a追加
with open(fileh, "r+",encoding=charset2) as fp:
	for i, d in enumerate(fp.readlines(), start= 1):
		#提取前部数据
		if font_end !=1:
			if d.find(line0) != -1: 
				font_end=1
			else:
				data_old += d
		#补加后面数据
		if d.find(linez) != -1:
			after_start=1
		elif after_start==1:
			data_old += d
		print("====INSERT OLD DATA: \n"+data_old)
#with open("./tests.txt", "w+",encoding=charset2) as fp:
	fp.seek(0)
	fp.write(data_old+"\n")
	fp.write(data1)
print("==== DONE")