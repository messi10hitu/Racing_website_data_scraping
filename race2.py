import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/58.0.3029.110 Safari/537.3'}

url = "https://www.tabtouch.com.au/racing/hub?date=2020-04-27&code=&_=1587974484370"

label1 = []
label2 = []
# STEP 1. get the HTML.
r = requests.get(url)
html_content = r.content
# print(html_content)
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.text)
table = soup.find("table", id="race-hub-races")
# print(table)
for row in table.find_all("tr"):
    for th in row.find_all("th"):
        print(th.text)
        label2.append(th.text)
# print(label2)
ser1 = pd.Series(label2)

# for data in tables except headings
for row in table.find_all("tr"):
    # print(row.text)
    for cell in row.find_all("td"):
        # print(cell.text)
        for anchor in cell.find_all("a"):
            label1.append(anchor.text)
l1 = label1[0:9]
l2 = label1[9:23]
l3 = label1[23:35]
l4 = label1[35:45]
l5 = label1[45:57]
# print(l5)

l6 = label1[57:66]
l7 = label1[66:75]
l8 = label1[75:88]
l9 = label1[88:98]
l10 = label1[98:109]
l11 = label1[109:123]
l12 = label1[123:133]
l13 = label1[133:147]
l14 = label1[147:159]
l15 = label1[159:168]
l16 = label1[168:178]
l17 = label1[178:192]
l18 = label1[192:203]
l19 = label1[203:213]
l20 = label1[213:224]
l21 = label1[224:236]
l22 = label1[236:248]
l23 = label1[248:251]
l24 = label1[251:263]
print(l24)

# convert data into series to concatinate it
ser2 = pd.Series(l1)
ser3 = pd.Series(l2)
ser4 = pd.Series(l3)
ser5 = pd.Series(l4)
ser6 = pd.Series(l5)
ser7 = pd.Series(l6)
ser8 = pd.Series(l7)
ser9 = pd.Series(l8)
ser10 = pd.Series(l9)
ser11 = pd.Series(l10)
ser12 = pd.Series(l11)
ser13 = pd.Series(l12)
ser14 = pd.Series(l13)
ser15 = pd.Series(l14)
ser16 = pd.Series(l15)
ser17 = pd.Series(l16)
ser18 = pd.Series(l17)
ser19 = pd.Series(l18)
ser20 = pd.Series(l19)
ser21 = pd.Series(l20)
ser22 = pd.Series(l21)
ser23 = pd.Series(l22)
ser24 = pd.Series(l23)
ser25 = pd.Series(l24)

df1 = pd.concat([ser1, ser2, ser3,ser4,ser5,ser6,ser7,ser8,ser9,ser10,ser11,ser12,ser13,ser14,ser15,ser16,ser17,ser18,ser19,ser20,ser21,ser21,ser22,ser23,ser24,ser25],axis=1)
print(df1)
df1.to_csv("race.csv")
# df1 = pd.DataFrame(l1, columns=["Meetings"])  # dataframe is an excel sheet which we can use in the python

# frame = pd.concat(df2,l1)
# print(frame)
# df1['NAME'] = pd.DataFrame(l2)  # dataframe is an excel sheet which we can use in the python
# print(df1)


# l1 = list(dict.fromkeys(label1))
# df = pd.DataFrame(l1)
# print(df)

# with open('race.csv', 'w')as r:
#     for row in table.find_all("tr"):
#         for cell in row.find_all("td"):
#             for anchor in cell.find_all("a"):
#                 r.write(anchor.text.ljust(22))
#             r.write('\n ')

        # label1.append(cell.text)  #         label1.append(row.find_all("td")[0].text)  # it is showing me duplicates
#         label2.append(row.find_all("td")[1].text)  # it is showing me duplicates
#         label3.append(row.find_all("td")[1].text)  # it is showing me duplicates
#
# l1 = list(dict.fromkeys(label1))
# l2 = list(dict.fromkeys(label2))
# l3 = list(dict.fromkeys(label3))
# print(l1)
# print(l2)
# print(l3)

# df1 = pd.DataFrame(l1, columns=["RK"])  # dataframe is an excel sheet which we can use in the python
# # print(df1)
# df1['NAME'] = pd.DataFrame(l2)  # dataframe is an excel sheet which we can use in the python
# print(df1)
# df1.to_csv("new_race.csv")

# Parse JSON – convert the string to JSON:
# parsed = json.loads(html_content)
#
# print(json.dumps(parsed, indent=4))
# r = r.status_code
# print(r)
# print(r.text)
# print(r.json)
