import pandas as pd
from bs4 import BeautifulSoup


results = []

with open('sitemap.xml', 'r', encoding='utf-8') as file:
    bs = BeautifulSoup(file.read(), 'lxml')
urls = bs.find_all('url')

for url in urls:
    temp = dict()
    temp['Url'] = url.loc.text
    temp['Last modified'] = url.lastmod.text
    temp['Change frequency'] = url.changefreq.text
    temp['Priority'] = url.priority.text
    results.append(temp)

df = pd.DataFrame(results)
df.index += 1
df.to_excel('results.xlsx')
