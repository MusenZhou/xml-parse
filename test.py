import xml.etree.ElementTree as ET

mytree = ET.parse('test.xml')
myroot = mytree.getroot()

for x in myroot[0]:
	print(x.tag, x.attrib)


for x in myroot[0]:
	print(x.tag, x.attrib)



for x in myroot.findall('food'):
	item = x.find('item').text
	price=x.find('price').text
	print(item, price)






