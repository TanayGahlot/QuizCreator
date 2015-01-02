#oggpnosn
#hkhr 

import scrapy 
from scrapy.selector import Selector
from urllib2 import urlopen 
import threading 

baseUrl = "http://www.indiabix.com"
threads = []
mainUrl = "http://www.indiabix.com/engineering/"

response = urlopen(mainUrl)
text = response.read()
selector = Selector(text = text)

questionBank = []
fob = open("engineering.txt", "w")
fob.write("[")
def extractPage(elements):
	print elements
	for element in elements:
		if element:
			url = baseUrl + element;print url 
			text = urlopen(url).read()
			page = Selector(text = text)
			for questionNo in range(1,7):
				document = {}
				question = page.xpath("/html/body/div[1]/table[2]/tr[2]/td[2]/table/tr/td/div["+str(questionNo)+"]/table/tr[1]/td[2]/p/text()").extract()
				if question:
					question = question[0]
					choice = []
					flag = True
					for choiceNo in range(1,5):
						choiceText = page.xpath("/html/body/div[1]/table[2]/tr[2]/td[2]/table/tr/td/div["+str(questionNo)+"]/table/tr[2]/td/table/tr["+str(choiceNo)+"]/td[2]/text()").extract()
						if choiceText:
							choice.append(choiceText[0])
						else:
							choice.append("")
							flag = False
				#correctChoice = page.xpath("").extract()
					if flag == True:			
						fob.write(question + "\n") 
						fob.write("A)" + choice[0] + "\n")
						fob.write("B)" + choice[1] + "\n") 
						fob.write("C)" + choice[2] + "\n")	 
						fob.write("D)" + choice[3] + "\n")	 
				#document["correctChoice"] = correctChoice
				#document["category"] = element[0]	
				#questionBank.append(document)
				#fob.write(str(document) + ",")

elements = []
for i in range(1,7):
	for j in range(1,4):
		xpath = "/html/body/div[1]/table[2]/tr/td[1]/table/tr/td/table/tr[" + str(i) + "]/td["+ str(j) + "]/a/@href"
		element = selector.xpath(xpath).extract()
		if element: 
			elements.append(element[0])
		else:
			elements.append("")	

extractPage(elements)

#fob = open("questions.json", "w")
#import json 
#json.dump(questionBank, fob)
#fob.close()
