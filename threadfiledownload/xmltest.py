from xml.etree.ElementTree import parse

tree = parse('../XMLfiles/trmmdownloader.xml')
root = tree.getroot()

trmm = root.findall("TRMM_RT")
'''
name = [x.findtext("name") for x in student]
age = [x.findtext("age") for x in student]
score = [x.find("sco''re").attrib for x in student]
'''

link = [x.findtext("LINK") for x in trmm]
print(link)

