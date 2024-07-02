import urllib.request
import xml.etree.ElementTree as ET

url = "https://www.w3schools.com/xml/cd_catalog.xml"

response = urllib.request.urlopen(url)
data = response.read()

tree = ET.ElementTree(ET.fromstring(data))
root = tree.getroot()

results = []

for cd in root.findall('CD'):
    artist = cd.find('ARTIST').text
    title = cd.find('TITLE').text
    results.append((artist, title))

print("Zestaw utworów i wykonawców:")
print(results)
