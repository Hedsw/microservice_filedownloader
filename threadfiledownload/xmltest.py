from xml.etree.ElementTree import parse

tree = parse('../XMLfiles/alternativefile.xml')
root = tree.getroot()

trmm = root.findall("DATA")
#print(trmm)
'''
name = [x.findtext("name") for x in student]
age = [x.findtext("age") for x in student]
score = [x.find("sco''re").attrib for x in student]
'''

link = [x.findtext("LINK") for x in trmm]
types = [x.findtext("TYPES") for x in trmm]
start_year = [x.findtext("START_YEAR") for x in trmm]
end_year = [x.findtext("END_YEAR") for x in trmm]

url = link[0] + "/" + types[0] + "/" 
print(start_year)

print(url)