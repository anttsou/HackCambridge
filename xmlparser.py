from lxml import html
import requests

def parseFromUrl(URL):
   page = requests.get(URL)
   tree = html.fromstring(page.content)
   tags= tree.xpath('//p/text()')
   tags +=tree.xpath('//a/text()')
   for i in range (1,4):
      tags+=tree.xpath('//h' + str(i) + '/text()')
   tags +=tree.xpath('//span/text()')
   return tags

def parseFromList(urlList):
   rtn = ['']
   for url in urlList:
      rtn += parseFromUrl(url)
   return ' '.join(rtn)

